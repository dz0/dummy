import sys
# import traceback
import inspect
import linecache
import py

### GLOBALS
stack_defs_original_indents = []
stack_output_indents = []
last_indent = 0


depth = 0
MAX_DEPTH = 30

visited_lines = [] # not to visit the same again.. ID by filnename + lineno
visited_calls = [] # not to visit the same again.. ID by filnename + lineno
from collections import defaultdict, OrderedDict
call_map = defaultdict(list) # caller_lineID: [funcID1, funcID2..]
traced_values = OrderedDict()
codes = {}  # codes of functions

start_frame = None    

### end GLOBALS

def fileID(frame):
    co = frame.f_code
    filename = co.co_filename    
    return filename
    
def moduleID(frame):  # more readable than fileID
    module = inspect.getmodule( frame.f_code )
    module = module and module.__name__ 
    return module
    
SEP_4ID = "-"  # separator (or joiner) for ID (module to function or so)
def join_ids( *args ):
    return SEP_4ID.join( map(str, args))
    
def lineID(frame):
    lineno = frame.f_lineno
    return join_ids(moduleID(frame), lineno)  # to be suitable for HTML DOM ID
    # return (moduleID(frame), lineno)
    # return (fileID(frame), lineno)
    
def funcID(frame):
    qualname = get_qualname(frame)
    module = moduleID(frame)
    return join_ids(module, qualname) #  to be suitable for HTML DOM ID
    # return (module, qualname)
    # return (frame.f_code.co_filename , qualname)
    
def getline(filename, lineno):

    return linecache.getline(filename, lineno )  # it kind of ignores file errors

    """
    try:
        # line = linecache.getline(filename, lineno-1 )
        line = open(filename).readlines()[ lineno-1 ] # to notice file errors
    except FileNotFoundError as e:
        for path in ["<frozen importlib._bootstrap>", "<ipython-input-"]:
            if path in str(e):
                    break
        else:
            print ("FileNotFoundError", e)
    """
                
def format_inspect_stack(stack, start_frame, end_frame):
     # FrameInfo(frame, filename, lineno, function, code_context, index)
    calls = []
    for fi in stack:
        # line = open(fi.filename).readlines()[ fi.lineno-1 ]
        line = getline(fi.filename, fi.lineno )
        
        func_name = fi.frame.f_code.co_name
        calls.insert(0, f'{fi.filename}:{fi.lineno}:{func_name}: {line}' )
        if fi.frame is start_frame:
            break
        
    calls = ['  '*i + "-> " + line for i, line in enumerate( calls ) ] # add indents
    return ''.join( calls )



    
def ajust_indent( line ):
    orig_indent = len(line) - len(line.lstrip())
    if stack_defs_original_indents:
        indent_inside_def = orig_indent - stack_defs_original_indents[-1]
    else:
        indent_inside_def = 0
        
    output_indent = stack_output_indents[-1] if stack_output_indents else 0
    
    new_indent = output_indent + indent_inside_def
    return " " * new_indent  + line.lstrip()

def apply_indent( line ):
    output_indent = stack_output_indents[-1] if stack_output_indents else 0
    return output_indent * ' '   + line

pySource_cache = {}
def get_file_pySource(path):
    # could cash
    if not path in pySource_cache:
        with open(path) as f:
            pySource_cache[path] = py.code.Source( f.read() )
    return pySource_cache[path]

    
def log_line(frame, extra=""):
    lineno = frame.f_lineno
    co = frame.f_code
    filename = co.co_filename    
    id = lineID(frame)
    if id not in visited_lines:
        line =  ajust_indent( getline(filename,lineno ) )
        global last_indent
        
        def get_current_statement_indent(line):
            return len(line) - len(line.lstrip())
            
            
        def get_first_statement_lineno(filename, lineno):
            s = get_file_pySource( filename )
            # print("DBG src", s)
            if s:
                # print("DBG pySrc line", s.getstatement( lineno ) )  # could do auto dedent...
                statement_start = s.getstatementrange( lineno-1 )[0]  
                return statement_start+1
                
        if lineno == get_first_statement_lineno(filename, lineno):
            # TODO if the call happens not at the end of statement -- use last line indent instead.., 
            last_indent = get_current_statement_indent(line)
            

        line = line.rstrip('\n') +extra
        print( line )
        
    visited_lines.append( id ) # TODO: maybe log only once? or make ordered dict?

    
def get_func_header(frame): 
    co = frame.f_code
    # print("DBG", co )
    try:
        header = inspect.getsourcelines( co )[0][0]
        # print("DBG getsourcelines", inspect.getsourcelines( co ) )
        header = header.rstrip() 
    except TypeError:
        header = None
    return header


def get_qualname(frame):
    
    # https://stackoverflow.com/a/2544639/4217317
    def get_class_name(f):
        try:
            return f.f_locals['self'].__class__.__name__
        except KeyError:
            return None
    classname = get_class_name( frame )
    
    if classname:
        return classname+'.'+frame.f_code.co_name
    else:
        return frame.f_code.co_name
    """    
    try:
        obj = frame.f_locals['self']
        func_obj = getattr(obj, frame.f_code.co_name)
        return func_obj.__qualname__
    except (KeyError, AttributeError):
        return None
        
    # func_obj = frame.f_globals.get(frame.f_code.co_name)
    # qualname = func_obj and func_obj.__qualname__   or ""
    """        


def trace_calls(frame, event, arg):
    global start_frame
    global last_indent


    co = frame.f_code
    func_name = co.co_name
    func_line_no = lineno = frame.f_lineno
    func_filename = filename = co.co_filename
    
    try:
        module = inspect.getmodule( frame.f_code )
        module = module and module.__name__ 
    except Exception as e:
        print("no module here", e, frame)
        print(filename, lineno)
        # print(getline(filename, lineno))
        module =  "???"


    if event == 'line':
        log_line( frame )#, extra=f"  # line: {frame.f_lineno}, {frame.f_locals}   #module {module}" )
        
        return trace_calls #FIXME
        """
        line = getline( filename, line_no) 
        # target:         df = df.pivot(columns='label', values='value', index='time_index') # in emitter.py:get_dataframe(..)
        if '# TRACE:' in  line:
            print ("!!!", line)
            

            print("inspect STACK\n")
            print(format_inspect_stack( inspect.stack()[1:], start_frame, end_frame=frame  )   )

            target_vars = line.split('# TRACE:')[-1].strip()
            
            # print("TRACEVAR:", target_vars, eval(target_vars, None, frame.f_locals ))
            
            target_vars = target_vars.split(',') 
            for target_var in map(str.strip, target_vars):
                # print("TRACEVAR:", target_var, frame.f_locals[target_var])
                print("TRACEVAR:", target_var, eval(target_var, frame.f_globals, frame.f_locals ) )
         """   

    elif module in ["__main__", "test_mytracer"] or module and module.startswith("csv2df"):
    # if True:
        
        """
        #skip if already visited
        if lineID(frame) in visited_calls:  # TODO: allow duplicate visits -- as it may mean different lines inside call
            # if event == 'call':
                # print( apply_indent( last_indent*' ' + '#@skip_inline (already visited)') )
            pass
            # FIXME: TODO deprecate -- as when calling it should include "caller line" -- better use call_map
            # return trace_calls    
            
        else:
            visited_calls.append( lineID(frame)  )  # now this includes returns as well...
        """    
        
        global depth
        
        if event == 'call':
            # print("DBG call", filename, lineno)

            depth += 1

            if depth < MAX_DEPTH:
                
                header = get_func_header( frame ) 
                if header is None:
                    print("DBG no function header", filename, lineno)
                    return trace_calls
                # else:
                    # print("DBG HEADER", header)

                stack_output_indents.append( last_indent )  
                # print("DBG last_indent", last_indent, stack_output_indents)
                orig_indent = len(header) - len(header.lstrip() )
                # print("Header orig_indent", header, orig_indent)
                header = apply_indent( header.lstrip() ) # should go here:  after  orig_indent and  before append            
                qualname = get_qualname(frame)
                fID = funcID( frame )
                if not fID in codes:
                    codes[ fID ] = inspect.getsourcelines( frame.f_code )
                
                
                print( apply_indent( f"#@inline {depth}: {module}. {qualname} " ))
                print( header )
                stack_defs_original_indents.append( orig_indent ) 

               
                def inspect_caller(frame):
                    caller = frame.f_back
                    if caller is None:
                        print ("DBG, strange, caller is None", frame, lineID(frame) )
                        return 
                    else:
                        caller_lineno = caller.f_lineno
                        caller_filename = caller.f_code.co_filename
                        # print( apply_indent( f"#@caller {caller_lineno} @{caller_filename} " ))
                        
                        called_from_line = call_map[ lineID(caller) ]
                        if fID not in called_from_line: 
                            called_from_line.append( fID )
                    
                        if func_name == 'get_dataframes': # TODO -- make option..
                            global start_frame
                            start_frame = caller
                inspect_caller(frame) 
                
            return trace_calls
            
        if event == 'return':
            if depth < MAX_DEPTH:
                # print (apply_indent( '#@inline_end'))
                def head( val, cnt=30 ):
                    val = str(val)
                    if len(val) > cnt:
                        val = val[:cnt]+"..."
                    return val
                    
                
                retval = arg
                print (apply_indent( '#@return: %s => %s' % (func_name, head(retval) )))
                
                # if stack_defs_original_indents: stack_defs_original_indents.pop()
                stack_defs_original_indents.pop()
                # if stack_output_indents: stack_output_indents.pop()
                last_indent = stack_output_indents.pop()
                
                # last_indent = stack_output_indents[-1]
                
            depth -= 1
                             
        
     

if True:
   def A(*args, **kwargs): 
        a = 5
        print(
          "A"
          )
        if a > 10:
            print("a > 10")
        else:
            print("a <= 10")
        
        c = C()
        for x in range(3):
            C()
        return a
    
if True:
      def B(): 
                 print("start B")
                 x = 42  
                 u = (A(
                   x=C() ,
                   y=3,
                    z=2
                      
                 )
                 )
                
                 print("end B")

def C():
         print("C")
         return 2


if __name__=="__main__":
    # tests
    
    import test_mytracer

    import sys

    # grab stdout https://stackoverflow.com/a/45567127/4217317  
    import  io
    stdout = sys.stdout
    sys.stdout = io.StringIO()
    sys.settrace(trace_calls)
    
    try:
        print()
        B()
        
        # test_mytracer.test()
        # sys.settrace(None)
        
    finally:
        
        sys.settrace(None)
        output = sys.stdout.getvalue()
        sys.stdout = stdout
        with open('out_inlined.py', 'w') as f:
            f.write( output )
            # print( output )
        
        import mytracer_render 
        # monkeypach inject some stuff
        mytracer_render.SEP_4ID = SEP_4ID
        mytracer_render.join_ids = join_ids
        
        mytracer_render.render_html(visited_lines, codes, call_map, traced_values)

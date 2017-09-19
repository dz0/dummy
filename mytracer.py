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
watched_values = defaultdict(list) #OrderedDict() # key:val   will be   lineID: table of vars
watched_values_after_exec = defaultdict(list) 
stack_waiting_watched_values_after_exec = [None]; #defaultdict(list) #OrderedDict() # key:val   will be   lineID: list of dicts 
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
    result = SEP_4ID.join( map(str, args))
    # result = result.replace('.', '_' ) # for jquery, not to confuse '.' with classname -- refactored to use jquerify
    return result 
    
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

def log(*args, **vars):
    print(*args, **vars)
    
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
        log( line )
        
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
    funcname = frame.f_code.co_name
    if funcname in ["<lambda>", "<genexpr>", "<listcomp>", "<dictcomp>", "<setcomp>" ]:  #https://github.com/gak/pycallgraph/issues/156
        funcname = funcname + '[' + hex(id(frame.f_code)) + ']' +"_"+ lineID(frame)
        
    
    if classname:
        return classname+'.'+funcname
    else:
        return funcname
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
    filename = co.co_filename
    
    try:
        module = inspect.getmodule( frame.f_code )
        module = module and module.__name__ 
    except Exception as e:
        print("no module here", e, frame)
        print(filename, lineno)
        # print(getline(filename, lineno))
        module =  "???"

    def eval_watches( target_expressions, watch_timeline ):
        """ gets watch expressions values in current frame . Appends them to given watch_timeline table/list """
        # print("#WATCH:", target_expressions, eval(target_expressions, None, frame.f_locals ))
            
        line_watches = OrderedDict()
        for target_expr in map(str.strip, target_expressions):
            # print("DBG locals:",  frame.f_locals )
            try:
                line_watches[target_expr] = eval(target_expr, frame.f_globals, frame.f_locals )
            except NameError as e:
                print( "DBG", e, target_expr )
                line_watches[target_expr] = str(e)
            print("#WATCH:", target_expr, line_watches[target_expr] )
            # print("#WATCH:", target_var, frame.f_locals[target_var]) # wouldn't allow expressions
        
        if not watch_timeline: # it is table with headers in first row
            watch_timeline.append( target_expressions )
        watch_timeline. append( list( line_watches.values() ) )
        
        return line_watches

    if event == 'line':
        log_line( frame )#, extra=f"  # line: {frame.f_lineno}, {frame.f_locals}   #module {module}" )
        
                
        def track_watches():
            """ uses #WATCH[_AFTER] pragmas to take expression snapshots 
            Default WATCH takes the value before line execution (default settrace behaviour)
            WATCH_AFTER takes the value AFTER line execution (this is more robust (possibly buggy), as execution can jump into another function call before finishing)
            """
            ### watch after exec init  finally previous
            waiting_watches = stack_waiting_watched_values_after_exec[-1]
            if waiting_watches:
                line_id, target_expressions = waiting_watches
                eval_watches( target_expressions, watch_timeline=watched_values_after_exec[line_id] )
                stack_waiting_watched_values_after_exec[-1] = None
                                        
            line = getline( filename, lineno) 
            line_id = lineID( frame )
            # target:         df = df.pivot(columns='label', values='value', index='time_index') # in emitter.py:get_dataframe(..)

            for pragma in ['#WATCH:', '#WATCH_AFTER:' ]:
                if pragma  in  line:
                    target_expressions = line.split( pragma )[-1].strip()
                    target_expressions = target_expressions.split(';')  # todo use AST?
                    
                    if pragma == '#WATCH:':
                        # print("inspect STACK\n")
                        # print(format_inspect_stack( inspect.stack()[1:], start_frame, end_frame=frame  )   )
                        eval_watches( target_expressions, watch_timeline=watched_values[ line_id ] )
                    
                    if pragma == '#WATCH_AFTER:':                            
                        ### watch after exec init
                        stack_waiting_watched_values_after_exec[-1] = ( (lineID(frame), target_expressions) )
           
        
        track_watches()
        return trace_calls 

    elif module and module.startswith("test_mytracer_") or module and module.startswith("csv2df"):
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
        
        # ignore/skip calls that are apparent (TODO think twice if something important is not lost)
        if frame.f_code.co_name in ["<genexpr>", "<dictcomp>", "<setcomp>", "<listcomp>"]:
            return trace_calls


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
                stack_defs_original_indents.append( orig_indent ) 
                
                stack_waiting_watched_values_after_exec.append( None )
                
                # print("Header orig_indent", header, orig_indent)
                header = apply_indent( header.lstrip() ) # should go here:  after  orig_indent and  before append            
                qualname = get_qualname(frame)
                fID = funcID( frame )
                    
                if not fID in codes:
                    codes[ fID ] = inspect.getsourcelines( frame.f_code )
                
                
                log( apply_indent( f"#@inline {depth}: {module}. {qualname} " ))
                log( header )

               
                def inspect_caller(frame):
                    caller = frame.f_back
                    if caller is None:
                        log ("DBG, strange, caller is None", frame, lineID(frame) )
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
            
        elif event == 'return':
            if depth < MAX_DEPTH:
                # print (apply_indent( '#@inline_end'))
                def head( val, cnt=30 ):
                    val = str(val)
                    if len(val) > cnt:
                        val = val[:cnt]+"..."
                    return val
                    
                
                retval = arg
                log (apply_indent( '#@return: %s => %s' % (func_name, head(retval) )))
                
                # if stack_defs_original_indents: stack_defs_original_indents.pop()
                stack_defs_original_indents.pop()
                # if stack_output_indents: stack_output_indents.pop()
                last_indent = stack_output_indents.pop()
                
                waiting_watches = stack_waiting_watched_values_after_exec.pop()
                ### watch after exec init  finally previous
                if waiting_watches:
                    line_id, target_expressions = waiting_watches
                    eval_watches( target_expressions, watch_timeline=watched_values_after_exec[line_id] )
                
                # last_indent = stack_output_indents[-1]
                
            depth -= 1
        
        else:
            print("DBG WEIRD EVENT", event, frame.f_code)
    else:
        print( "#DBG ignoring", event, frame)
        
     



if __name__=="__main__":
    # tests
    
    import test_mytracer_simple
    import test_mytracer_kep

    import sys

    # grab stdout https://stackoverflow.com/a/45567127/4217317  
    import  io
    stdout = sys.stdout
    # sys.stdout = io.StringIO()  # turn on buffering output to file
    sys.settrace(trace_calls)
    
    try:
        print()
        
        # test_mytracer_simple.B()           
        test_mytracer_kep.test()
        
    finally:
        try:
            sys.settrace(None)
            output = sys.stdout.getvalue()
            sys.stdout = stdout
            
            with open('out_inlined.py', 'w') as f:
                f.write( output )
                # print( output )
        except AttributeError as e:
            print( e )
            
        import mytracer_render 
        # monkeypach inject some stuff
        mytracer_render.SEP_4ID = SEP_4ID
        mytracer_render.join_ids = join_ids
        
        mytracer_render.render_html(visited_lines, codes, call_map, watched_values, watched_values_after_exec)

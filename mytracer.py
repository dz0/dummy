import sys
# import traceback
import inspect
import linecache
       
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


stack_defs_original_indents = []
stack_output_indents = []
last_indent = 0

visited_lines = [] # not to visit the same again.. ID by filnename + lineno
visited_calls = [] # not to visit the same again.. ID by filnename + lineno

    
start_frame = None    
    
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

def log_line(frame, extra=""):
    lineno = frame.f_lineno
    co = frame.f_code
    filename = co.co_filename    
    id = (filename, lineno)
    if id not in visited_lines:
        line =  ajust_indent( getline(filename, lineno ))
        global last_indent
        last_indent = len(line) - len(line.lstrip())
        # if not stack_output_indents:
            # stack_output_indents.append( last_indent )
        line = line.rstrip('\n') +extra
        print( line )
    visited_lines.append( id )

    
def get_func_header(frame): 
    co = frame.f_code
    # print("DBG", co )
    try:
        header = inspect.getsourcelines( co )[0][0]
        header = header.rstrip() 
    except TypeError:
        header = None
    return header

def trace_calls(frame, event, arg):
    global start_frame

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

    # if func_name == 'trace_calls' and  event == 'call':
        # return

    if event == 'line':
        log_line( frame) #, extra=f"  # line: {frame.f_lineno}, {frame.f_locals}   #module {module}" )
        
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

    if module in ["__main__", "test_mytracer"] or module and module.startswith("csv2df"):
    # if True:
        
        #skip if already visited
        if (filename, lineno) in visited_calls:  
            # if event == 'call':
                # print( apply_indent( last_indent*' ' + '#@skip_inline (already visited)') )
            return trace_calls    
            
        visited_calls.append( (filename, lineno)  )
        

        if event == 'return':
            # print (apply_indent( '#@inline_end'))
            print (apply_indent( '#@inline_end return: %s => %s' % (func_name, repr(arg)[:20] )))
            
            # if stack_defs_original_indents: stack_defs_original_indents.pop()
            stack_defs_original_indents.pop()
            # if stack_output_indents: stack_output_indents.pop()
            stack_output_indents.pop()
           
        
        if event == 'call':
            # print("DBG call", filename, lineno)

            header = get_func_header( frame ) 
            if header is None:
                print("DBG no function header", filename, lineno)
                return trace_calls
            # else:
                # print("DBG HEADER", header)
                
            stack_output_indents.append( last_indent ) 
            orig_indent = len(header) - len(header.lstrip() )
            # print("Header orig_indent", header, orig_indent)
            header = apply_indent( header.lstrip() ) # should go here:  after  orig_indent and  before append            
            print( apply_indent( "#@inline:" ))
            print( header )
            stack_defs_original_indents.append( orig_indent ) 
            # print("DBG: stack_defs_original_indents", stack_defs_original_indents)  
            # print("DBG: stack_output_indents", stack_output_indents)   
           
            
            caller = frame.f_back
            if caller is None:
                return 

            caller_line_no = caller.f_lineno
            caller_filename = caller.f_code.co_filename
            
            #line = linecache.getline(caller_filename, caller_line_no-1 )
            #if '_assert_has_no_duplicate_rows' in  line:
            #        print ("!!! CALL", line)
            
                # print(header)
                    
            if func_name == 'get_dataframes':
                start_frame = caller
                                
                            
            return trace_calls


if True:
   def A(): 
        a = 5
        print("A")
        return a*C()
    
if True:
      def B(): 
         print("start B")
         x = 42  
         A()
         c = C()
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
    
    # B()
    

    test_mytracer.test()

    sys.settrace(None)
    
    output = sys.stdout.getvalue()
    sys.stdout = stdout
    with open('out_inlined.py', 'w') as f:
        f.write( output )
        

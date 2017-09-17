import sys
# import traceback
import inspect
import linecache
       

# file.func:var
tracked_info = ['test_trace.b:z']
def check_tracked_info( frame, only_assignments = False):
    """should work only for assignments"""

    co = frame.f_code
    func_name = co.co_name
    lineno = frame.f_lineno
    filename = co.co_filename[:-len(".py")]

    line = linecache.getline(filename, lineno-1 )

    if only_assignments:
        is_assignment = "=" in line and "==" not in line
        if not is_assignment:
            return 
        lhs = line[:line.index("=")].strip() 
        locals_ = {name: frame.f_locals[name] for name in  lhs.split(',')}
    else: 
        locals_ = frame.f_locals
        
    for inf in tracked_info:
        inf = inf.replace(':', '.')
        mod, func, var = inf.split('.')
        
        
        if ( mod, func ) == (filename, func_name ):
            for lvar in locals_:
                if var == lvar:
                    print(f"Tracked_var: {var}: {locals_[var]}")
                    
    
start_frame = None

def format_inspect_stack(stack, start_frame, end_frame):
     # FrameInfo(frame, filename, lineno, function, code_context, index)
    calls = []
    for fi in stack:
        # line = open(fi.filename).readlines()[ fi.lineno-1 ]
        line = linecache.getline(fi.filename, fi.lineno-1 )
        
        func_name = fi.frame.f_code.co_name
        calls.insert(0, f'{fi.filename}:{fi.lineno}:{func_name}: {line}' )
        if fi.frame is start_frame:
            break
        
    calls = ['  '*i + "-> " + line for i, line in enumerate( calls ) ] # add indents
    return ''.join( calls )


def trace_calls(frame, event, arg):

    co = frame.f_code
    func_name = co.co_name
    func_line_no = line_no = frame.f_lineno
    func_filename = filename = co.co_filename
    
    if func_name == 'trace_calls':
        return
    
    
        
    if event == 'return':
        print ('%s => %s' % (func_name, arg))
        if func_name == 'b':
            print( "LOCAL x", frame.f_locals['x'] )
        
    if event == 'call':

        
        caller = frame.f_back
        if caller is None:
            return 
        caller_line_no = caller.f_lineno
        caller_filename = caller.f_code.co_filename
        
        if func_name == 'a':
            global start_frame

            start_frame = caller
                        
        if func_name == 'write':
            # Ignore write() calls from print statements
            return
        
        # print ('Call to %s on line %s of %s from line %s of %s' % \
                # (func_name, func_line_no, func_filename,
                 # caller_line_no, caller_filename)
         # )
        caller_line = open(caller_filename).readlines()[ caller_line_no-1 ]
        print( caller_line )
        return trace_calls

    if event == 'line':
        line = open(filename).readlines()[ line_no-1 ]
        
        check_tracked_info( frame )
        
        if 'return' in  line:
            print ("!!!", line)
            # traceback.print_stack()
            # print("traceback STACK: ", ''.join( traceback.format_stack()[:-1]))
                    
            print("inspect STACK\n")
            print(format_inspect_stack( inspect.stack()[1:], start_frame, end_frame=frame  )   )
        
def c():
    print("in c()")
    pass  # HERE
    
def b(x):
    print ('in b()')
    z = x
    c()
    return "ret b"

def a():
    print ('in a()')
    b(4)
    return "ret a"

def start(): 
    a()

sys.settrace(trace_calls)
start()


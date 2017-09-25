"""defines what code to trace 
and what expressions in which lines or watch"""
# import mytracer
from mytracer import moduleID, lineID, funcID, join_ids

def decide_to_trace_call(frame):
    """ decides if call is needed to be traced """
    if frame.f_code.co_name in ["<lambda>", "<genexpr>", "<dictcomp>", "<setcomp>", "<listcomp>"]:  # FIXME: seems, sometimes wrong def is taken for listcomp or genexp -- if it is used inside of them, example: listcomp_ = [ x for x in generator_()  ] 
        return False

    module = moduleID(frame)
    if module and module.startswith('test_mytracer'):
       return True 
    

# def exprs_are_equal(a, b):
    # return a==b

def inject_watch_pragma(line, frame):
    """ a way to define what to watch  in which line -- based on  regexps 
    uses function qualname and lineID to define line.
    
    and appends #WATCH[_AFTER] pragrma (before analysis/parsing of Watches takes place)"""
    
    
    inject = ""
    if frame.f_code.co_name == "A":
        # let's try to automatically detect assignments (in very primitive way, better would be to use AST)
        if '=' in line:
            parts = line.split('=')
            if len(parts) == 2:
                inject = " #INJECTED #WATCH_AFTER: " + parts[0]                
    return line + inject




import mytracer # Monkey patch hooks

mytracer.decide_to_trace_call = decide_to_trace_call
mytracer.inject_watch_pragma = inject_watch_pragma
# mytracer.other_cases = other_cases

import test_mytracer_simple

def test_simple():    test_mytracer_simple.B()   # wrap

mytracer.do_trace( test_simple )

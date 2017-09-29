"""defines what code to trace 
and what expressions in which lines or watch"""
# import mytracer
from mytracer import moduleID, lineID, funcID, join_ids

def decide_to_trace_call(frame):
    """ decides if call is needed to be traced """
    if frame.f_code.co_name in ["<lambda>", "<genexpr>", "<dictcomp>", "<setcomp>", "<listcomp>"]:  # FIXME: seems, sometimes wrong def is taken for listcomp or genexp -- if it is used inside of them, example: listcomp_ = [ x for x in generator_()  ] 
        return False

    module = moduleID(frame)
    if module:
        for start in ["test_mytracer_", "csv2df"]: # we will trace all calls in these modules
            if  module.startswith( start ):
                return True 
    

# def exprs_are_equal(a, b):
    # return a==b

def inject_watch_pragma(line, frame):
    """ a way to define what to watch  in which line -- based on  regexps 
    uses function qualname and lineID to define line.
    
    and appends #WATCH[_AFTER] pragrma (before analysis/parsing of Watches takes place)"""
    
    inject = ""
    if funcID(frame) == "csv2df.reader-Reader.items":
    # if modID(frame) == "csv2df.reader"  and get_qualname(frame)=="Reader.items":
        if 'rowstack = RowStack(self.rows)' in line:
            inject  = " #INJECTED #WATCH_AFTER: rowstack.rows"
                
    return line + inject




import mytracer # Monkey patch hooks

mytracer.decide_to_trace_call = decide_to_trace_call
mytracer.inject_watch_pragma = inject_watch_pragma
# mytracer.other_cases = other_cases
# mytracer.BUFFER_STDOUT = False

import test_mytracer_kep

# mytracer.do_trace( test_mytracer_kep.test  )  
with mytracer.CallTracer():
     test_mytracer_kep.test()

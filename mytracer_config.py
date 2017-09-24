"""defines what code to trace 
and what expressions in which lines or watch"""
# import mytracer
from mytracer import moduleID, lineID, funcID, join_ids

def decide_to_trace_call(frame):
    """ decides if call is needed to be traced """
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

def other_cases( frame, event, arg ):
    # print( "#DBG ignoring", event, lineID(frame) )
    pass

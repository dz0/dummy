#@inline 1: __main__. B 
def B():
   print("start B")  # line: 283, {}   #module __main__
start B
   x = 42    # line: 284, {}   #module __main__
   u = (A(  # line: 285, {'x': 42}   #module __main__
     3,  # line: 287, {'x': 42}   #module __main__
      2,  # line: 288, {'x': 42}   #module __main__
          1   # line: 289, {'x': 42}   #module __main__
          #@inline 2: __main__. A 
          def A(*args):
               a = 5  # line: 275, {'args': (3, 2, 1)}   #module __main__
               print(  # line: 276, {'args': (3, 2, 1), 'a': 5}   #module __main__
                 "A"  # line: 277, {'args': (3, 2, 1), 'a': 5}   #module __main__
A
               return a*C()  # line: 279, {'args': (3, 2, 1), 'a': 5}   #module __main__
               #@inline 3: __main__. C 
               def C():
                   print("C")  # line: 296, {}   #module __main__
C
                   return 2  # line: 297, {}   #module __main__
               #@return: C => 2
          #@return: A => 10
   c = C()  # line: 292, {'x': 42, 'u': 10}   #module __main__
C
   print("end B")  # line: 293, {'x': 42, 'u': 10, 'c': 2}   #module __main__
end B
#@return: B => None

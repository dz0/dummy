
#@inline 1: __main__. B 
def B():
           print("start B")
start B
           x = 42  
           u = (A(
             x=C() ,
           #@inline 2: __main__. C 
           def C():
                    print("C")
C
                    return 2
           #@return: C => 2
             y=3,
              z=2
           #@inline 2: __main__. A 
           def A(*args, **kwargs):
                a = 5
                print(
                  "A"
A
                if a > 10:
                    print("a <= 10")
a <= 10
                c = C()
C
                return a
           #@return: A => 5
           print("end B")
end B
#@return: B => None

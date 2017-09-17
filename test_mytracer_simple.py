if True:
   def A(*args, **kwargs): 
        a = 5
        print(
          "A"
          )
        if a > 10:  #WATCH: a
            print("a > 10")
        else:
            print("a <= 10")
        
        c = C() 
        pass #WATCH: c
        for x in range(3):
            C()
        return a
    

def B(): 
         print("start B")
         x = 42  
         x = x #WATCH: x; x-10
         u = (A(
           x=C() ,
           y=3,
            z=2
              
         )
         )
        
         print("end B")

def C():
         print("C")
         def generator_():
             listcomp_ = [x for x in [5, 6, 7]]
             for a in listcomp_:
                yield a #WATCH: a; a*2

         genexpr_ = [x for x in generator_()]
         lambda_ = lambda x: x*x
         
         mapped = map(lambda_, genexpr_)
         return 2

class fun:
    a=2
    def __init__(self):
         self.x=3
         self.y=4
         
    def display(self):
        print(self.x,self.y)

    def __del__(self):
        print("object is deleted ")

    def __cmp__(self,other):
        if(self.x==other.x):
            print("comparable")
         
    def __str__(self):
          return(str(f1.x))

    def __repr__(self):
       return("string is returned")

    def compare(self,other):
        if(self.x==other.x):
            print("true")

    def __neg__(self,other):
        print(self.x-other.x)

f1=fun()
f2=fun()
f1.display()
print(f1.x)
print(f1.__class__.a)
print(f1.a)        
f1.age=4
print(f1)
print(f1.age)
#del f1.x
#f1.display()
#del f1
#f1.__class__.__del__()
#cmp(f2,3)
f1.__class__.__cmp__(f2,f1)
print(str(f1))
print(repr(f1))
f1.compare(f1)
f1.__cmp__(f2)
f1.__neg__(f2)

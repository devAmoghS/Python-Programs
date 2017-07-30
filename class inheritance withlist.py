class polygon:
    def __init__(self,no_of_sides,*sides):
        self.no_of_sides=no_of_sides
        self.sides=[0]
    def input_sides(self):
        for i in range (self.no_of_sides):
           s=int(input("enter the value for side[%d]"%i))
           self.sides.append(s)
    def print_sides(self):
           print("the sides entered are:",self.sides[1:])

class Triangle(polygon):
    def __init__(self):
        polygon.__init__(self,3)
    def findArea(self):
        area=0
        for i in range(self.no_of_sides):
            area+=self.sides[i]
        area/=2
        print("the area of the triangle is:",area)

        
t=Triangle()
t.input_sides()
t.print_sides()
t.findArea()

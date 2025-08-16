class shape:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def area(self):
        return self.x*self.y
rec=shape(5,3)
print(rec.area())


class circle(shape):
    def __init__(self,r):
        self.r=r
    
    def area(self):
        return 3.14*self.r*self.r

cir=circle(3)
print(cir.area())
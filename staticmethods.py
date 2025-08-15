class Math:
    def __init__(self,num):
        self.num=num
    def addTonum(self,n):
        self.num=self.num+n
    @staticmethod
    def add(a,b):
        return a+b
    def mul(a,b):
        return a*b
result=Math.add(2,3)
print(result)
a=Math(5)
print(a.add(2,3))
print(Math.add(3,4))
a.addTonum(4)
print(a.num)
print(Math.mul(2,4))



class Emp:
    compName="apple"
    def __init__(self,name):
        self.name=name
    def showDetails(self):
        print(f"{self.name} belongs to the {self.compName}")
e1=Emp("harry")
e2=Emp("lorry")
e1.showDetails()
e2.showDetails()
e1.compName="nestle"
e1.showDetails()
e2.showDetails()

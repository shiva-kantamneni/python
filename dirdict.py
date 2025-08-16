x=[1,2,3]
print(dir(x)) #useful to know about the object
print(x.__add__)

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
p=Employee('harry',30)
print(p.__dict__) #dictionary representation of an object attributes

print(help(p)) #description of attributes and methods


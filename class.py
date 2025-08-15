class details:
    name="Rohan"
    age=20  
    def info(self):
        print(f"{self.name} age is {self.age}")

a=details()
a.info()

class person:
    def __init__(self,n,o):
        print("Hey i am the person")
        self.name=n
        self.occ=o
    def info(self):
        print(f"{self.name} occupation is {self.occ}")
a=person("harry","software")
b=person("lorry","hardware")
a.info()
b.info()


def greet(fx):
    def greet(*args,**kwargs):
        print("Hello world")
        fx(*args,**kwargs)
        print("tanku")
    return greet

@greet
def add(a,b):
    print( a+b)
add(1,2)

#getters
class student:
    def __init__(self,value):
        self._value=value
    def show(self):
        print(self._value)
    
s1=student(10)
print(s1._value)
s1._value=12
print(s1._value)

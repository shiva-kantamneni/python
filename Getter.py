class myClass:
    def __init__(self,value):
        self._value=value
    def show(self):
        print(f"{self._value}")
   
    @property
    def value(self):
        return self._value
obj=myClass(10)
obj.show()
print(obj.value)




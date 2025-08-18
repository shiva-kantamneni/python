class Emp:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(f"the name is {self.name}")
class Dancer:
    def __init__(self,dance):
        self.dance=dance
    def show(self):
        print(f"the dance is {self.dance}")
class DancerEmp(Emp,Dancer):
    def __init__(self, name,dance):
        self.name=name
        self.dance=dance
o=DancerEmp("harry","Khatak")
print(o.name)
print(o.dance)
o.show() #first check in dancerEmp then emp and then dancer

        


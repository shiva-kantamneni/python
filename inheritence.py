class emp:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def showDetails(self):
        print(f"name of emp is {self.name} and id is {self.id}")

class programmer(emp):
    def showLang(self):
        print("default is python")
    

e=emp("rohna",34)

e.showDetails()

e1=programmer("harry",25)
e1.showDetails()
e1.showLang()

        
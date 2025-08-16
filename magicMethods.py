class emp:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def __len__(self):
        return len(self.name)
    def __str__(self):
        return f"name of the emp is {self.name} and id is {self.id}"
e=emp("hary",2)
print(len(e))
print(e)
class examp:
    def __init__(self):
        self.val=10
        self.__name="harry"
        self._age=20
e=examp()
print(e.val)
print(e._examp__name) #can be accessed indirectly which is called name mangling
print(e._age)


class exam(examp):
    pass
class otherclass:
    pass

e1=exam()
print(e1._age)

    



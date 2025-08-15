class Library:
    def __init__(self):
        self.noofBooks=0
        self.books=[]
    def addBook(self,book):
        self.books.append(book)
        self.noofBooks=len(self.books)
    def showInfo(self):
        print(f"The library has {self.noofBooks} books")


l=Library()
l.addBook("harry")
l.addBook("lorry")
l.showInfo()
    

def welcome():
    print("You are welcome from harry")

if __name__=="__main__":
    welcome()

x=10

def fun():
    global x
    print(x)
fun()

import time
def usingFor():
    for i in range(10):
        print(i)
def usingWhile():
    for i in range(10):
        print(i)

t1=time.time()
usingFor()
print(time.time()-t1)

t2=time.time()
usingWhile()
print(time.time()-t2)

time.sleep(5)
print("i am printed after 5 seconds")

t=time.localtime()
formatted=time.strftime("%Y-%m-%d %H:%M:%S",t)
print(formatted)
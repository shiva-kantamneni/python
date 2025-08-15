def cube(x):
    return x*x*x

print(cube(2))

l=[1,2,3,4,5]

lis=[]
for i in l:
    lis.append(cube(i))
print(lis)

res=list(map(cube,l))
print(res)


def fil(x):
    if(x%2==0):
        return True
    else:
        return False
res=list(filter(fil,l))
print(res)
from functools import reduce
res=reduce(lambda x,y:x+y,l)
print(res)


print("s"=="s")
print("s" is "s")

name="harry brrok"
name1="harry brrok"
print(name==name1)
print(name is name1)

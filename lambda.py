# def doub(x):
#     return x*2

def apply(fx,val):
    return val+fx(val)

doub=lambda x:x*2
avg=lambda x,y:(x+y)/2

print(doub(3))
print(avg(3,3))
print(apply(lambda x:x*2,2))





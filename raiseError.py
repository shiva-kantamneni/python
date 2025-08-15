a=int(input("Enter any value between 1 to 9"))
if(a<1 or a>9):
    raise ValueError("value should be in between 1 to 9")

class InvalidAgeError(Exception):
    def __init__(self,age):
        super().__init__(f"Invalid age:{age}.Age must be >=18")

age=int(input())
try:
    if(age<18):
        raise InvalidAgeError(age)
    print("Access granted")
except InvalidAgeError as e:
    print("custom error caught:",e)
import random
import string
def gen_rand(length):
    charecters=string.ascii_lowercase
    return ''.join(random.choice(charecters) for i in range(length))

a=input("Enter string: ")

b=len(a)
if(b>=3):
    rand=gen_rand(3)
    a=rand+a[1:b]+a[0]+rand
else:
    a=a[::-1]
print(f"coded string is {a}")




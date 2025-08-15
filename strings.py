# strings are immutable

names="harry,shubham"

print(names[0:5])
print(len(names))
print(names[0:-3])

for i in names:
    print(i)

print(names.lower())
print(names.upper())
print(names.replace("har","mar"))
print(names.split(" "))
print(names.capitalize())
print(names.find("shu"))
print(names.endswith("am"))
print(names.isalnum())
print(names.isalpha())
print(names.isnumeric())

a=18
if(a>18):
    print("You can drive car now")
elif(a==18):
    print("1 year to go")
else:
    print("No you can't")

import time
timest=time.strftime('%H:%M:%S')
h=int(time.strftime('%H'))
if(h<12):
    print("Good morning sir")
elif(h<17):
    print("Good afternoon sir")
else:
    print("Good evening sir")

print(timest)



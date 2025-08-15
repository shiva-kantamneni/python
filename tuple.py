tup=(1,2,3,4,5,6)
#to make changes to the tuple first we have to convert it into the list
l_tup=list(tup)
l_tup.append(7)
l_tup.reverse()
l_tup[3]=19
tup=tuple(l_tup)
print(tup)


#string formatting
letter="Hey my name is {} and i am from {}"
name="ramu"
country="india"
print(letter.format(name,country))
print(f"my name is {name} and i am from {country}")

#docstrings
def square(n):
    '''this function takes in number n and return the square
    of the n
    '''
    return n*n
square(5)
print(square.__doc__)
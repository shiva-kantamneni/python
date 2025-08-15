# f=open('file.txt','a')

# f.write("this is python boys")  #appending 


#f=open("file.txt",'w')

# f.write("this is python boys") #writing

# with statement automatically closes the file after the  operations

f=open('file.txt','r')

while True:
    line=f.readline()
    if not line:
        break
    print(line)



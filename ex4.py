import re
file_name=input("enter the file name")


try:
    f=open("ex4.txt","r")
    
except(IOError):
    print("file doesnot exsist")

for line in f.readlines():
    a=re.findall('#(.*)#',line)
    
    if( a != []):
         print(a)
    else:
        f1=open(file_name,"a")
        f1.writelines(line)

f1.close()
f.close()
    


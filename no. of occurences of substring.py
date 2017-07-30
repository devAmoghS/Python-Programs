"""
s="preeni"
ss="e"
"""
s=input("enter the string:")
ss=input("enter the substring:")

j=0

for i in range(len(s)):
    m=s.find(ss)
    #the first occurence of ss
    if(j==0):
        print("m=%d"%m)
    if(m== -1 and j==0):
        print("no such substring is available")
        break
    if(m== -1):
        break
    else :
        j=j+1
        s=s[m+1:]
       # print(s)
print("no. of occurences is %s"%j)


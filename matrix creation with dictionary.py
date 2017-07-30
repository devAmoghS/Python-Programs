final=[]
r= int(input("enter the no. of rows:"))
c=int(input("enter the no. of columns:"))
      
for i in range (r):
    l=[]
    for j in range(c):
        e=int(input("enter the value for [%d ][ %d]:"% (i+1,j+1)))
        l.append(e)
    final.append(l)
    
for i in range(r):
    s=str(final[i])
    print(s+" ")

print(final)
        

d={}
for i in range(r):
    for j in range (c):
        elem=final[i][j]
        if (elem !=0):
            t=(i,j)
            d[t]=elem
print(d)



i=0
l=[]
element=input('Enter the elements enter end to stop: ')
while(element != 'end'):
	l.append(int(element))
	i=i+1
	element=input('Enter the elements enter end to stop: ')

print('Your input')
for item in l:
	print(item)

d=l

for k in range(0,len(l)):
	for j in range(k,len(l)):
		if(l[k]>=l[j]):
			l[k],l[j]=l[j],l[k]
print("Elements after sorting by bubble sort:")
for item in l :
	print(item) 


for i in range(0,len(d)):
	for j in range(i,0,-1):
		if(d[j] <= d[j-1]):
			d[j],d[j-1]=d[j-1],d[j]

print("Elements after sorting by insertion sort:")
for item in d:
	print(item)

			
			

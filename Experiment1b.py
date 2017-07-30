def sort_tuple(l):
	#sorts the list based on the last element of each tuple in the list
	for i in range(0,len(l)):	
		for j in range(i,len(l)):
			ti=l[i]
			tj=l[j]
			if(ti[len(ti)-1] >= tj[len(tj)-1]):
				l[i],l[j]=l[j],l[i]
	return l


l=[]
t=()
element=input('Enter the element STOP to stop the set and END to stop the list:')
while(element != 'END'):
	while(element != 'STOP'):	
		t+=(int(element),)
		element=input('Enter the element STOP to stop the set and END to stop the list:')
	l.append(t)
	t=()
	element=input('Enter the element STOP to stop the set and END to stop the list:')

l=sort_tuple(l)
print(l)



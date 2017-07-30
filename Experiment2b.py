s=input('Enter the string:')
ss=input('Enter the substring:')
l=[]
offset=0
while(s.find(ss)!=-1):
	offset=offset+s.find(ss)
	l.append(offset)
	s=s[s.find(ss)+1:]
	offset+=1
print(l)

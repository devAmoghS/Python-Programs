people=['One','Two','Three']
personOne={'Two':5,'Three':1}
personTwo={'One':3,'Three':4}
personThree={'One':3,'Two':2}
persons=[personOne,personTwo,personThree]
l=[0,0,0]
index=0
for i in people:
	for k in persons:
		for j in k.keys():
			if(i==j):
				l[index]+=k[i]
		
	index=index+1
print(l)
popularity=max(l)
mostPopular=l.index(popularity)
print(people[mostPopular],' is the most popular friend') 


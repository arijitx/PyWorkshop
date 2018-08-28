r=int(input())
l=[]
for i in range(r):
	x=input()
	if(i==0):
		l.append(x.split(' ')[2])
	else:
		if(len(x.split(' '))==3):
			#insert operation
			pos=int(float((x.split(' ')[1])))
			#print("pis is ",pos)
			l1=l[:pos]
			l2=l[pos:]
			l1.append(x.split(' ')[2])
			l=[]
			l=l1+l2
			#print(l)
		else:
		    # remove
		    pos=int(float((x.split(' ')[1])))
		    l1=l[:pos+1]
		    l2=l[pos+1:]
		    #print("l1 ",l1)
		    #print("l2 ",l2)
		    l1.pop()
		    l=[]
		    l=l1+l2
		    #print(l)
print(l)
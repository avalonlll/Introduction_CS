x=raw_input("please give a string: ")
list1 =x.split() #put x elements to list1
y= len(list1) 
emptylist=[] #create an empty list
for i in range (y):
	newlist=list1[i] #
	print newlist
	if ( newlist.isalpha() ):
		newlist=newlist[1:]+newlist[0]+'argh'
		emptylist.append(newlist)
	if ( newlist.isalpha() == False & len(newlist)!= 1 ):
		if (newlist.isdigit() for i in newlist):
			emptylist.append(newlist)
		else:
			length=len(newlist)-1
			lastdigit=newlist[length]
			newlist=newlist[0:length]
			newlist=newlist[1:]+newlist[0]+'argh'
			emptylist.append(newlist)
			emptylist.append(lastdigit)
		
	print newlist
	
	
print emptylist

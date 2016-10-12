x=raw_input("please give a string: ")
list1 =x.split() #put x elements to list1
y= len(list1) 
emptylist=[] #create an empty list
for i in range (y):
	newlist=list1[i] #newlist takes list's i element
	if ( newlist.isalpha() ): #if new list has only alpharithmetics, make the change
		newlist=newlist[1:]+newlist[0]+'argh' 
		emptylist.append(newlist)#add newlist's element to emptylist
	if ( newlist.isalpha() == False & len(newlist)!= 1 ): #if newlist isn't alpharithmetics and it's not only 1 character, append newlist's element to emptylist
		if (newlist.isdigit() for i in newlist): #if newlist has one/more digits, append newlist's element to emptylist
			emptylist.append(newlist)
		else:
			length=len(newlist)-1  
			lastdigit=newlist[length]
			newlist=newlist[0:length]
			newlist=newlist[1:]+newlist[0]+'argh'
			emptylist.append(newlist)
			emptylist.append(lastdigit)
	
	
print emptylist

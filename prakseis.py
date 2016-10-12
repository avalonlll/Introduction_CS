def prakseis (x):
	i=0 #counter equal to 0
	s = x % 10 #takes x's last digit
	flag=True 
	while (flag == True):
		if (x < 10 ):
			break
		x = x/10 #deletes x last digit
		s*= x%10 
		if (x < 10): 
			if (s < 10) : 
				i+=1
				flag = False
				break
			else:
				x=s
				s = s % 10
				i +=1
	return i

def prob_1(n):
	return n%2==0

def prob_2(n):
	b= (n-32)/1.8
	return b

def prob_3(n1, n2):
	n= n1
	for i in range (1,n2):
		n1 = n1*n
	return n1

def prob_4(caracter, lon):
	h= len caracter
	lon= lon-h
	lon=lon/2
	return "*"*lon, caracter, "*"*lon
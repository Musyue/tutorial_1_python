#!/usr/bin/python3
def fibonnacci():
	num= int(input('Please enter how many Fibonacci numbers you want to generate:'))
	fib=[]
	i=0
	a=b=1
	if num==1:
		fib=[1,]
	else:
		while i<num:
			fib.append(b)
			a,b=b,a+b
			i+=1
	return fib
print (fibonnacci())

# F(1)=1，F(2)=1, F(n)=F(n-1)+F(n-2)（n>=2，n∈N*）
#The Rule is xn = xn−1 + xn−2
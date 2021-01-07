def multiple(a,b):
	a=a+b
	b=a*b
	c=a/b
	return a,b,c
x=multiple(10,20)#if you have multiple return value and you have onlu put one value in actual argument then you have only tuple type data type
print(x)
x,y,z=multiple(10,20)
print(x)
print(y)
print(z)


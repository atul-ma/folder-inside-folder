import os
def makefolder():
	a=0
	for i in range(0,500000):
		b=str(a)
		os.mkdir(b)
		a=a+1
		print(a)
makefolder()

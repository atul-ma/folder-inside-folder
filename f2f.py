import os
a=1
for i in range(0,5):
	b=str(a)
	os.mkdir(b)
	os.chdir(b)
	
	if a==5:
		f=open("cong.atul","w")
		f.write("Congrats ! You are doing something new.")
	a=a+1

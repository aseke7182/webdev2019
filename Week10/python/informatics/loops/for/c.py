import math

a = int(input())
b = int(input())
for numb in range(a,b+1):
	if math.sqrt(numb)==int(math.sqrt(numb)):
		print(numb,end = " ")
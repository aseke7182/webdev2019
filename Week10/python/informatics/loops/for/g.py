import math

a = int(input())
for num in range(2,a+1):
	if a%num==0:
		print(num)
		break
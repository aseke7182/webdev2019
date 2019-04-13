import math
 
n = int(input())
c = input()
arr = c.split(" ")
for i in arr:
	if int(i)%2==0:
		print(i, end = " ")
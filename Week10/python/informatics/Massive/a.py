import math
 
n = int(input())
c = input()
arr = c.split(" ")
for i in range(len(arr)):
	if i%2==0:
		print(arr[i], end = " ")
import math

def pow(a,n):
	ans = float(a)
	for i in range(1,n):
		ans*=float(a)
	return float(ans)

arr = input().split(" ")
a = float(arr[0])
n = int(arr[1])
if n==0:
	print(1)
else:
	print(pow(a,n))
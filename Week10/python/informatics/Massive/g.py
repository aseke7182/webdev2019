import math

cnt = 0
n = int(input())
arr = input().split(" ")
for i in range(0,int(n/2)):
	arr[i], arr[n-i-1] = arr[n-1-i] , arr[i]
for i in arr:
	print(i, end = " ")
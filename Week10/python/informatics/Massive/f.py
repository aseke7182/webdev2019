import math

cnt = 0
n = int(input())
arr = input().split(" ")
for i in range(1,n-1):
	if int(arr[i])>int(arr[i-1]) and int(arr[i])>int(arr[i+1]):
		cnt+=1
print(cnt)
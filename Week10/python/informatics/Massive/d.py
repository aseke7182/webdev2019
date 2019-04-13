import math

cnt = 0
n = int(input())
c = input()
arr = c.split(" ")
for i in range(1,n):
	if int(arr[i]) > int(arr[i-1]):
		cnt+=1
print(cnt)
import math

ok = False
n = int(input())
arr = input().split(" ")
for i in range(1,n):
	if int(arr[i])>0 and int(arr[i-1])>0 or int(arr[i])<0 and int(arr[i-1])<0:
		ok = True
if ok:
	print("YES")
else:
	print("NO")
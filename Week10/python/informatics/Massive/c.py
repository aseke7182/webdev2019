import math

cnt = 0
n = int(input())
c = input()
arr = c.split(" ")
for i in arr:
	if int(i)>0:
		cnt+=1;
print(cnt)
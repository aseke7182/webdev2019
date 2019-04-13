import math

a = int(input())
i = 1
cnt = 0
if a == 1:
	print(0)
	a = 0
while i <= a:
	i*=2
	cnt+=1
	if i >= a:
		print(cnt)
		break
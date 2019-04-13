import math

a = int(input())
i = 1
ok = False
while i <= a:
	if i==a:
		print("YES")
		ok = True
	i*=2
if ok==False:
	print("NO")

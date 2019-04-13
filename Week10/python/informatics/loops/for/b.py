import math

a = int(input())
b = int(input())
c = int(input())
d = int(input())
for numb in range(a,b+1):
	if numb%d==c:
		print(numb, end = " ");
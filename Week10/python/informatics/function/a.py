import math

def mini(a,b):
	if a<b:
		return a
	return b

def min(a,b,c,d):
	return mini(mini(a,b),mini(c,d))

arr = input().split(" ");
a = int(arr[0])
b = int(arr[1])
c = int(arr[2])
d = int(arr[3])

print(min(a,b,c,d))
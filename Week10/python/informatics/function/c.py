import math

def xor(a,b):
	if a==b:
		return 0
	return 1

arr = input().split(" ")
a = int(arr[0])
b = int(arr[1])
print(xor(a,b))
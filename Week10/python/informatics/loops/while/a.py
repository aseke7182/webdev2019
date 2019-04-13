import math

a = int(input())
i = 0
while i < a:
	i+=1
	if math.sqrt(i) == int(math.sqrt(i)):
		print(i)
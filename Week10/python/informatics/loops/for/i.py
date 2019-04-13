import math

a = int(input())
cnt = (0)
for num in range(1,int(math.sqrt(a+1))):
	if a % num==0:
		cnt+=2
if a % math.sqrt(a)==0:
	cnt+=1
print(cnt)
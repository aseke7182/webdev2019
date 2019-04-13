import math

a = int(input())
b = int(input())
distance = int(a*b)
answer = int(distance%109 + 109 %109)
print(str(answer))
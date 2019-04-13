#!/bin/python3

N = int(input())
ok = True
if N%2==1:
    ok = False
else:
    if N>=6 and N<=20:
        ok = False
if ok == False:
    print("Weird")
else:
    print("Not Weird")

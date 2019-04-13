def fix_teen(n):
  if n>12 and n<15 or n>16 and n<20:
    n=0
  return n

def no_teen_sum(a, b, c):
  a = fix_teen(a)
  b = fix_teen(b)
  c = fix_teen(c)
  cnt = a+b+c
  return cnt

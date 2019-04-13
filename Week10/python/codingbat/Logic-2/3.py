def go(n):
  if n%10>=5:
    n+=10-n%10
  else:
    n-=n%10
  return n
def round_sum(a, b, c):
  a = go(a)
  b = go(b)
  c = go(c)
  return a+b+c

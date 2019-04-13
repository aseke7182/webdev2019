def lucky_sum(a, b, c):
  cnt = 0
  if a==13:
    cnt = 0
  elif b==13:
    cnt = a
  elif c==13:
    cnt = a+b
  else:
    cnt = a+b+c
  return cnt

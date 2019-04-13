def lone_sum(a, b, c):
  cnt = 0
  if(a==b):
    if b!=c:
      cnt+=c
  elif a==c:
    if b!=c:
      cnt+=b
  elif b==c:
    if a!=c:
      cnt+=a
  else:
    cnt+=a+b+c
  return cnt
def count_hi(str):
  pat = "hi"
  cnt = 0
  ind = 0
  while pat in str[ind:]:
    ind = str.find(pat,ind)+1
    cnt+=1
  return cnt
  

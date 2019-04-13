def string_match(a, b):
  cnt = 0;
  for i in range(min(len(a),len(b))-1):
    if(a[i]==b[i]):
      if(a[i+1]==b[i+1]):
        cnt+=1
  return cnt
      

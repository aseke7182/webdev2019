def count_code(str):
  cnt = 0
  for i in range(len(str)-3):
    if( str[i]=='c'):
      if( str[i+1]=='o'):
        if( str[i+3]=='e'):
          cnt+=1
  return cnt

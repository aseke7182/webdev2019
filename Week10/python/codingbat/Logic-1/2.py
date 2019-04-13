def in1to10(n, outside_mode):
  if(outside_mode):
    if(n>9 or n<2):
      return True
    return False
  else:
    if(n>0 and n<11):
      return True
    return False

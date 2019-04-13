def close_far(a, b, c):
  if (abs(a-c)<2 and abs(a-b)>1 and abs(b-c)>1) or (abs(b-c)>1 and abs(a-b)<2 and abs(a-c)>1):
    return True
  return False

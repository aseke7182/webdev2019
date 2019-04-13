def caught_speeding(speed, is_birthday):
  m = 0;
  if(is_birthday):
    m = 5
  if(speed >= 81 + m):
    return 2
  elif (speed >= 61+m):
    return 1
  return 0

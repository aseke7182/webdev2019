def squirrel_play(temp, is_summer):
  m = 90
  if is_summer:
    m = 100
  if(temp>=60 and temp<=m):
    return True
  return False
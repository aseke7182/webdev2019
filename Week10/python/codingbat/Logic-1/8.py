def date_fashion(you, date):
  if(you>7 and date>2 or date>7 and you>2 ):
    return 2
  elif (you<3 or date<3):
    return 0
  return 1

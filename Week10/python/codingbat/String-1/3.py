def combo_string(a, b):
  if (len(a)>len(b)):
    short = b
    longg = a
  else:
    short = a
    longg = b
  return short + longg + short

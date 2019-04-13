def end_other(a, b):
  a = a.lower()
  b = b.lower()
  x = min(len(a),len(b))
  if(a[-x:]==b or b[-x:]==a):
    return True
  return False

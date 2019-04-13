def change(input_str):
  return input_str[-1] + input_str[1:-1] + input_str[0]

def front_back(str): 
  if len(str) <= 1:
    return str
  s = change(str)
  return s
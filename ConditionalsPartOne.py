def plus(a, b):
  if type(b) is str:
    return None  
  else:
    return a + b

plus(12, "10")

def plus(a, b):
  if type(b) is int or type(b) is float:
    return a + b  
  else:
    return None

print(plus(12, 1.2))

#chaining the conditions

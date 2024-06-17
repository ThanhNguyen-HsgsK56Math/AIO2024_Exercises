import math

def is_number(n):
  try:
    float(n)
    return True

  except ValueError:
    return False

def sigmoid(n):
  sigmoid = 1 / (1 + math.exp(-n))
  return sigmoid 

def reLu_function(n):
  return max(0, n)

def ELU_function(n, alpha):
  if n <= 0:
    elu_func = alpha * (math.exp(n)-1)
    return elu_func 
  else:
    return n
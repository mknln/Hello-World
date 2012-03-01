
def f(x, y):
  if x == 0:
    return 1
  else:
    return y * x * f(x - 1, y)

  return 0

print f(5, 2)

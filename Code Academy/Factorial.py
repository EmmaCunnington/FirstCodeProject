def factorial(x):
  f = 1
  while x > 1:
    f = f *x
    x = x-1
  return f
print(factorial(4))

def digit_sum(x):
  string_x = str(x)
  total = 0
  for i in string_x:
    total += int(i)
  return total

print(digit_sum(1234))
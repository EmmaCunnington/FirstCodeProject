n = ["Michael", "Lieberman"]
# Add your function here
def join_strings(words):
  result = ''
  for word in words:
    result = result + str(word)
  return result

print(join_strings(n))
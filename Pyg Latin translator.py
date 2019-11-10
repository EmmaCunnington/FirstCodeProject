print('Welcome to the Pyg Latin Translator!')

while (1):
  pyg = 'ay'
  original = input('Enter the word you wish to translate: ')

  if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    new_word = word[1:len(original)] + first + pyg
    print(('%s in Pyg Latin is %s!') % (original, new_word))
  else:
    print("Please make sure you've entered a word with no numbers, symbols or spaces!")

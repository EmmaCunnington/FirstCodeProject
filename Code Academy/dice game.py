"""This program is a dice game! It will:
  - roll 2 dice
  - add the values
  - ask the user to guess a number
  - compare guess to sum
  - determine winner!"""

from random import randint
from time import sleep

def get_user_guess():
  guess  = int(input('Guess the sum of the dice: '))
  return guess

def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_val = number_of_sides * 2
  print ("The maximum roll is %d" % (max_val))
  guess = get_user_guess()
  if guess > max_val:
    print ('That guess is too big!')
    roll_dice(6)
  else:
    print ('Rolling...')
    sleep(1)
    print (str(first_roll))
    sleep(1)
    print (str(second_roll))
    sleep(1)
    total_roll = first_roll + second_roll
    print (str(total_roll))
    print ('Result...')
    sleep(1)
    if guess == total_roll:
      print ("Congratulations! You won!")
    elif abs(guess - total_roll) == 1:
      print('So close!')
      roll_dice(6)
    else:
      print ("Bad luck! Maybe next time.")
      roll_dice(6)
      
roll_dice(6)
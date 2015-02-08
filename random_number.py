import random

def show_help():
  print("Random number guessing game: You get 5 chances to guess a random number selected by the computer.  It will be a whole number from 1 to 10 inclusive. If you guess wrongly, you will be told whether the random number is higher or lower than your guess.  The game will let you know how many guesses you've made. ")
  
def generate_random_no():
  random_number = random.randint(1,10)
  return random_number

def check_guess(guess, random_number):
  if (guess == random_number):
    print("Well done! You guessed correctly!")
    exit()
  elif (guess < random_number):
    print("Bad luck! Your guess is too low!")
  elif (guess > random_number):
    print("Bad luck! Your guess is too high!")
  
total_no_of_chances = 5
chances_left = 5

show_help()
random_number = generate_random_no()

while (chances_left > 0):
  try:
    guess = int(input("Enter your guess: "))
  except:
    print("Sorry, you need to enter a whole number")
    break
  if (guess < 1 or guess > 10):
    print("Sorry, you need to enter a whole number between 1 and 10 inclusive.")
    break
  check_guess(guess, random_number)
  chances_left = chances_left - 1
  print("You have made {} guesses so far!".format(total_no_of_chances-chances_left))
  if (chances_left == 0):
    print("Sorry, you've run out of guesses. The correct answer was {}".format(random_number))
  
  
  
  

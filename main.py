#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
from art import logo

print(logo)
print("welcome to the guessing game!")
print("i'm thinking of a number between 1-100, and you should try to guess the number.")
attempt = 0

def lavel_game():
  lavel = input("choose a difficulty. type 'easy' for getting 10 attempt to guess, or 'hard' for 5 attempt to guess.\n")
  global attempt
  
  if lavel == "hard":
    attempt = 5
  elif lavel == "easy":
    attempt = 10
  else:
    print("you can only type 'hard' or 'easy', please type again.\n")
    lavel_game()
  
def valid_choose(user_choose):
  if user_choose < 101 and user_choose > 0:
    return True
  return False

def guess_check(guess):
  user_choose = int(input("make a guess: "))
  if not valid_choose(user_choose):
    print("you choose invalid guess, your guess should be between 1-100.\nplease guess again.")
    guess_check(guess)
  else:
    if user_choose < guess:
      print(f"{user_choose} is too low!")
      return False
    elif user_choose > guess:
      print(f"{user_choose} is too high!")
      return False
    else:
      print(f"you got it! the answer was {user_choose}.")
      print("guess again!")
      return True
    



guess = random.randint(1,100)
lavel_game()

guess_corect = False

while not guess_corect and attempt:
  print(f"you have {attempt} attempts remaining to guess the number")
  guess_corect = guess_check(guess)
  attempt -= 1
if not guess_corect:
  print("your attempts to try is over but nice try, you can try guess again!")
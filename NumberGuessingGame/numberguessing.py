"""
NUMBER GUESSING GAME

Step1: Create a dictionary of different levels as keys and under each level make another dictionary of max_limit and attempts
Step2: Create level_choosing function
     --> Based on level: Get the max and attempts
     --> Use randint to get get a number betweeen 1 and max
     --> return number, max, attempts
Step3: Create the game function. Make chance as 0: For every iteration that does not match, increment chance by 1
     --> Use while loop to get input until match is found or attempts exhaust
     --> Check if input guess is between 1 and max: else skip
     --> Check if guess < num: print low  | Check if guess > num: print high
     --> If guess == num: Match (break the loop)
     --> when attempts == chance: attempts exhausted (break the loop) Reveal the number
    
"""

import random

difficulty = {
   "1": {
      "max": 50,
      "attempt": 12,
   }, 
   "2": {
      "max": 100,
      "attempt": 10,
   },
   "3": {
      "max": 200,
      "attempt": 8,
   }
}

def level():
   while True:
      level = input("1: Easy  2: Intermediate  3: Hard  Choose Level: ")
      if level in ["1","2","3"]:
         break
      else:
         print("Choose between 1-3")
   settings = difficulty[level]

   max = settings["max"]
   num = random.randint(1, max)
   
   attempts = settings["attempt"]

   return num, max, attempts

def game(num, max, attempts):
   chance = 0
   while True:
      guess = int(input(f"Enter a number between 1 and {max}:  "))
      if guess < -1 or guess > max:
         print(f"Please enter a number between 1 and {max}")
      
      elif guess*10 < num:
         print("Very Very Low! Think Big")
         chance +=1
      elif guess > num*10:
         print("Very Very High! Stay in Limits")
         chance +=1

      elif guess < num:
         print("Low! Try something greater")
         chance +=1
      elif guess > num:
         print("High! Try something lower")
         chance +=1

      else:
         print("Match")
         print(f"You have completed the game in {chance} attempts")
         break
     
      if attempts == chance:
         print("Out of Attempts")
         print(f"The number was {num}")
         break


num, max, attempts = level()
game(num, max, attempts)
      

"""
ODD EVEN'S GAME
Step1: Create function to choose odd even by the player and also by the computer using random module
    --> Starts with the player and then whoever wins the turn get to choose odd/even for the next turn
Step2: Create function to get the player_input of number and computer imput of number [1-6]
    --> return the total, player_input, computer_input
Step3: Create function to check who win the turn  --> total % 2== 0: Even  | total % 2 == 1: Odd
    --> Use condition to check who wins player or computer
    --> Increment the score who wins
    --> Return player_turn = False if computer wins
Step4: Ask the player for the max points, he want to play for
Step5: USe while loop to loop until the computer_points or player_points reach max
    --> Inititate the function one after another
Step6: After exiting loop check who has scored max_points ---> who scored wins the game
"""

import random

def choose_odd_even(player_turn):
   if not player_turn:
      computer_choose = random.choice(['odd', 'even'])
      player_choose = "even" if computer_choose == "odd" else "odd"
      return player_choose, computer_choose
   
   while True:
      player_choose = input("\nChoose ODD or EVEN: ").strip().lower()
      if player_choose in ['odd', 'even']:
         break
      print("Invalid Choice. Please choose either 'odd' or 'even'.")
   computer_choose = "even" if player_choose == "odd" else "odd"
   return player_choose, computer_choose
      

def hand_gesture():
   while True:
      player_gesture = int(input("\nEnter a number between [1-6]: "))
      if 1<= player_gesture <= 6:
         break
      print("Out of range. Enter between 1 to 6")   
   computer_gesture = random.randint(1,6)
   total = player_gesture + computer_gesture
   return player_gesture, computer_gesture, total

def who_win(player_choose, computer_choose, total, player_points, computer_points):
   if (total % 2 == 0 and player_choose == "even") or (total % 2 != 0 and player_choose == "odd"):
      player_points += 1
      player_turn = True
      print("Player +1")
   else:
      computer_points += 1
      player_turn = False
      print("Computer +1")
   return player_points, computer_points, player_turn

player_points = 0
computer_points = 0
print("\n------------- WELCOME TO ODD EVEN'S GAME -----------\n")
max_points = int(input("For how many points do you want to play: "))
player_turn = True

i = 0
while player_points < max_points and computer_points < max_points:
   print(f"\nRound: {i+1}")
   player_choose, computer_choose = choose_odd_even(player_turn)
   print(f"\nPlayer: {player_choose}")
   print(f"Computer: {computer_choose}")

   print("-------------------------------------")
   
   player_gesture, computer_gesture, total = hand_gesture()
   print(f"Player: {player_gesture}  |  Computer: {computer_gesture}")

   print("-------------------------------------")
   
   player_points, computer_points, player_turn = who_win(player_choose, computer_choose, total, player_points, computer_points)
   print(f"Current Score:\nPlayer: {player_points}  |  Computer: {computer_points}")

   print("-------------------------------------")
   print("-------------------------------------")
    
   i += 1


if computer_points == max_points:
   print("Computer wins the game!")
elif player_points == max_points:
   print("Player wins the game!")

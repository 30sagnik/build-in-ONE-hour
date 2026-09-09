"""
HAND CRICKET GAME
Step1: Create the toss function and use random module to get who wins the toss computer/player
Step2: Create the bat/bowl choose function. Take input of who has won the toss. Return the name who will bat
Step3: Create player_hand function. Use try catch and get the number [1-6] player want to play
Step4: Create the innings function. This will take input of batter, overs, wickets and target score(Set target as None by default)
     --> Set balls, score and wickets_lost to 0 at beginning
     --> Use a while loop to loop will balls are lesser than overs and wickets_lost are lesser than wickets
     --> get the player_hand from the player_hand function. Use randint to get computer_hand. Increment the ball by 1 after every turn
     --> if both hands are same, increment the wicket or else increment the score with the batter_hand_score.
     --> if the score > target, break the loop(This is for the second innings, in the first innings it is set as None)
     --> Return the score, balls, wickets
Step5: Create the main function. Take input of overs, wickets from user
     --> Initiate the toss function. Then the bat/bowl choose function to get the first_batter
     --> Then assign first_score and initiate the innings function with input of first_batter
     --> Set target variable as score + 1
     --> Assign second_batter using condition to the alternate team of first_batter
     --> Again initiate the innings function, this time with input as second_batter. Save this in second_score
Step6: Create a display function and according to the condition (player_score > computer_score ===> Player wins) print the result.

"""

import random

def toss():
   while True:
      toss_choose = input("Choose Head or Tail: ").strip().lower()
      if toss_choose in (['head', 'tail']):
         break
      print("Invalid Choice. Choose Head or Tail")
   toss = random.choice(['head', 'tail'])
   toss_win = "player" if toss == toss_choose else "computer"
   return toss_win


def choose_batting(toss_win):
   if toss_win == "computer":
      print("\nComputer wins the toss")
      computer_choose = random.choice(['batting', 'bowling'])
      if computer_choose == "batting":
         return "computer"
      return "player"
   print("\nPlayer wins the toss")
   while True:
      player_choose = input("Choose Batting or Bowling: ").strip().lower()
      if player_choose in (['batting', 'bowling']):
         break
      print("Invalid Choice. Choose Batting or Bowling")

   if player_choose == "batting":
      return "player"
   return "computer"


def get_player_hand():
   while True:
      try:
         get_hand = int(input("\nEnter a number between [1-6]: "))
         if get_hand in range(1,7):
            return get_hand
         print("Please enter a number between 1-6")
      except ValueError:
         print("Enter a valid number")


def play_innings(batter, overs, wickets, target = None):
   balls = 0
   wickets_lost = 0
   score = 0
   while balls < (overs * 6) and wickets_lost < wickets:
      player_hand = get_player_hand()
      computer_hand = random.randint(1,6)
      
      print(f"You: {player_hand}  |  Computer: {computer_hand}")

      balls += 1
      
      if player_hand == computer_hand:
         print("Wicket!")
         wickets_lost += 1
      else:
         if batter == "computer":
            score += computer_hand
         else:
            score += player_hand
      
      print(f"\nCurrent Score: {score} Runs   Wickets: {wickets_lost}   Over: {balls//6} Ball: {balls%6}")
      
      if target is not None and score > target:
         break
   
   return score, wickets_lost, balls

def display_result(player_score, computer_score):
   if player_score > computer_score:
      print("You win the Match!")
   elif player_score == computer_score:
      print("Draw Match")
   else:
      print("Computer wins the match")

def main():
   print("\n========== WELCOME TO HAND CRICKET GAME ===========\n")
   overs = int(input("Enter number of overs you would like to play for: "))
   wickets = int(input("Enter wickets you will play for: "))
   
   toss_winner = toss()
   
   first_batter = choose_batting(toss_winner)
   print(f"\n{first_batter.capitalize()} will bat first.")

   first_score, wickets_lost, balls = play_innings(first_batter, overs, wickets)
   
   target = first_score + 1

   second_batter = "computer" if first_batter == "player" else "player"
   print(f"Target: {target} for {second_batter}")

   second_score, wickets_lost, balls = play_innings(second_batter, overs, wickets, target)
   
   if first_batter == "player":
      player_score = first_score
      computer_score = second_score
   else:
      player_score = second_score
      computer_score = first_score

   display_result(player_score, computer_score)


main()
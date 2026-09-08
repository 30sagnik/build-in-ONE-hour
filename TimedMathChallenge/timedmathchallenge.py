"""
TIMED MATH CHALLENGE
Step1: State the operators in a list
Step2: State the max_limit and min_limit for taking random input within that range
Step3: Take input from user about total problem they want to solve and the opportunities they need
Step4: Create generate_problem() function. Use randint to generate left and right operands. Use choice to select a operator from the list
     --> Return the whole problem in a string. Use eval function to evaluate the answer
Step5: Use for loop to loop through the number of total questions
Step6: Get the problem and answer from the generate_problem function
Step7: Use while loop for the condition (chance < opportunities) --> Take input from the user for the given problem.
     --> if the input answer matches with the function generated answer ---> break
     --> else increment the chance
Step8: Use else with while --> Break when chance == oppportunities
Step9: Before for loop starts, use time module to note the time in a variable
Step10: After the whole loop ends, again note the time.
Step11: Subtract the time and get the time taken for the whole loop to run, which will state the time taken
Step12: Print the results

"""

import random
import time

OPERATORS = ['+', '-', '*', '%', '//']
MAX_LIMIT = 15
MIN_LIMIT = 1
total_problems = int(input("How many problems would you like to solve: "))
opportunities = int(input("How many opportunities do you want for wrong guesses: "))

def generate_problem():
   num_left = random.randint(MIN_LIMIT, MAX_LIMIT)
   num_right = random.randint(MIN_LIMIT, MAX_LIMIT)
   operator = random.choice(OPERATORS)

   problem = str(num_left) + " " + operator + " " + str(num_right)
   answer = eval(problem)
   return problem, answer

ready = input("Press Enter if you are ready to begin: ")
start_time = time.time()

chance = 0
correct = 0
for i in range(total_problems):
   problem, answer = generate_problem()
   
   while chance < opportunities:
      guess = input(f"#Problem {i+1} : {problem} =")
      if guess == str(answer):
         correct += 1
         break
      chance += 1
      print(f"{opportunities - chance} Opportunities left.")
   else:
      print("You are out of opportunities.")
      break

end_time = time.time()
total_time = round(end_time - start_time, 2)

if correct == total_problems:
   print(f"Congrats! You have completed the challenge in {total_time} seconds")
else:
   print("Try Again")
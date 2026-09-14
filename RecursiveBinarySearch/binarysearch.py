"""
RECURSIVE BINARY SEARCH
Step1: Create a sorted list of numbers
Step2: Take user input of the number they would like to find
Step3: Create the function with input of list and step count (default 0). Check if length of list is 0, return False
     --> Get the middle index of the list using length //2. Get the middle item
     --> Check if the input taken matches with it, if matches return True & exit
     --> if Input is higher, slice the list to check only numbers higher than mid, return recursive function
     --> if Input is lower, slice the list to check numbers till the min, return recursive function  
"""

numbers = [0,1,2,3,4,5,6,7,8,9]

find = int(input("Enter number you want to find: "))

def binarysearch(num_list, steps = 0):
   if len(num_list) == 0:
      return False
   
   middle_idx = len(num_list) //2
   middle = num_list[middle_idx]
   steps += 1
   print(f"Check: {middle}")
   if find == middle:
      print(f"Match found! \nAnswer: {middle}")
      print(f"Total Steps needed: {steps}")
      return True, steps
   elif find > middle and find <= num_list[-1]:
      num_list = num_list[middle_idx+1:]
      print("Higher")
      return binarysearch(num_list, steps)
   elif find < middle and find >= num_list[0]:
      num_list = num_list[:middle_idx]
      print("Lower")
      return binarysearch(num_list, steps)
   print("Item not found")

binarysearch(numbers)
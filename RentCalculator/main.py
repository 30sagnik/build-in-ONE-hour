"""
Steps: Take all input from User
Step1: Input rent of the whole room
Step2: Input electricity unit for the month
Step3: Input charge per unit
Step4: Total food ordered
Step5: List of all people staying
Step6: Did all people stay in this month -> True/False
Step7: If Yes,
	Total/no of people
	else ask for the person names in list:
		Total + cost-food/eaten by people & Total/ number of people
Step8: Print the amount to pay for each person
"""
print("Welcome to Rent Calculator")
room_rent = int(input("Enter the rent of the room: "))
unit_used = int(input("Enter electricity unit used: "))
charge_unit = int(input("Enter cost per unit: "))
food_ordered = int(input("Enter total cost of food ordered: "))
people = input("Enter name of people staying [use comma to seperate each names]: ").split(",")
people_list = [item.strip() for item in people]
print(people_list)
count = len(people_list)

#Condition of whether everyone was present and ordered food
is_food = input("Did everyone stayed for this month and ordered food? [Y/N] ").lower()[0]
if is_food == "y":
   contri = (room_rent + (unit_used * charge_unit) + food_ordered)//count
   for name in people_list:
      print(f"{name}: {contri}")
elif is_food == "n":
   absent = input("Enter people who were absent and did not order for food[use comma to seperate each names]:  ").split(",")
   absent_list = [item.strip() for item in absent]
   if not set(absent_list).issubset(set(people_list)):
      print("These names don't match with the people who are staying. Try again.")
      exit()   

   #Total cost
   total = room_rent + (unit_used * charge_unit)
   for name in people_list:
      if name in absent_list:
         print(f"{name}: {total//count}")
      else:
         print(f"{name}: {total//count + food_ordered//(count - len(absent))}")


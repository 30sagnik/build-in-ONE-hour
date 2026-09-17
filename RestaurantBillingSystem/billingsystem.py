"""
RESTAURANT BILLING SYSTEM
Step1: Create the order function with input of *foods and **settings
Step2: Loop through the list of foods, if food item is in menu, then get the amount by price * quantity
    --> Add the amount to total_amount
    --> If item is not in food menu, print that Item is not on menu
Step3: Get the Discount from the settings dictionary using get function, if not present then return 0
Step4: Get the tax from the settings dictionary using get function, if not present then resturn 0
Step5: Subtract the discount from the amount, if any discount is there
Step6: Add tax to the amount and return the final amount
Step7: Initiate the function with a list of tuple of items with their quantity, then add discount, tax and any other settings
       Function(("Burger", 2), discount = 7, tax = 5)
"""
menu = {
   "Burger" : 120,
   "Fries": 80,
   "Coke": 50,
   "Pizza": 250,
   "Coffee": 100
   }

def order(*foods, **settings):
   amount = 0
   for food, quantity in foods:
      if food in menu:
         food_price = menu[food] * quantity
         print(f"Item: {food} Quantity: {quantity} --> Amount: {food_price}")
         amount += food_price
      else:
         print(f"{food} is not available on the menu")
   print(f"Total Amount: {amount}")

   discount = settings.get("discount", 0)
   tax = settings.get("tax", 0)

   amount -= amount*(discount/100)
   print(f"After {discount}% Discount: {amount}")

   amount += amount*(tax/100)
   print(f"After {tax}% Tax: {amount}")

   return amount

print("\n-------Order 1-------")
order(
    ("Burger", 2),
    ("Fries", 3),
    ("Pizza", 1),
    ("Burger", 1),
    tax = 5,
    discount = 10
)


print("\n-------Order 2-------")
order(
    ("Coke", 5),
    ("Coffee", 3),
    ("Coke", 2),
    discount=10,
    tax=5
)

print("\n-------Order 3-------")
order(
    ("Burger", 1),
    ("Fries", 1),
    ("Coke", 1),
    ("Pizza", 1),
    ("Coffee", 1),
    tax=10,
    discount=5
)
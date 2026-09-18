"""
DISCOUNT PRICING ENGINE
Note: Here we store functions in a dictionary
Step1: Create different functions with input of price and different operations
Step2: Create a dictionary with each key's value as a function
Step3: Take input of the discount option.
Step4: Get the function from the dictionary and input the price. Print the after discount price. 
"""

def student_discount(price):
   return price - (price * 0.15)

def festival_discount(price):
   return price - (price * 0.20)

def bulk_discount(price):
   return price - (price * 0.30)
 
def no_discount(price):
   return price

discount_rules = {
   "student": student_discount,
   "festival": festival_discount,
   "bulk": bulk_discount,
   "no": no_discount
}

select_offer = input(f"Enter offer {discount_rules.keys()} : ").lower()

if select_offer in discount_rules:
   offer = discount_rules[select_offer]
   price = int(input("Enter price: "))
   amount = offer(price)
   print(f"Final Price: {amount}")
else:
   print("Invalid Offer")
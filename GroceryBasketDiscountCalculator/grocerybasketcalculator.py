"""
GROCERY BASKET DISCOUNT CALCULATOR

Step1: Make a dictionary of products having name: [price, offer]
Step2: State a bulk_offer. Apply string indexing and manipulation to get the bulk_price, discount, limit
Step3: While loop to add products in the cart
Step4: Set an exit commadn to exit the loop and get to the final result
Step5: If name does not match with the names in product disctionary, again ask for the product

------Types of Offer: 1. Buy X Get Y Free            2.Buy X Get Y% Discount
Step6: Use string indexing to get all the values. Convert into int. Save them in variables

-->Step7: Formula for 'FREE': discounted_quantity= X * quantity//(X+Y) + min(X, quantity%(X+Y))

Step8: Get the discounted amount by multiply discounted_quantity with price

-->Step8: Formula for 'DISCOUNT': Give a condition if the quantity>=X: Then apply the discount. Else keep the original amount

Step9: If no offer specified, state the orginal amount

-->Step10: Now give the condition of bulk_offer: If the original_amount > bulk_amount, then apply the discount.
       --> If discount > limit then just provide the limit discount not more than that

Step11: Display in table format using print(f"{'String':<20}")

"""

#Specify all the products in a dictionary
products = {
   "Britania Marie" : [50, "Buy:3 Get:2 Free"],
   "ParleG HappyHappy": [90, ""],
   "Haldiram Bhujia": [120, "Buy:1 Get:1 Free"],
   "Britania Slice Cake": [40, "Buy:5 Get:10% Discount"],
   "Tata Tea": [100, "Buy:1 Get:10% Discount"],
   "Cadbury DairyMilk": [50, ""],
   "Bhikharam Soan Papdi": [130, "Buy:3 Get:2 Free"],
   "Good Day Butter": [45, "Buy:2 Get:1 Free"],
   "Sunfeast Dark Fantasy": [60, "Buy:1 Get:10% Discount"],
   "Amul Butter 100g": [58, ""],
   "Kissan Mixed Fruit Jam": [150, "Buy:2 Get:20% Discount"],
   "Maggi 2-Minute Noodles": [14, "Buy:12 Get:2 Free"],
   "Lays Magic Masala": [20, "Buy:5 Get:1 Free"],
   "Kurkure Masala Munch": [20, "Buy:4 Get:1 Free"],
   "Nestle Everyday Milk Powder": [220, "Buy:1 Get:15% Discount"],
   "Taj Mahal Tea": [180, "Buy:2 Get:1 Free"],
   "Saffola Gold Oil 1L": [190, "Buy:2 Get:10% Discount"],
   "Dabur Honey 250g": [125, "Buy:1 Get:1 Free"],
   "NutriChoice Digestive": [85, "Buy:3 Get:1 Free"],
   "Bisk Farm Top Biscuit": [30, "Buy:4 Get:1 Free"],
   "Catch Red Chilli Powder": [75, "Buy:2 Get:15% Discount"],
   "Everest Garam Masala": [68, ""],
   "Knorr Tomato Soup": [55, "Buy:3 Get:1 Free"],
   "Real Mixed Fruit Juice": [110, "Buy:2 Get:1 Free"],
   "MTR Masala Dosa Mix": [95, "Buy:1 Get:10% Discount"],
   "Kwality Wall's Vanilla": [140, "Buy:1 Get:1 Free"]
   }

print("==========================GROCERY STORE============================")
print(
   f"{'Item':<30}"
   f"{'Offer':<30}"
   f"{'Price':<10}"
)
print("_"*103)
for item, list in products.items():
   print(
      f"{item:<30}"
      f"{list[1]:<30}"
      f"{list[0]:<10}"
   )

mega_discount = "Get 20% Off on order of Rs.5000 or above upto Rs.2000"
bulk_offer = mega_discount.replace(" ","")
bulk_dis = int(bulk_offer[bulk_offer.find('Get') + len('Get') : bulk_offer.find('%')])
bulk_amount = int(bulk_offer[bulk_offer.find('Rs.') + len('Rs.') : bulk_offer.rfind('or')])
bulk_limit = int(bulk_offer[bulk_offer.rfind('Rs.') + len('Rs.') :])

print(f"\nMEGA DISCOUNT: {mega_discount}\n")

original_bill = 0
dis_bill = 0
cart = {}
while True:
   item = input("Enter product[Type 'Order' to quit]: ")
   if item.lower() == "order":
      break
   if item not in products.keys():
      print("This product is not in our store")
   else:
      quantity = int(input(f"Enter the quantity of {item} required: "))
      original_amount = quantity * products[item][0]
      original_bill += original_amount
  

      if products[item][1].find('Free') != -1:
         string = products[item][1].replace(" ","")
         val1 = int(string[len('Buy:'): string.find('Get:')])
         val2 = int(string[string.rfind(':') + 1: string.find('Free')])
         sets = quantity//(val1+val2)
         remainder = quantity % (val1+val2)
         dis_quantity = (val1 * sets) + min(remainder, val1)
         dis_amount = dis_quantity * products[item][0]

         cart[item] = [products[item][1], quantity, original_amount, dis_amount]
         dis_bill += dis_amount
         

      elif products[item][1].find('Discount') != -1:
         string = products[item][1].replace(" ","")
         val1 = int(string[len('Buy:'): string.find('Get:')])
         val2 = int(string[string.rfind(':') + 1: string.find('%')])
         if quantity >= val1:
            dis_amount = original_amount - ((quantity * products[item][0]) * (val2/100))
            
            cart[item] = [products[item][1], quantity, original_amount, dis_amount]
            dis_bill += dis_amount
         else:
            dis_amount = quantity * products[item][0]
            cart[item] = [products[item][1], quantity, original_amount, dis_amount]
            dis_bill += dis_amount

      else:
         dis_amount = original_amount
         
         cart[item] = [products[item][1], quantity, original_amount, dis_amount]
         dis_bill += dis_amount

      print(f"{item}: {dis_amount}")

print("========================================GROCERY BILL=========================================")

if original_bill >= bulk_amount:
   if original_bill * (bulk_dis/100)  <= bulk_limit:
      discount = original_bill * (bulk_dis/100)
      dis_bill = original_bill - discount
   else:
      discount = bulk_limit
      dis_bill = original_bill - discount
   
   print(
      f"{'Item':<30}"
      f"{'Quantity':<10}"
      f"{'Original Price':<15}"
   )
   print("_"*60)
   for item, list in cart.items():
      print(
         f"{item:<30}"
         f"{list[1]:<10}"
         f"{list[2]:<15}"
      )
   print("="*35 + f"{'Total:':<8}" + f"{original_bill:<8}")
   print(" "*35 + f"{'Discount:':<8}" + f"{discount:<8}")
   print(" "*35 + f"{'After Discount:':<8}" + f"{dis_bill:<8}")
   

else:
   print(
      f"{'Item':<30}"
      f"{'Offer':<30}"
      f"{'Quantity':<10}"
      f"{'Original Price':<18}"
      f"{'After Discount':<15}"
   )
   print("_"*103)
   for item, list in cart.items():
      print(
         f"{item:<30}"
         f"{list[0]:<30}"
         f"{list[1]:<10}"
         f"{list[2]:<18}"
         f"{list[3]:<15}"
      )
   print("="*72 + f"{'Amount to Pay:  '}" + f"{dis_bill:<8}")


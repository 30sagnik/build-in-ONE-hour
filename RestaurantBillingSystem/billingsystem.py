"""
RESTAURANT BILLING SYSTEM
"""
menu = {
   "Burger" : 120,
   "Fries": 80,
   "Coke": 50,
   "Pizza": 250,
   "Coffee": 100
   }

def add_item(*items, order = None):
   for item, quantity in items:
      if item in menu.keys():
         if item in order:
            order[item] += quantity
         else:
            order[item] = quantity
   return order

def calculate_subtotal(order):
   subtotal = 0
   for item, quantity in order.items():
      subtotal += menu[item] * quantity
   return subtotal

def create_order(*items, **conditions):
   order = {}
   add_item(*items, order = order)

   subtotal = calculate_subtotal(order)
   final_total = subtotal

   discount_amount = 0
   if "discount" in conditions:
      discount_amount = final_total * (conditions["discount"]/100)
      final_total -= discount_amount

   tax_amount = 0
   if "tax" in conditions:
      tax_amount = final_total * (conditions["tax"]/100)
      final_total += tax_amount

   for item, quantity in order.items():
      item_total = menu[item] * quantity
      print(f"  - {item} x {quantity} = ₹{item_total}")

   if "discount" in conditions:
      print(f"Discount     : -₹{discount_amount}")
   if "tax" in conditions:
      print(f"Tax          : +₹{tax_amount}")
   print(f"Final Total  : ₹{final_total}")

   return final_order


create_order(
    ("Burger", 2),
    ("Fries", 3),
    ("Pizza", 1),
    ("Burger", 1),
    discount=10,    
    tax=5
)
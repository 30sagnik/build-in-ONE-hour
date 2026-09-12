"""
DATA PROCESSING PIPELINE

Step1: Create the filter function to filter based on amount. Filter items of above the limit.
Step2: Create the map function to get the amount on each product sold based on quantity x price.
Step3: Create the reduce function to get the total sum of amount using reduce from functools
Step4: Use function to take input of limit to filter, map and get the total revenue.
Step5: Create function to take minimum limit of price and filter orders to get the items having higher price.
Step6: Create a discounted_revenue function to input discount and get the the total revenue after discount.
"""

from functools import reduce

orders = [
    {"item": "Laptop", "price": 70000, "quantity": 1},
    {"item": "Mouse", "price": 1200, "quantity": 2},
    {"item": "Keyboard", "price": 2500, "quantity": 1},
    {"item": "Monitor", "price": 18000, "quantity": 2},
    {"item": "USB Cable", "price": 500, "quantity": 3}
]

def filter_orders(orders, limit):
   filtered = list(filter(lambda order: order['price'] >= limit, orders))
   return filtered

def transform_products(filtered):
   transformed = list(map(lambda order: order['price'] * order['quantity'], filtered))
   return transformed

def total(transformed):
   total_sum = reduce(lambda a,b: a+b, transformed)
   return total_sum


def revenue(orders):
   limit = int(input("Enter minimum limit: "))
   filtered = filter_orders(orders, limit)
   
   transformed = transform_products(filtered)

   total_sum = total(transformed)
   return total_sum

def high_value_products(orders):
   limit = int(input("Enter minimum limit: "))
   filtered = filter_orders(orders, limit)
   
   products = [product['item'] for product in filtered]
   print(f"High Value Products above Rs.{limit}: {products}")

def discounted_revenue(orders):
   discount = int(input("Enter discount %: "))
   discounted = list(map(lambda order: (order['price'] * order['quantity'] * (1 - discount/100)), orders))
   
   discounted_sum = reduce(lambda a,b: a+b, discounted)
   return discounted_sum

print("\nTOTAL REVENUE\n")
total = revenue(orders)
print(f"Total Revenue: {total}")

print("\nHIGH VALUE PRODUCTS\n")
high_value_products(orders)

print("\nDISCOUNTED REVENUE\n")
discounted = discounted_revenue(orders)
print(f"Discounted Revenue: {discounted}")
   
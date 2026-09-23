"""
SHOPPING CART
Step1: Create Product class. Define init method and pass Id, name & price
Step2: Create Cart class. Define init method which only tales self because cart does not require any initialization arguments
     --> Create a instance variable 'items' & assign en empty list
Step3: Define method to add items to Cart list. Pass product. Append the object to the list
Step4: Define remove method to remove a desired product from the list
Step5: Define method to calculate total value of cart. Loop through the list and add the item.price to get the total
Step6: Define display method to print the items(ID, name, price) in the Cart
Step7: First make products(objects) from the Product class
Step8: Then instantiate the Cart class
     --> For add & remove save and remove the previously created product object from the Cart
"""

class Product:
   def __init__(self, product_id, name, price):
      self.product_id = product_id
      self.name = name
      self.price = price

class Cart:
   def __init__(self):
      self.items = []

   def add_product(self, product):
      self.items.append(product)

   def remove_product(self, product):
      self.items.remove(product)

   def calculate_total(self):
      total = 0
      for item in self.items:
         total += item.price
      return total

   def display(self):
      for item in self.items:
         print(f"Id: {item.product_id} | Product: {item.name} | Price: {item.price}")   


p1 = Product(32124, 'Biscuit', 55)
p2 = Product(12131, 'Chips', 30)
p3 = Product(21311, 'Cheese', 120)

cart = Cart()

cart.add_product(p1)
cart.add_product(p2)
cart.add_product(p3)
cart.display()

total = cart.calculate_total()
print(f"Cart Total: {total}")

cart.remove_product(p3)
cart.display()
print(f"Cart Total: {cart.calculate_total()}")
   
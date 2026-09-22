"""
RECTANGLE CALCULATOR
Step1: Create a class of Rectangle and define constructor to pass self, length & breadth
Step2: Define methods to return the area, perimeter and check is_square 
Step3: Define method to display details of each object of rectangle
    --> Print the length, breadth, then get the area, perimeter, is_square and print them
Step4: Create (objects)instance of the class.Use display method to display details for each object
"""

class Rectangle:
   def __init__(self, length, width):
      self.length = length
      self.width = width

   def area(self):
      return self.length * self.width
    
   def perimeter(self):
      return (self.length + self.width) * 2
   
   def is_square(self):
      if self.length == self.width:
         return True
      return False

   def display(self):
      print(f"length: {self.length} | width: {self.width} | Area: {self.area()} | Perimeter: {self.perimeter()} | Square: {self.is_square()}")

r1 = Rectangle(10, 20)
r2 = Rectangle(20, 20)

r1.display()
r2.display()

#Change length of r1 and check
r1.length = 20
r1.display()
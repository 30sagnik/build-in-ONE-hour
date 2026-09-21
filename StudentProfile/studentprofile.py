"""
STUDENT PROFILE
Step1: Create a Student Class
Step2: Create init method (Constructor) and define the instance variables: name, roll, branch, age, marks[]
Step3: Create Instance method passing self as Instance. Display the details of the student
Step4: Create other Instancce method to get the average from marks
Step5: Create a method to check passed. Pass self and passmarks to the method
    --> Use 'any' function and loop over the marks list to check if any mark is less than pass marks
Step6: Create an object(instance) of the class s1
Step7: Display the student details, get the average, check if passed or not
"""

class Student:
   def __init__(self, name, roll_no, branch, age, marks):
      #Instance Variables
      self.name = name
      self.roll = roll_no
      self.branch = branch
      self.age = age
      self.marks = marks

   #Instance Methods
   def display(self):
      print(f"Name: {self.name} | Roll No: {self.roll} | Branch: {self.branch} | Age: {self.age} | Marks: {self.marks}")

   def calculate_avg(self):
      return round(sum(self.marks) / len(self.marks), 2)

   def is_passed(self, pass_marks):
      if any(mark < pass_marks for mark in self.marks):
         return False
      else:
         return True

#Object(Instance) of Student class
s1 = Student('Sagnik', 46, 'CSE', 22, [22,47,53])

s1.display()    #---> Student.display(s1)

average = s1.calculate_avg()
print("Average:", average)

pass_marks = 25
passed = s1.is_passed(pass_marks)
print("Passed:", passed)
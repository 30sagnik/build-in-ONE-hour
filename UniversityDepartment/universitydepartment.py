"""
UNIVERSITY DEPARTMENT
Step1: Create a Class of University. Define init method and create a instance variable of dictionary of departments
Step2: Define a method to create a new department. First check whether the department name already exists or not
    --> If not, then instantiate the inner class and store it in the dictionary against the name
Step3: Define method to display details of all departments
Step4: Create the inner class (Department). Define init method and pass the name of the department
    --> Create instance variables of department_name, student list, faculty list, course list
Step5: Define method to add_student, add_faculty & add_course to students list, faculty list & courses list respectively
Step6: Define display method inside inner class to display all details of the particular department
Step7: Create a object of University. Using its create_department method to instantiate a Department object
    --> Give the department name. Store the object in a variable 
    --> This variable (object) can be used to add student, faculty, course & display the details
"""

class University:
   def __init__(self):
      self.departments = {}

   def create_department(self, name):
      if name in self.departments:
         print(f"{name} Department Name already exists")
         return
      department = self.Department(name)
      self.departments[name] = department
      return department

   def display_departments(self):
      for department in self.departments.values():
         print(f"Department: {department.name} | "
               f"Students: {len(department.students)} | "
               f"Faculties: {len(department.faculty)} | "
               f"Courses: {len(department.courses)}"
           )


   class Department:
      def __init__(self, name):
         self.name = name
         self.students = []
         self.faculty = []
         self.courses = []

      def add_student(self, new_student):
         self.students.append(new_student)
         print(f"{new_student} joined {self.name} department")

      def add_faculty(self, new_faculty):
         self.faculty.append(new_faculty)
         print(f"{new_faculty} appointed in {self.name} department")

      def add_course(self, new_course):
         self.courses.append(new_course)
         print(f"{new_course} added to {self.name} department")

      def display(self):
         print(f"Students: {', '.join(self.students)}")
         print(f"Faculties: {', '.join(self.faculty)}")
         print(f"Courses: {', '.join(self.courses)}")

uni = University()

# Create departments
cse = uni.create_department("CSE")
ece = uni.create_department("ECE")
me = uni.create_department("ME")

# CSE
cse.add_student("Sagnik")
cse.add_student("Soma")
cse.add_student("Vola")

cse.add_faculty("Dr. Sam")
cse.add_faculty("Dr. John")

cse.add_course("Python")
cse.add_course("Data Structures")
cse.add_course("Machine Learning")

# ECE
ece.add_student("Rahul")
ece.add_student("Ananya")

ece.add_faculty("Dr. Sharma")
ece.add_faculty("Dr. Das")

ece.add_course("Digital Electronics")
ece.add_course("Microprocessors")

# ME
me.add_student("Arjun")
me.add_student("Riya")
me.add_student("Amit")

me.add_faculty("Dr. Roy")

me.add_course("Thermodynamics")
me.add_course("Fluid Mechanics")
me.add_course("Machine Design")

# Display individual departments
cse.display()
ece.display()
me.display()

# Display university
uni.display_departments()

# Duplicate department test
uni.create_department("CSE")

# Independence test
ece.add_student("Kunal")

cse.display()
ece.display()

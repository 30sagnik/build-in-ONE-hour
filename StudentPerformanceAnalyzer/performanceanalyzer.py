"""
STUDENT PERFORMANCE ANALYZER
Step1: Create a dictionary of students with marks in lists as values.
Step2: Create the function to take input of the dictionary and iterate through each student to calculate the total marks.
     --> Return the total marks of each student in a dictionary
Step3: Create a function to calculate average just like previous function and return in a dictionary
Step4: Create a top_x function to get top X students in the dictionary based on their marks
     --> Create a temporary copy of the main dictionary. Iterate through the dictionary. Handle if the total students is less than x. 
     --> Use max function to get the max score and use a key to choose the marks section of the total marks dictionary
     --> Append the name, marks to a new list. Then pop the max item from the temporary dictionary.
     --> Repeat the process to get 1st, 2nd, 3rd, and so on
Step4: Create the get_passed function to get students who passed
     --> Iterate through the dictionary and use conditions to check if marks < pass marks. If any is True append to failed_list
     --> Else append to Passed_list
"""
students = {
    "Sagnik": [85, 92, 78],
    "Rahul": [65, 71, 80],
    "Ananya": [30, 30, 30],
    "Biswas": [25, 92, 78],
    "Soma": [85, 11, 80],
    "Ankita": [30, 80, 15]
}


def score(students):
   total_marks = {}
   for name, marks in students.items():
      total_marks[name] = sum(marks)
   return total_marks


def top_x(total_marks):
   remaining = total_marks.copy()
   toppers = []
   x = int(input("Top X: "))
   i = 0
   for i in range(min(x, len(remaining))):
      student, marks = max(remaining.items(), key = lambda x: x[1])

      toppers.append((student, marks))
      remaining.pop(student)

   return toppers


def average(students):
   avg_marks = {}
   for name, marks in students.items():
      avg = sum(marks)/len(marks)
      avg_marks[name] = round(avg, 3)
   return avg_marks


def get_passed(students):
   pass_marks = int(input("Enter the pass marks: "))
   passed = []
   failed = []
   for name, marks in students.items():
      for mark in marks:
         if mark < pass_marks:
            failed.append(name)
            break
      else:
         passed.append(name)

   return passed, failed

total_marks = score(students)

toppers = top_x(total_marks)
print("\nToppers: ")
for name, marks in toppers:
   print(f"{name}: {marks}")

avg_marks = average(students)
print("\nAverage Marks of each students: ")
for name, marks in avg_marks.items():
   print(f"{name}: {marks}")

passed, failed = get_passed(students)
print(f"\nPassed: {passed}")
print(f"\nFailed: {failed}")





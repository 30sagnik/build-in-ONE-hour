"""
RECURSIVE DIRECTORY SIZE CALCULATOR
Chapter1: Calculating total size of directory
Step1: Create the function, with input of folder
Step2: Assign a variable with value 0
Step3: Iterate item, value through the dictionary.item()
Step4: If type of value is int, which means it is the endpoint(size of a file), add it to the total
Step5: Else total is equal to total + Recursive function for the value(sub-dictionary)
Step6: Return total
"""
project = {
    "main.py": 12,

    "data": {
        "users.csv": 20,
        "orders.csv": 30
    },

    "models": {
        "model.py": 25,

        "utils": {
            "helper.py": 15
        }
    }
}

#Calculate total folder size
def calculate_size(folder):
   total = 0

   for item, value in folder.items():
      if isinstance(value, int):
         total += value
      else:
         total += calculate_size(value)
   return total
         
print(f"Total Size: {calculate_size(project)}")

"""
Chapter2: Finding whether a file exists in the folder or not
Step1: Create a function with input of the folder and target file/subfolder
Step2: Iterate through the dictionary items
Step3: If item is equal to target, return True
Step4: Elif value is dictionary, then assign result to recursive function with input of value for that iteration
Step5: If result is True, then return True and exit, otherwise continue the loop
Step6: Outside the whole for loop return False
"""

#Check if sub-folder or file is present or not in the folder
def find(folder, target):
   for item, value in folder.items():
      if item == target:
         return True
      elif isinstance(value, dict):
         result = find(value, target)
         if result:
            return True
   return False

print(f"Found: {find(project, "model.py")}")
print(f"Found: {find(project, "models")}")
print(f"Found: {find(project, "modeles")}")
print(f"Found: {find(project, "helper.py")}")

"""
Chapter3: Calculate size of sub-foder/file
Step1: Create the function with input of target sub-folder and folder
Step2: Initiate a loop for all the folder dictionary items
Step3: If item is equal to target, and item is value is dictionary return calculate function for that value
Step4: If not dictionary, return the value(as file-size)
Step5: If item is not equal to target and value is dictionary, result is equal to recursive function of value(as folder)
Step6: If result is not None, then return the result, otherwise continue the loop
"""

#Calculate size of sub-foler or file
def subfolder(sub, folder):
   for item, value in folder.items():
      if item == sub:
         if isinstance(value, dict):
            return calculate_size(value)
         else:
            return value
      if isinstance(value, dict):
         result = subfolder(sub, value)
         if result is not None:
            return result
   return None

print(f"Subfolder Size: {subfolder("model.py", project)}")
print(f"Subfolder Size: {subfolder("models", project)}")

      

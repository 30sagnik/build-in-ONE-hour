"""
PASSWORD VALIDATOR
Step1: Create mulyiple functions to check the password like lowercase chars, uppercase chars, length , etc
     --> Use 'any' function to check if any character returns true value
Step2: Create a list storing all functions as items
Step3: Define the Higher order function with input of password and the rule needed to be implemented
Step4: Create an empty list with input of password and list of rules
     --> Initiate a for loop to get the rules one by one and implement it on the function and append the result to the results list
     --> Also increment the count if the function outcome is true
Step5: Return results and count. Print it
"""

def has_min_length(password):
   return len(password) >= 8

def is_uppercase(password):
   return any(char.isupper() for char in password)

def is_lowercase(password):
   return any(char.islower() for char in password)

def is_digit(password):
   return any(char.isdigit() for char in password)

def has_special_char(password):
   special_chars = "~!@#$%^&*()-_=+[]{}:;',<>./?"
   return any(char in special_chars for char in password)

rules = [
   has_min_length,
   is_uppercase,
   is_lowercase,
   is_digit,
   has_special_char
]

#Higher Order Function: Function as a parameter
def validate_password(password, rules):
   results = []
   count = 0

   for rule in rules:
      results.append(rule(password))
      if rule(password):
         count += 1

   return results, count

password = input("Enter the password: ")
results, count = validate_password(password, rules)
print(results)
print(f"You have {count} fields validated among {len(rules)} fields in your password")


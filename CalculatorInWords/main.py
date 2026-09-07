"""
CALCULATOR IN WORDS
Step1: Take input of the calculation in string
Step2: Make it uppercase and strip all whitespace present in the string
Step3: State the 4 Operators in a list[+,-,*,/]
Step4: Check which operator is present in the string
        - if none present exit the code
Step5: Import operator module and build a dictionary stating each operator as keys and value as the operation to perform [operator.add]
Step6: num1 and num2 should be extracted by string indexing. Take input of num1 and num2
Step7: If operator is not None -----> Perform the calculation.
"""

import operator

print("Operators:\n -PLUS: +\n -MINUS: -\n -MULTIPLY: *\n -DIVIDE: /\n")
string_input = input("Type the Calculation you want to do[e.g. APLUSB => A+B] : ").upper()
string = string_input.replace(" ","")
all_operators = ['PLUS', 'MINUS', 'MULTIPLY', 'DIVIDE']
operate = ""
for op in all_operators:
   if string.find(op) != -1:
      operate = op
      index = string.find(op)
      break
else:
   print("Invalid Operator")
   print("Try Again")
   exit()

operator_mapping = {
   "PLUS": operator.add,
   "MINUS": operator.sub,
   "MULTIPLY": operator.mul,
   "DIVIDE": operator.truediv
   }

num1 = string[:index]
num2 = string[len(num1)+len(operate):]
operand1 = int(input(f"Enter {num1}: "))
operand2 = int(input(f"Enter {num2}: "))

if operator != None:
   operation = operator_mapping[operate]
   calculation = operation(operand1, operand2)
   print(f"Result: {calculation}")


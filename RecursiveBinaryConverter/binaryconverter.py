"""
RECURSIVE BINARY CONVERTER
Step1: Create the function with input as number.
Step2: If number = 0, then return empty string.
Step3: Get the remainder from number divided by 2.
Step4: Use Recursive function with input num//2, and assign it to variable answer.
Step5: Add answer with remainder of num%2, and re-assign it with answer.
Step6: Return answer.
          num
           7
        3  |  1
     1  |  1
  0  |  1
  | ''

''+'1'+'1'+'1'
"""

def binaryconverter(num):
   if num == 0:
      return ""
   remainder = num % 2
   print(f"{num} --> {num//2} --> {remainder}")
   answer = binaryconverter(num//2)
   answer += str(remainder)
   return answer

number = int(input("Enter the decimal number: "))
print(f"Decimal: {number}")
answer = binaryconverter(number)
print(f"Binary: {answer}")
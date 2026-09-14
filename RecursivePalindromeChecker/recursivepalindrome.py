"""
RECURSIVE PALINDROME: First Approach
Step1: Create the function to take input of string
Step2: Assign start_index as 0, end_index as length of string -1
Step3: Check if start_index is larger or equal to end_index. If yes, return True as we need to check till middle
Step4: Check if the word at every start_index and end_index is equal, if not return False
Step5: Slice the word from one char after start, till one char before end
Step6: Recursive function on the new word
Step7: Initiate the function with a string.
"""

def palindrome(word):
   start = 0
   end = len(word) -1
   if start >= end:
      return True
   if word[start] != word[end]:
      return False
   print(f"Check: {word[start]}  & {word[end]}")
   word = word[start+1: end]
   return palindrome(word)   

check_string = input("Enter string to check Palindrome: ")
check = palindrome(check_string)
print(f"{check_string} Is Palindrome: {check}")


"""
RECURSIVE PALINDROME: Second Approach
Step1: Define the function with input of string, start & end
Step2: Check if start_index is >= end_index then return True
Step3: Check if start is not equal to end element then return False
Step4: Use Recursive function with input string, start_index +1, end_index -1
Step5: Initiate the function with a input string, start as 0, end as length of string -1
"""

def palindrome_2(word, start, end):
   if start >= end:
      return True
   if word[start] != word[end]:
      return False
   print(f"Check: {word[start]}  & {word[end]}")
   return palindrome_2(word, start + 1, end - 1)

check_string2 = input("Enter string to check Palindrome: ")
check2 = palindrome_2(check_string2, 0 , len(check_string) - 1)
print(f"{check_string2} Is Palindrome: {check2}")

"""
RECURSIVE PALINDROME: Second Approach
Step1: Define a function with input of the string
Step2: Check if the length of the string is less than or equal to 1, then return True
Step3: Check if starting item is not equal to ending item, then return False
Step4: Slice the word from 2nd Index to 2nd last index
Step5: Use recursive Function with intput of the new word after slicing
Step6: Initiate the function with a input string
"""

def palindrome_3(word):
   if len(word)<=1:
      return True
   if word[0] != word[-1]:
      return False
   print(f"Check: {word[0]}  & {word[-1]}")
   word = word[1:-1]
   return palindrome_3(word)

check_string3 = input("Enter string to check Palindrome: ")
check3 = palindrome_3(check_string2)
print(f"{check_string3} Is Palindrome: {check3}")
import math
#Factorial function using recursion
def factorial(num):
   if num <= 1:
      return 1
   return num * factorial(num-1)

#Calculate Greatest Common Factor
def gcd(*nums):
   return math.gcd(*nums)

#Calculate Least common factor
def lcm(*nums):
   return math.lcm(*nums)

#Calculate Power
def power(num, pow):
   return num ** pow
         
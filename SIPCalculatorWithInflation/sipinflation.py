"""
SIP Calculator With Inflation
Step1: Create a function with input of inflation rate.
Step2: Create inner function with input of function, this would be declared as decorator.
Step3: Create wrapper function having the rate of return, years and SIP amount
Step4: Initiate the function in the decorator function and store it in a variable
Step5: Use the formula to get the real amount deducting inflation. Return the real amount
Step6: Return the wrapper function
Step7: Return the decorator function
Step6: Declare the Decorator with input of the inflation rate value
Step7: Define the function to calculate the SIP by taking input of rate of Return, Years, and SIP value
Step8: Initiate the function with the rate, years and SIP value
"""

def inflation(inflation_rate):
   def decorator(func):
      def wrapper(rate_return, years, monthly_sip):
         future_value = func(rate_return, years, monthly_sip)
         inflation = inflation_rate/100
         real_value = future_value / ((1 + inflation) ** years)
         return round(real_value, 2), future_value
      return wrapper
   return decorator

inflation_rate = int(input("Enter annual inflation rate: "))

@inflation(inflation_rate)
def sip(rate_return, years, monthly_sip):
   rate_return = rate_return / (12 * 100)
   future_value = monthly_sip * ((((rate_return + 1) ** (12 * years)) - 1) / rate_return) * (1 + rate_return)
   return round(future_value, 4)

rate_of_return = float(input("Enter annual rate of Return: "))
duration = int(input("Enter Duration: "))
monthly_sip = int(input("Enter monthly SIP: "))

real_value, future_value = sip(rate_of_return, duration, monthly_sip)

print(f"Total Return: {future_value}")
print(f"Return after deducting Inflation: {real_value}")
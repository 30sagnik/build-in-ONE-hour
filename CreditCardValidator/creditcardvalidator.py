"""
CREDIT CARD VALIDATOR
Step1: Take input of the Credit Card no.
Step2: Use the Luhn's Algorithm
Step3: Iterate from second last digit backwards skipping one digit
Step4: Multiply by 2
Step5: If the number>9 ---> 1st digit + 2nd digit
     --> else number. Do sum of all the numbers and assign a variable sum_even
Step6: Do sum of rest of the digits of the card no. ans assign to sum_odd
Step7: Do the total
Step8: If total MOD 10 == 0: Valid ---> else: Invalid

"""

card_no = input("Enter your Credit Card No.: ").replace("-","").replace(" ","")

sum_even = 0
for i in card_no[-2::-2]:
   i = int(i)*2
   if i>= 10:
      sum_even += (i//10) + (i%10)
   else:
      sum_even += i

print(sum_even)

sum_odd = 0
for i in card_no[-1::-2]:
   sum_odd += int(i)
print(sum_odd)

total = sum_even + sum_odd
if total % 10 == 0:
   print('Valid Credit Card')
else:
   print('Invalid Credit Card')



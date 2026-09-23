"""
BANK ACCOUNT
Step1: Create BankAccount Class. Define init method and declare the account_no, name & balance
Step2: Create deposit method passing amount. Add the amount to the balance
Step3: Create withdraw method and if amount is less than balance then subtract amount from balance
Step4: Define a method to print the current balance
Step5: Define a method to print all bank details
"""

class BankAccount:
   def __init__(self, account_no, holder_name, balance):
      self.account_no = account_no
      self.holder_name = holder_name
      self.balance = balance

   def deposit(self, amount):
      self.balance += amount
      print(f"{amount}/- deposited to Account No: {self.account_no}")

   def withdraw(self, amount):
      if self.balance >= amount:
         self.balance -= amount
         print(f"{amount}/- withdrawn from Account No: {self.account_no}")
      else:
         print("Insufficient Balance")

   def check_balance(self):
      print(f"Current Balance: {self.balance}")

   def display(self):
      print(f"Account No: {self.account_no} | Acc Holder Name: {self.holder_name}" | Balance: {self.balance})

acc1 = BankAccount(43092323456, 'Sagnik Dey', 5000)

acc1.display()

acc1.deposit(3000)

acc1.withdraw(2000)

acc1.check_balance()

acc1.display()

acc2 = BankAccount(23234241214, 'John Ghosh', 10)

acc2.display()
"""
ATM Operation
Step1: Make a Dictionary of accounts with there initial balance as 0
Step2: Define a function to login, if the Card no does not matches with those in the dictionary --> return False
Step3: Function for show balance
Step4: Function for Deposit
Step5: Function for Withdraw --> Accounts, Card_no
Step6: Main Function: Login --> if False --> Exit
Step7: Show Choice: Show balance, Deposit, Withdraw, Exit
Step8: Deposit --> Balance + Deposit    |    Withdraw --> Balance - Withdraw

"""
Accounts = {
   "432111115403": 0,
   "601100099013": 0,
   "222300312200": 0,
   "424242424242": 0,
   "362272062716": 0
   }

def login(Accounts):
   card_no = input("Enter Your Card No.: ").replace("-","").replace(" ","")
   if card_no not in Accounts:
      return False
   return card_no

def show_balance(card_no):
   balance = Accounts[card_no]
   return balance

def deposit():
   deposit = int(input("Enter amount you would like to deposit: "))
   if deposit <= 0:
      print("Invalid amount. Give an amount > 0")
      return 0
   return deposit

def withdraw(Accounts, card_no):
   withdraw = int(input("Enter amount you would like to withdraw: "))
   if withdraw > Accounts[card_no]:
      print("Insufficient Balance")
      return 0
   elif withdraw < 0:
      print("Invalid amount. Give an amount > 0")
      return 0
   else:
      return withdraw
      

def main():
   card_no = login(Accounts)
   if not card_no:
      print("Invalid Card Number. Try Again")
      return False
   while True:
      print("1. Show Balance")
      print("2. Deposit")
      print("3. Withdraw")
      print("4. Exit")
      
      choice = input("Enter Your Choice(1-4): ")
      
      if choice == "1":
         balance = show_balance(card_no)
         print(f"\nCurrent Balance in Acc No. {card_no} is Rs. {balance}\n")
      elif choice == "2":
         debit = deposit()
         Accounts[card_no] += debit
         print(f"\nRs. {debit} deposited to Acc No. {card_no}\n")
      elif choice == "3":
         credit = withdraw(Accounts, card_no)
         Accounts[card_no] -= credit
         print(f"\nRs. {credit} withdrawn from Acc No. {card_no}\n")
      elif choice == "4":
         print("\nThank You!\n")
         break
      else:
         print("\nInvalid Choice. Choose between 1-4: ")

main()
      
      

"""
CURRENCY CONVERTER
Note: Here we returned function from another function. These are called closures
Step1: Create a function with input of current currency, target_currency, and the dictionary having rates of all currencies
Step2: Define another function taking input of the amount.
    --> Define the formula to convert the value from current currency to USD, then from USD to target currency
Step3: Initiate the outer function with current and target currency and store it in a variable
Step4: Run the variable as a function with the amount
"""

USD_RATES = {
    "USD": 1.000000,
    "EUR": 0.871172,
    "GBP": 0.749304,
    "INR": 95.799651,
    "AUD": 1.405890,
    "CAD": 1.399189,
    "SGD": 1.275659,
    "CHF": 0.824490,
    "MYR": 4.098430,
    "JPY": 155.862944,
    "CNY": 6.707185,
    "NZD": 1.744065,
}

def create_converter(from_currency, to_currency, ledger = USD_RATES):
   def convert(value):
      to_usd = value / ledger[from_currency]
      amount = round(to_usd * ledger[to_currency], 2)
      return amount
   return convert

currency_list = list(USD_RATES.keys())
while True:
   print("Type X to exit")
   from_ = input(f"From {currency_list} : ").strip().upper()
   to_ = input(f"To {currency_list} : ").strip().upper()

   if from_ in USD_RATES and to_ in USD_RATES:
      while True:
         print("Type 0 to exit")
         value = float(input("Enter Amount to convert: "))
         if value == 0:
            print("Exiting..")
            break
         converter = create_converter(from_, to_)
         amount = converter(value)
         print(f"Converted Amount: {amount} {to_}\n")
   
   elif from_ == 'X' or to_ == 'X':
      print("Thank You")
      break
   else:
      print("Invalid currency abbreviation.")
"""
EXPENSE TRACKER
"""

from datetime import datetime
expenses = [
    {
        "amount": 280,
        "category": "Food",
        "description": "Zomato Biryani order",
        "timestamp": datetime(2026, 8, 1, 21, 15, 0)
    },
    {
        "amount": 60,
        "category": "Food",
        "description": "Morning chai and local puff",
        "timestamp": datetime(2026, 8, 2, 8, 30, 0)
    },
    {
        "amount": 450,
        "category": "Transport",
        "description": "Rapido bike taxi to client meeting",
        "timestamp": datetime(2026, 8, 2, 11, 0, 0)
    },
    {
        "amount": 1200,
        "category": "Food",
        "description": "Weekend dinner with friends at a café",
        "timestamp": datetime(2026, 8, 2, 20, 45, 0)
    },
    {
        "amount": 150,
        "category": "Transport",
        "description": "Metro smart card recharge",
        "timestamp": datetime(2026, 8, 3, 9, 10, 0)
    },
    {
        "amount": 350,
        "category": "Food",
        "description": "Swiggy office lunch",
        "timestamp": datetime(2026, 8, 3, 13, 30, 0)
    },
    {
        "amount": 850,
        "category": "Groceries",
        "description": "Quick delivery fresh milk, eggs, and bread",
        "timestamp": datetime(2026, 8, 4, 7, 45, 0)
    },
    {
        "amount": 2200,
        "category": "Utilities",
        "description": "Monthly high-speed broadband bill",
        "timestamp": datetime(2026, 8, 5, 10, 0, 0)
    },
    {
        "amount": 500,
        "category": "Entertainment",
        "description": "OTT platform subscription renewal",
        "timestamp": datetime(2026, 8, 6, 15, 20, 0)
    },
    {
        "amount": 180,
        "category": "Food",
        "description": "Evening street food chaat",
        "timestamp": datetime(2026, 8, 7, 18, 30, 0)
    },
    {
        "amount": 650,
        "category": "Shopping",
        "description": "New t-shirt purchase from Myntra",
        "timestamp": datetime(2026, 8, 8, 14, 0, 0)
    },
    {
        "amount": 1500,
        "category": "Food",
        "description": "Sunday family brunch reservation",
        "timestamp": datetime(2026, 8, 9, 13, 0, 0)
    },
    {
        "amount": 400,
        "category": "Transport",
        "description": "Uber ride back home late night",
        "timestamp": datetime(2026, 8, 9, 23, 40, 0)
    },
    {
        "amount": 320,
        "category": "Food",
        "description": "Office cafeteria lunch thali",
        "timestamp": datetime(2026, 8, 10, 13, 15, 0)
    },
    {
        "amount": 2500,
        "category": "Health",
        "description": "Monthly gym membership fee",
        "timestamp": datetime(2026, 8, 11, 8, 0, 0)
    },
    {
        "amount": 950,
        "category": "Groceries",
        "description": "Weekly supermarket vegetable and fruit stock-up",
        "timestamp": datetime(2026, 8, 12, 19, 0, 0)
    },
    {
        "amount": 350,
        "category": "Transport",
        "description": "Auto rickshaw to railway station",
        "timestamp": datetime(2026, 8, 14, 18, 0, 0)
    },
    {
        "amount": 120,
        "category": "Food",
        "description": "Mid-day cold coffee",
        "timestamp": datetime(2026, 8, 14, 15, 30, 0)
    },
    {
        "amount": 1800,
        "category": "Entertainment",
        "description": "Weekend multiplex movie tickets and popcorn",
        "timestamp": datetime(2026, 8, 15, 19, 30, 0)
    },
    {
        "amount": 600,
        "category": "Food",
        "description": "Late-night pizza delivery",
        "timestamp": datetime(2026, 8, 16, 23, 10, 0)
    },
    {
        "amount": 200,
        "category": "Transport",
        "description": "Metro fare to workplace",
        "timestamp": datetime(2026, 8, 17, 9, 0, 0)
    },
    {
        "amount": 450,
        "category": "Food",
        "description": "Team lunch contribution",
        "timestamp": datetime(2026, 8, 18, 13, 30, 0)
    },
    {
        "amount": 1100,
        "category": "Utilities",
        "description": "Electricity bill payment",
        "timestamp": datetime(2026, 8, 20, 11, 45, 0)
    },
    {
        "amount": 3500,
        "category": "Shopping",
        "description": "New footwear purchase",
        "timestamp": datetime(2026, 8, 22, 16, 0, 0)
    },
    {
        "amount": 2400,
        "category": "Food",
        "description": "Fine dining dinner date on Saturday night",
        "timestamp": datetime(2026, 8, 22, 21, 0, 0)
    },
    {
        "amount": 500,
        "category": "Transport",
        "description": "Cab ride back from airport",
        "timestamp": datetime(2026, 8, 23, 22, 30, 0)
    },
    {
        "amount": 290,
        "category": "Food",
        "description": "Quick office snack and tea break",
        "timestamp": datetime(2026, 8, 25, 16, 30, 0)
    },
    {
        "amount": 750,
        "category": "Groceries",
        "description": "Instacart/Blinkit refill of household essentials",
        "timestamp": datetime(2026, 8, 26, 8, 15, 0)
    },
    {
        "amount": 1500,
        "category": "Entertainment",
        "description": "Concert ticket booking",
        "timestamp": datetime(2026, 8, 28, 12, 0, 0)
    },
    {
        "amount": 800,
        "category": "Food",
        "description": "Sunday evening rooftop dinner with family",
        "timestamp": datetime(2026, 8, 30, 20, 0, 0)
    }
]

def add_expense():
   amt = int(input("Amount: "))
   cat = input("Category: ")
   des = input("Description: ")
   expense = {
      "amount": amt,
      "category": cat,
      "description": des,
      "timestamp": datetime.now()
   }

   expenses.append(expense)
   print("Your expense is added.")
   return expenses


def view_expense(list):
   print(
      f"{'Amount':<8}"
      f"{'Category':<15}"
      f"{'Description':<50}"
      f"{'Timestamp':<6}"
   )
   print("-"*95)
   for expense in list:
      print(
      f"{expense['amount']:<8}"
      f"{expense['category']:<15}"
      f"{expense['description']:<50}"
      f"{expense['timestamp'].strftime("%d-%b-%y  %I-%M %p"):<6}"
   )


def filter_by_amount(list):
   min = int(input("Enter Lower Limit: "))
   max = int(input("Enter Upper Limit: "))
   filtered = [expense for expense in list if min < expense['amount'] < max]
   return filtered
   

def filter_by_category(list):
   cat = input("Enter category: ")
   filtered = [expense for expense in list if expense['category'] == cat]
   return filtered


def filter_by_date(list):
   from_date= input("Enter Start Date[dd-mm-yyyy]: ")
   start = datetime.strptime(from_date, "%d-%m-%Y")
   to_date = input("Enter End Date[dd-mm-yyyy]: ")
   end = datetime.strptime(to_date, "%d-%m-%Y")
   filtered = [expense for expense in list if start<= expense['timestamp'] <= end]
   return filtered

def filter_by_month(list):
   month_input = input("Enter Month and Year [Month, yyyy] (e.g. August, 2026): ")
   target_month = datetime.strptime(month_input, "%B, %Y")
   filtered = [
      expense for expense in list
      if expense['timestamp'].month == target_month.month
      and expense['timestamp'].year == target_month.year
   ]
   return filtered


def total_expense(list):
   total = 0
   for expense in list:
      total += expense['amount']
   return total


def highest(list, top):
   expense_sort = sorted(list, key= lambda x: x['amount'], reverse = True)
   top_x = expense_sort[:top]
   return top_x


def segregate_weekend(list):
   weekend = {"Saturday", "Sunday"}
   weekend_expense = []
   weekday_expense = []
   for expense in list:
      day = expense['timestamp'].strftime("%A")
      
      if day in weekend:
         weekend_expense.append(expense)
      else:
         weekday_expense.append(expense)
   return weekend_expense, weekday_expense


def weekend_vs_weekday(weekend, weekday):
   total_weekend = total_expense(weekend)
   total_weekday = total_expense(weekday)
   difference = total_weekend - total_weekday
   if total_weekend > total_weekday:
      return f"You spend {difference * (100/total_weekday)}% more in the weekends than weekdays."
   elif total_weekend < total_weekday:
      return f"You spend {-difference * (100/total_weekend)}% more in the weekdays than weekends."
   else:
      return "You spend equally in weekdays and weekends."


"""
def week_wise(filtered_month):
   week_expense = {}
   for expense in filtered_month:
      week = expense['timestamp'].strftime("%W")
      if week not in week_expense.keys():
         week_expense[week] = [expense]
      else:
         week_expense[week].append(expense)
   
   weekwise_expense = {}
   i = 1
   for week in week_expense.keys():
      week_i = "week" + str(i)
      weekwise_expense[week_i] = week_expense[week]
      i += 1
   return weekwise_expense

"""
def week_wise(filtered_month):
   week_expense = {}
   for expense in filtered_month:
      week = expense['timestamp'].strftime("%W")
      # setdefault handles the missing key check in one line
      week_expense.setdefault(week, []).append(expense)
   #Re-index the keys sequentially
   return {f"week{i}": expense for i, expense in enumerate(week_expense.values(), start = 1)}


def search_week(weekwise_expense):
   while True:
      week_no = int(input("Enter which week of the month do you want to search: "))
      week_ = "week" + str(week_no)
      if week_ in weekwise_expense.keys():
         view_expense(weekwise_expense[week_])
         break
      print("Week No. not available.")


def compare_weeks(weekwise_expense):
   weekwise_total = []
   print(
         f"{'Week':<8}"
         f"{'Total':<8}"
      )
   for week in weekwise_expense.keys():
      total = total_expense(weekwise_expense[week])
      weekwise_total.append((week, total))
   sorted_weeks = sorted(weekwise_total, key = lambda x: x[1], reverse = True)
   for week_, total in sorted_weeks:
      print(
         f"{week_:<8}"
         f"{total:<8}"
      )
 

def main():
   while True:
      print("1. Add Expense")
      print("2. View Expense")
      print("3. Filter Expenses")
      print("4. All total Expense")
      print("5. Highest Expense")
      print("6. Compare Weekend vs Weekdays")
      print("7. Week-wise comparison")
      print("8. Exit")
   
      option = int(input("ENTER OPTION [1-8]: "))
       
      if option == 1:
         add = add_expense()
         
      elif option == 2:
         print("\n=========================================== ALL EXPENSES ===========================================\n")
         view_expense(expenses)
         
      elif option == 3:
         print("\nFilter Options\n")
         while True:
            print("\n1. Filter By Category")
            print("2. Filter By Amount")
            print("3. Filter By Date")
            print("4. Filter By Month")
            print("5. Go Back\n")
            
            optionA = int(input("ENTER OPTION [1-5]: "))
            
            if optionA == 1:
               print("\n=========================================== Filtered Results ===========================================\n")
               filtered_category = filter_by_category(expenses)
               view_expense(filtered_category)
               while True:
                  print("\n1. Get Total Expenses")
                  print("2. Get Highest Expenses")
                  print("3. Go Back\n")
                  
                  optionB = int(input("ENTER OPTION [1-3]: "))
                  
                  if optionB == 1:
                     total = total_expense(filtered_category)
                     print(f"\nAll Over Total Expense: Rs.{total}/-")
         
                  elif optionB == 2:
                     x = int(input("Enter Top X expenses: "))
                     top_x = highest(filtered_category, x)
                     view_expense(top_x)
            
                  elif optionB == 3:
                     print("<--")
                     break

                  else:
                     print("Invalid. Try Again")

            elif optionA == 2:
               print("\n=========================================== Filtered Results ===========================================\n")
               filtered_amount = filter_by_amount(expenses)
               view_expense(filtered_amount)

            elif optionA == 3:
               print("\n=========================================== Filtered Results ===========================================\n")
               filtered_date = filter_by_date(expenses)
               view_expense(filtered_date)
               while True:
                  print("\n1. Get Total Expenses")
                  print("2. Get Highest Expenses")
                  print("3. Go Back\n")
                  
                  optionB = int(input("ENTER OPTION [1-3]: "))
                  
                  if optionB == 1:
                     total = total_expense(filtered_date)
                     print(f"\nAll Over Total Expense: Rs.{total}/-")
         
                  elif optionB == 2:
                     x = int(input("Enter Top X expenses: "))
                     top_x = highest(filtered_date, x)
                     view_expense(top_x)
            
                  elif optionB == 3:
                     print("<--")
                     break

                  else:
                     print("Invalid. Try Again")

            elif optionA == 4:
               print("\n=========================================== Filtered Results ===========================================\n")
               filtered_month = filter_by_month(expenses)
               view_expense(filtered_month)
               while True:
                  print("\n1. Get Total Expenses")
                  print("2. Get Highest Expenses")
                  print("3. Go Back\n")
                  
                  optionB = int(input("ENTER OPTION [1-3]: "))
                  
                  if optionB == 1:
                     total = total_expense(filtered_month)
                     print(f"\nAll Over Total Expense: Rs.{total}/-")
         
                  elif optionB == 2:
                     x = int(input("Enter Top X expenses: "))
                     top_x = highest(filtered_month, x)
                     view_expense(top_x)
            
                  elif optionB == 3:
                     print("<--")
                     break

                  else:
                     print("Invalid. Try Again")

            elif optionA == 5:
               print("<--")
               break
           
            else:
               print("Invalid. Try Again")           

         
      elif option == 4:
         total = total_expense(expenses)
         print(f"\nAll Over Total Expense: Rs.{total}/-")
         
      elif option == 5:
         x = int(input("Enter Top X expenses: "))
         top_x = highest(expenses, x)
         view_expense(top_x)
         
      elif option == 6:
         print("\nWeekend vs Weekday Expenses\n")
         weekend, weekday = segregate_weekend(expenses)
         while True:
            print("\n1. View All Weekend Expenses")
            print("2. View All Weekday Expenses")
            print("3. Compare Weekday and Weekend Expenses")
            print("4. Go Back\n")
            
            optionA = int(input("ENTER OPTION [1-4]: "))
            
            if optionA == 1:
               print("\n=========================================== WEEKEND EXPENSES ===========================================\n")
               view_expense(weekend)
        
               while True:
                  print("\n1. Total Weekend Expense")
                  print("2. Highest Weekend Expense")
                  print("3. Filter By Category")
                  print("4. Go Back\n")

                  optionB = int(input("ENTER OPTION [1-4]: "))

                  if optionB == 1:
                     total = total_expense(weekend)
                     print(f"\nAll Over Total Weekend Expense: Rs.{total}/-")
         
                  elif optionB == 2:
                     x = int(input("Enter Top X weekend expenses: "))
                     top_x = highest(weekend, x)
                     view_expense(top_x)

                  elif optionB == 3:
                     filtered_category = filter_by_category(weekend)
                     view_expense(filtered_category)

                  elif optionB == 4:
                     print("<--")
                     break
                     
                  else:
                    print("Invalid. Try Again")
               
            elif optionA == 2:
               print("\n=========================================== WEEKDAY EXPENSES ===========================================\n")
               view_expense(weekday)

               while True:
                  print("\n1. Total Weekday Expense")
                  print("2. Highest Weekday Expense")
                  print("3. Filter By Category")
                  print("4. Go Back\n")

                  optionB = int(input("ENTER OPTION [1-4]: "))

                  if optionB == 1:
                     total = total_expense(weekday)
                     print(f"\nAll Over Total Weekday Expense: Rs.{total}/-")
         
                  elif optionB == 2:
                     x = int(input("Enter Top X weekday expenses: "))
                     top_x = highest(weekday, x)
                     view_expense(top_x)

                  elif optionB == 3:
                     filtered_category = filter_by_category(weekday)
                     view_expense(filtered_category)

                  elif optionB == 4:
                     print("<--")
                     break

                  else:
                     print("Invalid. Try Again")

            elif optionA == 3:
               print(weekend_vs_weekday(weekend, weekday))

            elif optionA == 4:
               print("<--")
               break

            else:
               print("Invalid. Try Again")
               
      elif option == 7:
         print("\nWeek-wise Expenses\n")
         filtered_month = filter_by_month(expenses)
         weekwise_expense = week_wise(filtered_month)
         
         compare_weeks(weekwise_expense)
         while True:
            print("\n1. Search expenses with Week No.")
            print("2. Go Back\n")
            
            optionA = int(input("ENTER OPTION [1-2]: "))
            
            if optionA == 1:
               search_week(weekwise_expense)
           
            elif optionA == 2:
               print("<--")
               break
          
            else:
               print("Invalid. Try Again")

         
      elif option == 8:
         print("Thank You")
         break

      else:
         print("Invalid. Try Again")
   
main()
"""
Step11: Main
      --> Add Expense
      --> View Expense
      --> Filter
         --> Filter By Category
            --> Filter By Date
            --> Filter By Month
            --> Total Expense for Filtered result
            --> Top X Expensen for Filtered result
         --> Filter By Amount
         --> Filter By Date
            --> Total Expense for Filtered result
            --> Top X Expensen for Filtered result
         --> Filter By Month
            --> Total Expense for Filtered result
            --> Top X Expense for Filtered result
      --> Total Expense
      --> Top X Expense
      --> Compare Weekend vs Weekday
         --> View Weekend Expense
         --> View Weekday Expense
         --> Compare Weekday vs Weekend
      --> Compare Week-wise: Compare Total expenses of every week
         --> Search Week-wise

"""

from expensetracker import *

def main():
   while True:
      print("\n1. Add Expense")
      print("2. View Expense")
      print("3. Filter Expenses")
      print("4. All total Expense")
      print("5. Highest Expense")
      print("6. Compare Weekend vs Weekdays")
      print("7. Week-wise comparison")
      print("8. Exit\n")
   
      option = int(input("ENTER OPTION [1-8]: "))
       
      if option == 1:
         add_expense()
         
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
               filtered_category = filter_by_category(expenses)
               print("\n=========================================== Filtered Results ===========================================\n")
               view_expense(filtered_category)
               while True:
                  print("\n1. Filter By Amount")
                  print("2. Filter By Date")
                  print("3. Filter By Month")
                  print("4. Get Total Expenses")
                  print("5. Get Highest Expenses")
                  print("6. Go Back\n")
                  
                  optionB = int(input("ENTER OPTION [1-6]: "))

                  if optionB == 1:
                     filtered_amount = filter_by_amount(filtered_category)
                     print("\n=========================================== Filtered Results ===========================================\n")
                     view_expense(filtered_amount)

                  elif optionB == 2:
                     filtered_date = filter_by_date(filtered_category)
                     print("\n=========================================== Filtered Results ===========================================\n")
                     view_expense(filtered_date)

                  elif optionB == 3:
                     filtered_month = filter_by_month(filtered_category)
                     print("\n=========================================== Filtered Results ===========================================\n")
                     view_expense(filtered_month)

                  elif optionB == 4:
                     total = total_expense(filtered_category)
                     print(f"\nAll Over Total Expense for filtered category: Rs.{total}/-")
         
                  elif optionB == 5:
                     x = int(input("Enter Top X expenses for this category: "))
                     top_x = highest(filtered_category, x)
                     view_expense(top_x)
            
                  elif optionB == 6:
                     print("<--")
                     break

                  else:
                     print("Invalid. Try Again")

            elif optionA == 2:
               filtered_amount = filter_by_amount(expenses)
               print("\n=========================================== Filtered Results ===========================================\n")
               view_expense(filtered_amount)

            elif optionA == 3:
               filtered_date = filter_by_date(expenses)
               print("\n=========================================== Filtered Results ===========================================\n")
               view_expense(filtered_date)
               while True:
                  print("\n1. Get Total Expenses")
                  print("2. Get Highest Expenses")
                  print("3. Go Back\n")
                  
                  optionB = int(input("ENTER OPTION [1-3]: "))
                  
                  if optionB == 1:
                     total = total_expense(filtered_date)
                     print(f"\nAll Over Total Expense for Date range: Rs.{total}/-")
         
                  elif optionB == 2:
                     x = int(input("Enter Top X expenses for Date range: "))
                     top_x = highest(filtered_date, x)
                     view_expense(top_x)
            
                  elif optionB == 3:
                     print("<--")
                     break

                  else:
                     print("Invalid. Try Again")

            elif optionA == 4:
               filtered_month = filter_by_month(expenses)
               print("\n=========================================== Filtered Results ===========================================\n")
               view_expense(filtered_month)
               while True:
                  print("\n1. Get Total Expenses")
                  print("2. Get Highest Expenses")
                  print("3. Go Back\n")
                  
                  optionB = int(input("ENTER OPTION [1-3]: "))
                  
                  if optionB == 1:
                     total = total_expense(filtered_month)
                     print(f"\nAll Over Total Expense for this month: Rs.{total}/-")
         
                  elif optionB == 2:
                     x = int(input("Enter Top X expenses for the month: "))
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
         filtered_month = filter_by_month(expenses)
         print("\nWeek-wise Expenses\n")
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
   
if __name__ == '__main__':
   main()
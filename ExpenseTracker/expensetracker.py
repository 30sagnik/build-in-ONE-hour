"""
EXPENSE TRACKER
Step01: Create function to add expense in the expenses list. Use datetime.now to get the timestamp value.
Step02: Create function to view expense in tabular format.
Step03: Create functions to Filter By Amount, Filter By Category, Filter By Date, Filter By Month. Use List comprehension
Step04: Create function to get the total amount of the given list.
Step05: Create function to get input of the highest expense in the given list. Use sorted function with key as 'amount'.
Step06: Create function to segregate weekday expenses and weekend expenses.
Step07: Use the output of segregate function and create the compare function to compare expenses bwetween weekend and weekday.
Step08: Create function to get the week-wise expenses for the given month in a dictionary of lists.
Step09: Create function to search for the week from the week-wise function keys and get all the expenses of a particular week.
Step10: Create function to sort and compare the total expenses for every week of the month
*Step11: Create Main function for operation

"""

from datetime import datetime
from expenses import expenses

#Add Expense
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

#Display the given Expense list
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
      f"{expense['timestamp'].strftime('%d-%b-%y  %I:%M %p'):<6}"
   )

#Filter By Amount
def filter_by_amount(list):
   min = int(input("Enter Lower Limit: "))
   max = int(input("Enter Upper Limit: "))
   filtered = [expense for expense in list if min < expense['amount'] < max]
   return filtered
   
#Filter By Category
def filter_by_category(list):
   cat = input("Enter category: ")
   filtered = [expense for expense in list if expense['category'] == cat]
   return filtered

#Filter By Date
def filter_by_date(list):
   from_date= input("Enter Start Date[dd-mm-yyyy] (e.g. 27-08-2026): ")
   start = datetime.strptime(from_date, "%d-%m-%Y")
   to_date = input("Enter End Date[dd-mm-yyyy]: ")
   end = datetime.strptime(to_date, "%d-%m-%Y")
   filtered = [expense for expense in list if start<= expense['timestamp'] <= end]
   return filtered

#Filter By Month
def filter_by_month(list):
   month_input = input("Enter Month and Year [Month, yyyy] (e.g. August, 2026): ")
   target_month = datetime.strptime(month_input, "%B, %Y")
   filtered = [
      expense for expense in list
      if expense['timestamp'].month == target_month.month
      and expense['timestamp'].year == target_month.year
   ]
   return filtered

#Total Expense of given list
def total_expense(list):
   total = 0
   for expense in list:
      total += expense['amount']
   return total

#Highest X expenses of the given list
def highest(list, top):
   expense_sort = sorted(list, key= lambda x: x['amount'], reverse = True)
   top_x = expense_sort[:top]
   return top_x

#Segregate into weekend and weekday lists according to days
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

#Compare Weekend vs Weekday
def weekend_vs_weekday(weekend, weekday):
   total_weekend = total_expense(weekend)
   total_weekday = total_expense(weekday)
   difference = total_weekend - total_weekday
   if total_weekend > total_weekday:
      return f"You spend {round(difference * (100/total_weekday), 3)}% more in the weekends than weekdays."
   elif total_weekend < total_weekday:
      return f"You spend {round(-difference * (100/total_weekend), 3)}% more in the weekdays than weekends."
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
#Week-wise segregation of expenses for the given month
def week_wise(filtered_month):
   week_expense = {}
   for expense in filtered_month:
      week = expense['timestamp'].strftime("%W")
      # setdefault handles the missing key check in one line
      week_expense.setdefault(week, []).append(expense)
   #Re-index the keys sequentially
   return {f"Week {i}": exp_list for i, exp_list in enumerate(week_expense.values(), start = 1)}

#Search expenses for given week
def search_week(weekwise_expense):
   while True:
      week_no = int(input("Enter which week of the month do you want to search: "))
      week_ = "Week " + str(week_no)
      if week_ in weekwise_expense.keys():
         view_expense(weekwise_expense[week_])
         break
      print("Week No. not available.")

#Compare total expense week-wise
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
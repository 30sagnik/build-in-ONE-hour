"""
DATABASE QUERY BUILDER
Step1: Create the function with input of the table_name, *columns and **conditions
Step2: Add the SELECT clause and join the columns list with ", ". Save it in a string1
Step3: Add the FROM clause with the first input(table_name), save it in a string2
Step4: Create a blank string3. Start a loop to get the items of the conditions dictionary
    --> If the item(value) is a dictionary then get the values of the dictionary append it to a temporary list
    --> Add the clause of the conditions(item) and join the items in the temporary list with 'AND'.
    --> Add the whole string to string3
    --> If the item(value) is not a dictionary, then add the clause and the condition(value) to string3
Step5: Return string1 + string2 + string3
Step6: Test a query by inputing table_name, column names & conditions
"""

def query(table, *columns, **conditions):
   if not columns:
      string1 = "SELECT " + "*"
   else:
      string1 = "SELECT " + ', '.join(columns)
   string2 = "\nFROM " + table
   string3 = "\n"
   for clause, condition in conditions.items():
      if isinstance(condition, dict):
         string_list = []
         for item, value in condition.items():
             string_list.append(item + ' = ' + str(value))
         string3 += clause.replace("_", " ").upper() + ' ' + " AND ".join(string_list) + '\n'
      else:
         string3 += clause.replace("_", " ").upper() + ' ' +  str(condition) + '\n'
   return string1 + string2 + string3

#Test 1
test_1 = query("products", limit=5)
print("--- Test 1 ---")
print(test_1)

#Test 2
test_2 = query("employees", "name", "department", where="salary > 50000")
print("--- Test 2 ---")
print(test_2)

#Test 3
test_3 = query(
    "orders",
    "order_id",
    "total_amount",
    where={"status": "pending", "customer_id": 104},
    order_by="total_amount DESC"
)
print("--- Test 3 ---")
print(test_3)

#Test 4
test_4 = query(
    "sales",
    "region",
    group_by="region",
    having={"total_sales": 10000}
)
print("--- Test 4 ---")
print(test_4)

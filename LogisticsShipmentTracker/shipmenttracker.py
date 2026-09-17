"""
LOGISTICS SHIPMENT TRACKER
Step1: Create a display function. Loop over the list items and create nested loops on the dictionary keys.
     --> Add the dictionary values to a temporary string. Print after exiting the nested for loop
Step2: Create the filter status function to filter based on status i.e. Delivered, Delayed, etc
Step3: Create filter heavy shipments function to filter based on weight with input of a minimum weight
Step4: Create a filter expensive function to filter based on shipment price
Step5: Create filter functions to filter based on Origin location and Destination location
Step6: Create a function to map the cost_per_kg for each of the shipment records
Step7: Create a function to map the expected_delivery_date for each of the records using datetime module
Step8: Create a function and use reduce function to get total_shipment_cost
     --> Assign two variables total, shipments and add total with shipments[shipping_cost]. Return the total
Step9: Using the same strategy create a function to get the total_shipment_weight
     --> Assign 0 at the end which signifies that total is starting from 0. Initial value of accumulator
"""

from shipments import shipments
from datetime import datetime, timedelta
from functools import reduce


def display_shipments(shipments):
   print("-" * 120)
   titles = ""
   for title in shipments[0].keys():
      titles += (f"{title.capitalize():<15}")
   print(titles)
   print("-" * 120)
   for item in shipments:
      row = ""
      for key in item.keys():
         row += f"{item[key]:<15}"
      print(row)

# FILTER

def shipments_status(shipments, status = 'Delayed'):
   filtered = list(filter(lambda x: x['status'] == status, shipments))
   return filtered


def heavy_shipments(shipments, weight = 10):
   heavy = list(filter(lambda x: x['weight'] > weight, shipments))
   return heavy


def expensive_shipments(shipments, price = 1000):
   expensive = list(filter(lambda x: x['shipping_cost'] > price, shipments))
   return expensive


def shipments_ogn(shipments, ogn = 'Kolkata'):
   filtered_ogn = list(filter(lambda x: x['origin'] == ogn, shipments))
   return filtered_ogn

def shipments_des(shipments, des = 'Delhi'):
   filtered_des = list(filter(lambda x: x['destination'] == des, shipments))
   return filtered_des

#MAP

def cost_per_kg(shipments):
   per_kg = list(
      map(
         lambda x: {
            **x,
            "cost_per_kg": round(x['shipping_cost'] / x['weight'], 2)
         },
         shipments
      )
   )
   return per_kg


def delivery(shipments):
   expected_delivery = list(
      map(
         lambda x: {
            **x,
            "expctd_delivery": (datetime.strptime(x['shipment_date'], '%Y-%m-%d') + timedelta(days = x['delivery_days'])).strftime('%Y-%m-%d')
         }, shipments
      )
   )
   return expected_delivery

#REDUCE

def total_shipping_cost(shipments):
   total_cost = reduce(lambda total, shipment : total + shipment['shipping_cost'], shipments, 0)
   return total_cost

def total_shipment_weight(shipments):
   total_weight = reduce(lambda total, shipment: total + shipment['weight'], shipments, 0)
   return total_weight


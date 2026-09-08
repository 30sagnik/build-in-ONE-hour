"""
METRO PRICING ENGINE
#Step1: Create a dictionary of stations
#Step2: Convert the dictionary key into a list of stations
#Step3: Create the function to take user_input [Start, End] --> Check if start, end exist in stations list or not
     --> Check if start == end
     --> Get the start_index and end_index from the list of stations
#Step4: Create the distance function to calculate distance to travel. If start_index > end_index ---> Alter the variables
     --> Use loop to loop through the keys: value and add them to distance to get distance travelled
#Step5: Create the price function to use if/elif condition for various slab of distance and accordingly assign the price
"""

stations = {
    "Kavi Subhash": 0.0,
    "Shahid Khudiram": 0.9,
    "Kavi Nazrul": 1.2,
    "Gitanjali": 1.3,
    "Masterda Surya Sen": 1.0,
    "Netaji": 0.9,
    "Mahanayak Uttam Kumar": 1.2,
    "Rabindra Sarobar": 1.3,
    "Kalighat": 1.0,
    "Jatin Das Park": 0.8,
    "Netaji Bhavan": 0.9,
    "Rabindra Sadan": 1.0,
    "Maidan": 1.0,
    "Park Street": 0.8,
    "Esplanade": 0.8,
    "Chandni Chowk": 0.7,
    "Central": 0.6,
    "Mahatma Gandhi Road": 1.0,
    "Girish Park": 0.9,
    "Shobhabazar Sutanuti": 1.0,
    "Shyambazar": 1.2,
    "Belgachhia": 1.3,
    "Dum Dum": 2.2,
    "Noapara": 2.1,
    "Baranagar": 1.6,
    "Dakshineswar": 1.2,
}

stations_list = list(stations.keys())

print("\nWELCOME TO KOLKATA METRO\n")
stations_string = "  <===>  ".join(stations_list)
print(stations_string)

#Take user Input
def user_input():
   while True:
      start = input("From: ").strip().title()
      end = input("To: ").strip().title()
      if start not in stations_list or end not in stations_list:
         print("Station not found. Enter a valid station name.")
         continue
      if start == end:
         print("Departure and Arrival Stations cannot be same")
         continue
      start_index = stations_list.index(start)
      end_index = stations_list.index(end)
      return start_index, end_index

#Measure the distance between arriving and departed station
def distance_engine(start_idx, end_idx):
   if start_idx > end_idx:
      start_idx, end_idx = end_idx, start_idx
   total_dist = 0
   for i in range(start_idx + 1, end_idx + 1):
      distance = stations[stations_list[i]]
      total_dist += distance
   return round(total_dist, 3)

#Calculate the ticket price according to the distance slab
def price_engine(distance):
   if distance < 2:
      ticket = 5
   elif 2 <= distance < 5:
      ticket = 10
   elif 5 <= distance < 10:
      ticket = 15
   elif 10 <= distance < 15:
      ticket = 20
   elif 15 <= distance < 20:
      ticket = 25
   else:
      ticket = 30
   return ticket


start_idx, end_idx = user_input()
distance = distance_engine(start_idx, end_idx)
ticket_price = price_engine(distance)

print("\n----------------------")

print(f"Distance: {distance} km")
print(f"Ticket Price: Rs. {ticket_price}")

print("----------------------")
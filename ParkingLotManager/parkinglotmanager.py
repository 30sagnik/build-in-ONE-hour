"""
PARKING LOT MANAGER
"""

from datetime import datetime

class Vehicle:
   def __init__(self, vehicle_no, owner_name, vehicle_type):
      self.vehicle_no = vehicle_no
      self.owner_name = owner_name
      self.vehicle_type = vehicle_type

class ParkingSlot:
   def __init__(self, slot_no, vehicle = None):
      self.slot_no = slot_no
      self.vehicle = vehicle

   def is_available(self):
      return self.vehicle == None

   def park_vehicle(self, vehicle):
      if not self.is_available():
         print(f"Slot {self.slot_no} is already occupied")
      else:
         self.vehicle = vehicle
         print(f"Vehicle No. {self.vehicle.vehicle_no} is parked in Slot {self.slot_no}")         

   def remove_vehicle(self):
      if not self.is_available():
         print(f"Vehicle No. {self.vehicle.vehicle_no} is removed from Slot {self.slot_no}")
         self.vehicle = None
      else:
         print(f"Slot {self.slot_no} is already empty")

class Ticket:
   def __init__(self, ticket_id, vehicle, slot, entry_time):
      self.ticket_id = ticket_id
      self.vehicle = vehicle
      self.slot = slot
      self.entry_time = entry_time

   def show_ticket(self):
      print("--------------PARKING TICKET----------------")
      print(f"Ticket ID         : {self.ticket_id}")
      print(f"Vehicle No        : {self.vehicle.vehicle_no}")
      print(f"Owner             : {self.vehicle.owner_name}")
      print(f"Vehicle Type      : {self.vehicle.vehicle_type}")
      print(f"Slot No           : {self.slot.slot_no}")
      print(f"Entry Time        : {self.entry_time}")

class ParkingLot:
   def __init__(self):
      self.name = 'City Centre Parking'
      self.slots = []
      self.tickets = {}
      self.next_ticketid = 1001

   def create_slots(self, count):
      for i in range(1, count+1):
         self.slots.append(ParkingSlot(i))

   def park_vehicle(self, vehicle):
      # Find a Free Slot
      for slot in self.slots:
         if slot.is_available():
            # Park the vehicle
            slot.park_vehicle(vehicle)
        
            # Generate ticket ID
            ticket_id = self.next_ticketid
            self.next_ticketid += 1

            # Create the ticket
            ticket = Ticket(ticket_id, vehicle, slot, datetime.now())
            
            # Store the ticket
            self.tickets[ticket_id] = ticket

            return ticket

      print("Parking Lot is full")
      return None

   def find_vehicle(self, vehicle_no):
      for slot in self.slots:
         if slot.vehicle is not None:
            if slot.vehicle.vehicle_no == vehicle_no:
               print(f"Slot: {slot.slot_no}")
               return slot.vehicle, slot
      return None, None

   def remove_vehicle(self, ticket_id):
      if ticket_id not in self.tickets:
         print("Invalid Ticket ID")
         return

      ticket = self.tickets[ticket_id]
      ticket.slot.remove_vehicle()

      del self.tickets[ticket_id]

   def display_status(self):
      for slot in self.slots:
         if slot.is_available():
            print(f"Slot {slot.slot_no}: EMPTY")
         else:
            vehicle = slot.vehicle
            print(f"Slot {slot.slot_no}: {vehicle.vehicle_no} | {vehicle.vehicle_type}")
           

lot = ParkingLot()
lot.create_slots(4)

car = Vehicle("WB02AB1234", "Sagnik", "Car")
ticket1 = lot.park_vehicle(car)
lot.display_status()

ticket1.show_ticket()

car2 = Vehicle("WB02BB2222", "Rahul", "Bike")
ticket2 = lot.park_vehicle(car2)
ticket2.show_ticket()

lot.find_vehicle("WB01AA1111")

lot.display_status()

lot.remove_vehicle(ticket1.ticket_id)
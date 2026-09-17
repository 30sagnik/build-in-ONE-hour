"""
MAIN: To operate shipmenttracker.py
"""

from shipmenttracker import *

def main():

    while True:
        print("\n" + "=" * 50)
        print("       LOGISTICS SHIPMENT TRACKER")
        print("=" * 50)

        print("1. Display All Shipments")
        print("2. Filter Shipments by Status")
        print("3. Find Heavy Shipments")
        print("4. Find Expensive Shipments")
        print("5. Filter by Origin")
        print("6. Filter by Destination")
        print("7. Calculate Cost per Kg")
        print("8. Calculate Expected Delivery Date")
        print("9. Calculate Total Shipping Cost")
        print("10. Calculate Total Shipment Weight")
        print("0. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            display_shipments(shipments)

        elif choice == "2":
            status = input(
                "Enter status (Delivered/In Transit/Delayed/Cancelled): "
            )

            result = shipments_status(shipments, status)
            display_shipments(result)

        elif choice == "3":
            weight = float(input("Enter minimum weight: "))

            result = heavy_shipments(shipments, weight)
            display_shipments(result)

        elif choice == "4":
            price = float(input("Enter minimum shipping cost: "))

            result = expensive_shipments(shipments, price)
            display_shipments(result)

        elif choice == "5":
            origin = input("Enter origin city: ")

            result = shipments_ogn(shipments, origin)
            display_shipments(result)

        elif choice == "6":
            destination = input("Enter destination city: ")

            result = shipments_des(shipments, destination)
            display_shipments(result)

        elif choice == "7":
            result = cost_per_kg(shipments)
            display_shipments(result)

        elif choice == "8":
            result = delivery(shipments)
            display_shipments(result)

        elif choice == "9":
            result = total_shipping_cost(shipments)
            print(f"\nTotal Shipping Cost: Rs.{result}/-")

        elif choice == "10":
            result = total_shipment_weight(shipments)
            print(f"\nTotal Shipment Weight: {result} kg")

        elif choice == "0":
            print("\nExiting Logistics Shipment Tracker...")
            break

        else:
            print("\nInvalid choice. Please try again.")

main()
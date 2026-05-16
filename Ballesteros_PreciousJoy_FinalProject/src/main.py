from manager import RentalSystem

def main():
    sys = RentalSystem()
    
    while True:
        print("\n--- ECORIDE BIKE RENTAL ---")
        print("1. View Bikes")
        print("2. Rent Bike")
        print("3. Return Bike")
        print("4. Add Bike (Admin)")
        print("5. Exit")
        
        choice = input("Select Option: ")

        if choice == "1":
            print(f"\n{'ID':<5} {'Brand':<15} {'Type':<10} {'Rate':<8} {'Status'}")
            for b in sys.inventory:
                stat = "Available" if b.available else "Rented"
                print(f"{b.bike_id:<5} {b.brand:<15} {b.bike_type:<10} P{b.rate:<7} {stat}")

        elif choice == "2":
            bid = input("Enter Bike ID to rent: ")
            bike = sys.find_bike(bid)
            # THE BASE CASE: Check if bike exists and is available
            if bike and bike.available:
                bike.available = False
                sys.save_to_file()
                print(f"Success! {bike.brand} is now yours.")
            else:
                print("Error: Bike not found or already rented.")

        elif choice == "3":
            bid = input("Enter Bike ID to return: ")
            bike = sys.find_bike(bid)
            if bike and not bike.available:
                hours = float(input("Hours used: "))
                print(f"Total Bill: P{hours * bike.rate:.2f}")
                bike.available = True
                sys.save_to_file()
                print("Return processed successfully.")
            else:
                print("Error: Transaction invalid.")

        elif choice == "4":
            bid = input("ID: ")
            br = input("Brand: ")
            tp = input("Type: ")
            rt = input("Rate: ")
            from models import Bike
            sys.inventory.append(Bike(bid, br, tp, rt))
            sys.save_to_file()
            print("Stock updated.")

        elif choice == "5":
            print("System offline. Goodbye!")
            break
vehicle_rates = {
    'ECONOMY': 10,
    'PREMIUM': 18,
    'SUV': 25
}
ride_history = []

def calculate_fare(distance_km, vehicle_type, travel_hour):
    try:
        if vehicle_type not in vehicle_rates:
            return None, "Service Not Available"
        rate_per_km = vehicle_rates[vehicle_type]
        base_fare = distance_km * rate_per_km
        surge_multiplier = 1
        if 17 <= travel_hour <= 20:
            surge_multiplier = 1.5
        total_fare = base_fare * surge_multiplier
        ride_data = {
            "distance": distance_km,
            "vehicle": vehicle_type,
            "rate": rate_per_km,
            "hour": travel_hour,
            "base_fare": base_fare,
            "surge": surge_multiplier,
            "total": total_fare
        }
        return ride_data, None
    except Exception as e:
        return None, str(e)
    
def save_receipt_to_file(ride):
    try:
        with open("ride_receipt.txt", "a", encoding="utf-8") as file:
            file.write("\n Ride Receipt \n")
            file.write(f"Distance : {ride['distance']} km\n")
            file.write(f"Vehicle  : {ride['vehicle']}\n")
            file.write(f"Rate/km  : {ride['rate']}\n")
            file.write(f"Hour     : {ride['hour']}\n")
            file.write(f"Base Fare: {ride['base_fare']:.2f}\n")

            if ride['surge'] > 1:
                file.write(f"Surge    : Yes ({ride['surge']}x)\n")
            else:
                file.write("Surge    : No\n")

            file.write(f"Total    : {ride['total']:.2f}\n")

    except Exception as e:
        print("Error saving receipt:", e)
        
def main():
    print(" Welcome to CityCab Fare Calculator ")
    try:
        distance_km = float(input("Enter distance (in km): "))
        vehicle_type = input("Enter vehicle type (Economy / Premium / SUV): ").strip().upper()
        travel_hour = int(input("Enter hour of travel (0-23): "))
        result, error = calculate_fare(distance_km, vehicle_type, travel_hour)
        if error:
            print("\n", error)
            return
        ride_history.append(result)
        print("\n Ride Estimate Receipt ")
        print(f"Distance Travelled : {result['distance']} km")
        print(f"Vehicle Type       : {result['vehicle']}")
        print(f"Rate per km        : {result['rate']}")
        print(f"Travel Hour        : {result['hour']}")
        print(f"Base Fare          : {result['base_fare']:.2f}")
        if result['surge'] > 1:
            print(f"Surge Applied      : Yes ({result['surge']}x)")
        else:
            print("Surge Applied      : No")
        print(f"Total Fare         : {result['total']:.2f}")
        save_receipt_to_file(result)
        print("\n--- Ride History ---")
        for i, ride in enumerate(ride_history, start=1):
            print(f"{i}. {ride['vehicle']} | {ride['distance']} km | {ride['total']:.2f}")
    except ValueError:
        print("\n Invalid input! Please enter correct values.")
    except Exception as e:
        print("\n Unexpected Error:", e)

if __name__ == "__main__":
    main()

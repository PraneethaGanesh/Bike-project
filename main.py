# main.py

from bike import Bike

def main():
    my_bike = Bike("Jawa 42 Bobber", 60)

    while True:
        initial_input = input(f"Do you want to ride the {my_bike.model}, check status, or exit? (ride/status/exit): ").strip().lower()

        if initial_input == 'ride':
            while my_bike.performance <= 50:
                print(f"Sorry, the {my_bike.model} has {my_bike.performance} performance left, it needs above 50 to ride!")
                repair_or_exit = input("Do you want to repair or exit? (repair/exit): ").strip().lower()
                if repair_or_exit == 'repair':
                    repair_type = input("Enter repair type (tyre/oil/handling/brake/engine): ").strip().lower()
                    my_bike.repair(repair_type)
                elif repair_or_exit == 'exit':
                    return
                else:
                    print("Invalid input. Please type 'repair' or 'exit'.")
            
            ride_type = input("Enter ride type (city/highway/offroad): ").strip().lower()
            speed = int(input("At what speed (kmph) do you want to ride? ").strip())
            duration = float(input("For how long (in hours) do you want to ride? ").strip())
            if my_bike.ride(ride_type, speed, duration):
                print("Ride is completed.")
                while my_bike.speed > 0:
                    ride_brake = input("Do you want to increase speed or put brake? (speed/brake): ").strip().lower()
                    if ride_brake == 'speed':
                        speed = int(input("At what additional speed (kmph) do you want to ride? ").strip())
                        my_bike.speed += speed
                        print(f"Speed increased to {my_bike.speed} kmph.")
                    elif ride_brake == 'brake':
                        brake_pe = float(input("By what percentage do you want to reduce the speed? (0 to 100): ").strip())
                        if not my_bike.brake(brake_pe):
                            break
                    else:
                        print("Invalid input. Please type 'speed' or 'brake'.")
        elif initial_input == 'status':
            my_bike.status()
        elif initial_input == 'exit':
            break
        else:
            print("Invalid input. Please type 'ride', 'status', or 'exit'.")
            continue
        
        while True:
            user_input = input(f"Do you want to ride, repair, refuel, check status, or exit? (ride/repair/refuel/status/exit): ").strip().lower()

            if user_input == 'ride':
                if my_bike.performance > 50:
                    ride_type = input("Enter ride type (city/highway/offroad): ").strip().lower()
                    speed = int(input("At what speed (kmph) do you want to ride? ").strip())
                    duration = float(input("For how long (in hours) do you want to ride? ").strip())
                    if my_bike.ride(ride_type, speed, duration):
                        print("Ride is completed.")
                        while my_bike.speed > 0:
                            ride_brake = input("Do you want to increase speed or put brake? (speed/brake): ").strip().lower()
                            if ride_brake == 'speed':
                                speed = int(input("At what additional speed (kmph) do you want to ride? ").strip())
                                my_bike.speed += speed
                                print(f"Speed increased to {my_bike.speed} kmph.")
                            elif ride_brake == 'brake':
                                brake_pe = float(input("By what percentage do you want to reduce the speed? (0 to 100): ").strip())
                                if not my_bike.brake(brake_pe):
                                    break
                            else:
                                print("Invalid input. Please type 'speed' or 'brake'.")
                else:
                    print(f"Sorry, the {my_bike.model} has {my_bike.performance} performance left, it needs above 50 to ride!")
            elif user_input == 'repair':
                repair_type = input("Enter repair type (tyre/oil/handling/brake/engine): ").strip().lower()
                my_bike.repair(repair_type)
            elif user_input == 'refuel':
                amount = float(input("Enter the amount of fuel to add (percentage): ").strip())
                my_bike.refuel(amount)
            elif user_input == 'status':
                my_bike.status()
            elif user_input == 'exit':
                return
            else:
                print("Invalid input. Please type 'ride', 'repair', 'refuel', 'status', or 'exit'.")

if __name__ == "__main__":
    main()

# bike.py
class Bike:
    def __init__(self, model, performance, speed=0, brake_condition=100, fuel=100):
        self.model = model
        self.performance = performance
        self.speed = speed
        self.brake_condition = brake_condition
        self.fuel = fuel
    
    def ride(self, ride_type, speed, duration):
        if self.brake_condition <= 0:
            print(f"Cannot ride. The brakes of {self.model} are in bad condition and need repair.")
            return False
        if self.fuel <= 0:
            print(f"Cannot ride. The {self.model} has no fuel and needs refueling.")
            return False

        ride_effects = {
            "city": (10, 15, 20),  # (performance, brake condition, fuel)
            "highway": (20, 10, 20),
            "offroad": (30, 15, 30)
        }

        if ride_type in ride_effects:
            distance_traveled = speed * duration  
            performance_reduction, brake_reduction, fuel_reduction = ride_effects[ride_type]

            self.performance -= performance_reduction * duration
            self.brake_condition -= (brake_reduction / 100) * self.brake_condition * duration
            self.fuel -= fuel_reduction * duration

            if self.performance < 0:
                self.performance = 0
            if self.brake_condition < 0:
                self.brake_condition = 0
            if self.fuel < 0:
                self.fuel = 0

            self.speed = speed
            print(f"{self.model} was ridden {ride_type} at {speed} kmph for {duration} hours, covering {distance_traveled} km.")
            print(f"Now has {self.performance} performance, {self.brake_condition:.2f}% brake condition, and {self.fuel}% fuel left.")
            return True
        else:
            print("Invalid ride type.")
            return False

    def brake(self, reduction_percentage):
        if reduction_percentage >= 100:
            self.speed = 0
            print(f"Braking at {reduction_percentage}%... {self.model} has stopped.")
            print("The ride has ended.")
            return False  # End the ride
        else:
            reduction_amount = self.speed * (reduction_percentage / 100)
            self.speed -= reduction_amount
            if self.speed < 0:
                self.speed = 0
            print(f"Braking... {self.model} is now going at {self.speed:.2f} kmph.")
            if self.speed == 0:
                print("Your bike has stopped.")
                print("The ride has ended.")
                return False  # End the ride
        return True  # Continue the ride

    def repair(self, repair_type):
        repair_effects = {
            "tyre": (5, 20),  # (performance increase, brake condition increase)
            "oil": (10, 10),
            "handling": (15, 15),
            "brake": (0, 50),
            "engine": (20, 0)
        }

        if repair_type in repair_effects:
            self.performance += repair_effects[repair_type][0]
            self.brake_condition += repair_effects[repair_type][1]
            if self.performance > 100:
                self.performance = 100
            if self.brake_condition > 100:
                self.brake_condition = 100
            print(f"Repaired {repair_type}. Now, the performance is {self.performance} and brake condition is {self.brake_condition}%.")
        else:
            print("Invalid repair type.")

    def refuel(self, amount):
        self.fuel += amount
        if self.fuel > 100:
            self.fuel = 100
        print(f"Refueled {amount}%. Now, the bike has {self.fuel}% fuel.")

    def status(self):
        print(f"Bike Status - Model: {self.model}, Performance: {self.performance}, Speed: {self.speed} kmph, Brake Condition: {self.brake_condition:.2f}%, Fuel: {self.fuel}%")

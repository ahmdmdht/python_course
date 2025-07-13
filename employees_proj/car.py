class Car:

    def __init__(self, name, fuelRate, velocity):
        self.name = name
        self.set_fuel_rate(fuelRate)
        self.set_velocity(velocity)

    def run(self, distance, velocity):
        self.set_velocity(velocity)
        distance_per_unit_fuel = 10
        max_distance = self.fuelRate * distance_per_unit_fuel

        if distance <= max_distance:
            self.fuelRate -= distance / distance_per_unit_fuel
            self.stop(0)
        else:
            self.fuelRate = 0
            remaining_distance = distance - max_distance
            self.stop(remaining_distance)

    def stop(self, remainingDistance):
        self.velocity = 0
        if remainingDistance == 0:
            print("Arrived at destination.")
        elif remainingDistance > 0:
            print(f"You haven't arrived yet.\n{remainingDistance} km left.")

    def set_fuel_rate(self, value):
        if value >= 100:
            self.fuelRate = 100
        elif value <= 0:
            self.fuelRate = 0
        else:
            self.fuelRate = value

    def get_fuel_rate(self):
        return self.fuelRate

    def set_velocity(self, value):
        if value >= 200:
            self.velocity = 200
        elif value <= 0:
            self.velocity = 0
        else:
            self.velocity = value

    def get_velocity(self):
        return self.velocity

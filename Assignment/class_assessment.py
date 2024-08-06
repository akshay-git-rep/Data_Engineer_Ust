class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

    def fare(self, seating_capacity):
        return seating_capacity * 100

class Bus(Vehicle):
    def fare(self, seating_capacity):
        total_fare = super().fare(seating_capacity)
        maintenance_charge = total_fare * 0.10
        return total_fare + maintenance_charge

# Example usage:
bus = Bus(80, 15)
print(f"Max Speed: {bus.max_speed} km/h")
print(f"Mileage: {bus.mileage} km/l")
print(f"Total Fare: ₹{bus.fare(50)}")


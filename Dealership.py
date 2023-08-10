# Initial vehicle class
class Vehicle:
    def __init__(self, make, miles, price):
        self.make = make
        self.miles = miles
        self.price = price
        self.engine_on = False
    
    def start_engine(self):
        print("All push to start now. doesnt feel as good as a turn key but she roars all the same")
        self.engine_on = True
    
    def make_noise(self):
        print("*Obnoxious Honk*")

# Derived Truck Class
class Truck(Vehicle):
    def __init__(self, make, miles, price):
        Vehicle.__init__(self, make, miles, price)
        self.cargo = False
    
    def load_cargo(self):
        print("Hang on, let me get the boys to load the bed.")
        self.cargo = True

# Derived Motorcycle Class
class Motorcycle(Vehicle):
    def __init__(self, make, miles, price, top_speed):
        Vehicle.__init__(self, make, miles, price)
        self.top_speed = top_speed
    
    def make_noise(self):
        print("VROOOOOOOOOOOOOOOM *something tells you that you'll hurt yourself on this bike*")

# area to list choices
bikes = []
trucks = []

# Create instances of each subclass
bikes.append(Motorcycle("Harley-Davidson", 10000, 8000, 150))
bikes.append(Motorcycle("Yamaha", 5000, 6000, 180))
bikes.append(Motorcycle("Honda", 2000, 7500, 160))

trucks.append(Truck("Ford", 30000, 25000))
trucks.append(Truck("Chevrolet", 25000, 28000))
trucks.append(Truck("Toyota", 20000, 30000))

# List to store selected vehicles for comparison that I dont think I did correctly 
vehicles_to_compare = # [  empty whereas the users input is expected ]

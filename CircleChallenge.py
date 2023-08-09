import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_diameter(self):
        return self.radius * 2
    
    def calculate_circumfrence(self):
        return 2 * math.pi * self.radius
    
    def calculate_area(self):
        return math.pi * (self.radius ** 2)
    
    def grow(self):
        self.radius *= 2

    def get_radius(self):
        return self.radius

def main():
    while True:
        try:
            radius = float(input("Enter how big you would like the initial radius: "))
        except ValueError:
            print("*ahem* A radius is typically measured in numbers.")
            continue

        circle = Circle(radius)

        print("Diameter:", circle.calculate_diameter())
        print("Circumfrence:", circle.calculate_circumfrence())
        print("Area:", circle.calculate_area())

        choice = input("Would you like the circle to grow? (yes/no) ")
        if choice == 'yes':
            print("Sure, sure. Just sign here, intial here, sign here...")
            circle.grow()
        else:
            print("Very well. Enjoy the rest of the day.")
            print("Final radius:", circle.get_radius())
            break


if __name__  == "__main__":
    main()
class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def display_details(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Color: {self.color}")

    def update_color(self, new_color):
        self.color = new_color
# Creating three different car objects
car1 = Car("Toyota", "Corolla", 2020, "Red")
car2 = Car("Honda", "Civic", 2021, "Black")
car3 = Car("Ford", "Mustang", 2019, "Yellow")

# Display details of each car
print("Car 1 Details:")
car1.display_details()

print("\nCar 2 Details:")
car2.display_details()

print("\nCar 3 Details:")
car3.display_details()

# Update the color of the first car and display updated details
car1.update_color("Blue")
print("\nUpdated Car 1 Details:")
car1.display_details()
# Prompt user for car details
make = input("Enter the make of the car: ")
model = input("Enter the model of the car: ")
year = int(input("Enter the year of the car: "))
color = input("Enter the color of the car: ")

# Create a new Car object using user input
user_car = Car(make, model, year, color)

# Display the details of the newly created car
print("\nUser Car Details:")
user_car.display_details()

 

'''Code explanation

The code defines a class named Car with the following attributes:

- make: the car's manufacturer

- model: the car's model

- year: the car's year of manufacture

- color: the car's color

The class has two methods:

- __init__: initializes a new Car object with the given attributes

- display_details: prints the car's details

- update_color: updates the car's color

Creating Car Objects

The code creates three Car objects: car1, car2, and car3, with different attributes.

Displaying Car Details

The code displays the details of each car using the display_details method.

Updating Car Color

The code updates the color of car1 to "Blue" using the update_color method and displays the updated details.

User Input

The code prompts the user to enter the make, model, year, and color of a car, creates a new Car object with the user's input, and displays the details of the newly created car.

In summary, this code defines a Car class, creates car objects, displays their details, updates a car's color, and creates a new car object based on user input.
'''
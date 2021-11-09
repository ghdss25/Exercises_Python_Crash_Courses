## 9-9. Battery Upgrade: Use the final version of electric_car.py from this section.
## Add a method to the Battery class called upgrade_battery(). This method
## should check the battery size and set the capacity to 100 if it isn’t already.
## Make an electric car with a default battery size, call get_range() once, and
## then call get_range() a second time after upgrading the battery. You should
## see an increase in the car’s range.

class Car:

    def __init__(self, name_car, score, manufactor, color, year):

        self.name_car = name_car.title()
        self.score = score
        self.manufactor = manufactor.title()
        self.color = color
        self.year = year
        self.odometer_reading = 0 

    def data_car(self):

        msg_name_car = "The car is: " + self.name_car
        msg_score = "The score of car it has: " + self.score
        msg_manufactor = "The manufactor of car is " + self.manufactor

        print(msg_name_car)
        print(msg_score)
        print(msg_manufactor) 

    def data_style(self):

        msg_color = "The color is: " + self.color
        msg_year = "The year is of Car: " + self.year

        print(msg_color)
        print(msg_year)

    def read_odometer(self):

        print(f"This car has {self.odometer_reading} miles on it")

    def update_odometer(self, mileage):

        if mileage >= self.odometer_reading:

            self.odometer_reading = mileage

        else:

            print("You can't roll back an odometer !")

    def increment_odometer(self, miles):

        self.odometer_reading += miles

class Eletric_Car(Car):

    def __init__(self, name_car, score, manufactor, color, year):

        super().__init__(name_car, score, manufactor, color, year)

        self.battery = Battery()

class Battery():

    def __init__(self, battery = 75):

        self.battery = battery

    def upgrade_battery(self):

        print(f"This car has a {self.battery} - Kwh battery. ")

    def get_range(self):

        if self.battery == 75:

            range = 350

        elif self.battery == 100:

            range = 345

        print(f"this car can go about {range} miles on a full charge")

my_tesla = Eletric_Car('Logan', '12764-18763', 'Renault', 'white', '2015')

print(my_tesla.data_car())
print(my_tesla.data_style())

my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()
        

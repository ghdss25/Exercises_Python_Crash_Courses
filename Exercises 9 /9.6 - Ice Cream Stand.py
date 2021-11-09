## 9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write
## a class called IceCreamStand that inherits from the Restaurant class you wrote
## in Exercise 9-1 (page 162) or Exercise 9-4 (page 167). Either version of
## the class will work; just pick the one you like better. Add an attribute called
## flavors that stores a list of ice cream flavors. Write a method that displays
## these flavors. Create an instance of IceCreamStand, and call this method.

class Restaurant:

      def __init__(self, name, cuisine_type):

            self.name = name.title()
            self.cuisine_type = cuisine_type

      def describe_name(self):

            msg = self.name + " is a Restaurant "
            print(msg)

      def describe_type(self):

            msg1 = self.cuisine_type + " is a Ice Cream"
            print(msg1)

restaurant = Restaurant('Atlanta', 'Flavors')

class IceCreamStand(Restaurant):

      def __init__(self, name, cuisine_type = 'Ice cream'):

            super().__init__(name, cuisine_type)

            self.flavors = []

      print("Welcome of a list of Ice Cream")

      def show_restaurant(self):

            for flavor in self.flavors:
      
                  print(" " + flavor.title())

big_one = IceCreamStand('Flavors', 'IceCream')
big_one.flavors = ['Strawberry', 'Vanilla', 'Chocolate']

big_one.describe_name()
big_one.show_restaurant()

from re import Restaurant 

my_restaurant = restaurant.Restaurant('Dominos', 'pizza')
print(my_restaurant.describe_name())

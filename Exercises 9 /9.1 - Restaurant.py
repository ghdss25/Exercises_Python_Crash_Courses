## Make a class called Restaurant. The __init__() method for
## Restaurant should store two attributes: a restaurant_name and a cuisine_type.
## Make a method called describe_restaurant() that prints these two pieces of
## information, and a method called open_restaurant() that prints a message indicating that the restaurant is open

## Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods

class Restaurant():

      def __init__(self, name, cuisine_type):

            self.name = name.title()
            self.cuisine_type = cuisine_type

      def describe_restaurant(self):

            msg = self.name + "name of restaurant" + "with the variables types of " + self.cuisine_type
            print(msg)

      def open_restaurant(self):

            msg = self.name + "is name of place that's person going"
            print(msg)

restaurant = Restaurant('Dominos', 'Pizza')

print(restaurant.name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()

            



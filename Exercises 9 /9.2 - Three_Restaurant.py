## Start with your class from Exercise 9-1. Create three
## different instances from the class, and call describe_restaurant() for each
## instance.

class Restaurant():

      def __init__(self, name, cuisine_typical):

            self.name = name.title()
            self.cuisine_typical = cuisine_typical

      def describe_restaurant(self):

            msg = self.name + "is restaurant of: " + self.cuisine_typical
            print(msg)

      def operations_restaurants(self):

            msg = "The it's open for the public food: " + self.cuisine_typical
            print(msg)

restaurant = Restaurant('Pizza Atlanta', 'Pizzas')
print(restaurant.name)
print(restaurant.cuisine_typical)

restaurant.describe_restaurant()
restaurant.operations_restaurants()

print("")

class Restaurant1():

      restaurant = Restaurant("Dominós", "Pizzas")

      msg = f"The restaurant {restaurant.name} it's open today tonight"
      print(msg)

      msg1 = f"My favorite food is {restaurant.cuisine_typical} of calabrease"
      print(msg1)

print("")
      
class Restaurant2():

      restaurant = Restaurant('Brazetus', "Pizzas")

      msg2 = f"The {restaurant.name} is a good place for food want flavor of pizzas: "
      print(msg2)

      msg3 = f"The {restaurant.name} have much {restaurant.cuisine_typical} of flavors of pizzas no Recife"
      print(msg3)



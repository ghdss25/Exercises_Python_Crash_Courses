## 9 -10. Imported Restaurant: Using your latest Restaurant class, store it in a module.
## Make a separate file that imports Restaurant. Make a Restaurant instance,
## and call one of Restaurant’s methods
## to show that the import statement is working properly.

class Restaurant:

      def __init__(self, name, custion_type):

            self.name = name.title()
            self.custion_type = custion_type.title()

      def describe_name(self):

            msg1 = "The name of Restaurant is: " + self.name
            print(msg1)

      def describe_type(self):

            msg2 = "The type of Restaurant is: " + self.custion_type
            print(msg2)


from restaurant import Restaurant

my_restaurant = Restaurant('Dominos', 'Pizzaria')

my_restaurant.describe_name()
my_restaurant.describe_type()

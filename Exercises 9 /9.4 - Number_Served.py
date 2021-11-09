## Start with your program from Exercise 9-1 (page 162).
## Add an attribute called number_served with a default value of 0. Create an
## instance called restaurant from this class. Print the number of customers the
## restaurant has served, and then change this value and print it again.
## Add a method called set_number_served() that lets you set the number
## of customers that have been served. Call this method with a new number and
## print the value again.
## Add a method called increment_number_served() that lets you increment
## the number of customers who’ve been served.
## Call this method with any number you like that could represent how many customers were served in, say, a
## day of business.

class Restaurant():

      def __init__(self, name, cuisine_type):

            self.name = name.title()
            self.cuisine_type = cuisine_type.title()
            self.number_served = 0 

      def describe_restaurants(self):

            msg = "The Restaurant is: " + self.name
            print(msg)

      def operations_restaurants(self):

            msg = "The type of Restaurant is: " + self.cuisine_type
            print(msg)

      def set_number_served(self, number_served):

            self.number_served = number_served
            print("Number of customers that have been served: ", str(self.number_served))

      def increment_number_served(self, add_number_server):

            self.number_served += add_number_server
            print("Summation of customers that have been served: ", str(self.number_served))
            

restaurant = Restaurant('Dominos', 'Pizza')

restaurant.describe_restaurants()
restaurant.operations_restaurants()
restaurant.set_number_served(234)
restaurant.set_number_served(342)
restaurant.increment_number_served(321)


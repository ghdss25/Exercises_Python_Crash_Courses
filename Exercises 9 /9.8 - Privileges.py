## Write a separate Privileges class. The class should have one
## attribute, privileges, that stores a list of strings as described in Exercise 9-7.
## Move the show_privileges() method to this class. Make a Privileges instance
## as an attribute in the Admin class. Create a new instance of Admin and use your
## method to show its privileges.

class User:

      def __init__(self, name, email, state, city, year):

            self.name = name.title()
            self.email = email.title()
            self.state = state
            self.city = city
            self.year = year

      def data_person(self):

            msg_name = "My name is: " + self.name
            msg_email = "My email is: " + self.email

            print(msg_name)
            print(msg_email)

      def data_location(self):

            msg_state = "My state is: " + self.state
            msg_city = "My city is: " + self.city

            print(msg_state)
            print(msg_city)

      def data_year(self):

            msg_year = "My Year is: " + self.year
            print(msg_year)

class Admin(User):

      def __init__(self, name, email, state, city, year):

            super().__init__(name, email, state, city, year)

            self.privileges = Privileges()

class Privileges():

      def __init__(self, privileges = []):

            self.privileges = privileges

      def show_describe(self):

            if self.privileges:

                  for privilege in self.privileges:

                        print(" The Privileges so:  " + privilege)

            else:

                  print("Privileges")

gustavo = Admin('Gustavo Henrique', 'gustavotinho@gmail.com', 'Pernambuco', 'Recife', '1991')

gustavo.data_person()
gustavo.data_location()
gustavo.data_year()

gustavo.privileges.show_describe()

gustavo_privileges = ['Add User', 'Deleting User', 'Update User']

gustavo.privileges.privileges = gustavo_privileges

gustavo.privileges.show_describe()

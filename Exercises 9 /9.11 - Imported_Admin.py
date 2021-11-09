## 9-11. Imported Admin: Start with your work from Exercise 9-8 (page 173).
## Store the classes User, Privileges, and Admin in one module.
## Create a separate file, make an Admin instance, and call show_privileges() to show that
## everything is working correctly.

class User:

      def __init__(self, name, email, place, state, city):

            self.name = name.title()
            self.email = email.title()
            self.place = place
            self.state = state
            self.city = city

      def describe_person(self):

            msg_name = "My name is: " + self.name
            msg_email = "My email is: " + self.email

            print(msg_name)
            print(msg_email)

      def describe_live(self):

            msg_state = "My state is: " + self.state
            msg_city = "My city is: " + self.city
            msg_place = "My favorite place is: " + self.place

            print(msg_state)
            print(msg_city)
            print(msg_place)

class Admin(User):

      def __init__(self, name, email, place, state, city):

            super().__init__(name, email, place, state,city)

            self.privileges = Privileges()

class Privileges():

      def __init__(self, privileges = []):

            self.privileges = privileges

      def show_describe(self):

            if self.privileges:

                  for privilege in self.privileges:

                        print("The Privilege is: " + privilege)

                  else:

                        print("Show Privileges")

gustavo = Admin('Gustavo Henrique', 'gustavotinho@gmail.com', 'Pernambuco', 'Recife', '1991')

gustavo.describe_person()
gustavo.describe_live()

gustavo.privileges.show_describe()

gustavo_privileges = ['Add User', 'Deleting User', 'Update User']

gustavo.privileges.privileges = gustavo_privileges

gustavo.privileges.show_describe()

## 9-12. Multiple Modules: Store the User class in one module, and store the
## Privileges and Admin classes in a separate module. In a separate file, create
## an Admin instance and call show_privileges() to show that everything is still
## working correctly

class User:

      def __init__(self, name, email, place, state, city):

            self.name = name.title()
            self.email = email.title()
            self.place = place
            self.state = state
            self.city = city

      def describe_user(self):

            msg_name = " My name is: " + self.name
            msg_email = "My email is: " + self.email

            print(msg_name)
            print(msg_email)

      def describe_world(self):

            msg_place = "My place is: " + self.place
            msg_state = "My state is: " + self.state
            msg_city = "My city is: " + self.city

            print(msg_place)
            print(msg_state)
            print(msg_city)



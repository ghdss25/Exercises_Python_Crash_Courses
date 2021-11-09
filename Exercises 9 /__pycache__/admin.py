from mm import MultipleModules

class Admin(User):

      def __init__(self, name, email, place, state, city):

            super().__init__(name, email, place, state, city)

            self.privilieges = Privileges()

class Privileges:

      def __init__(self, privileges = []):

            self.privileges = privileges

      def show_describe(self):

            if self.privileges:

                  for privilege in self.privileges:

                        print(" " + privilege)

                  else:

                        print("I don't privilege")

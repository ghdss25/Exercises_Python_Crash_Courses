## 9-7. Admin: An administrator is a special kind of user. Write a class called
## Admin that inherits from the User class you wrote in Exercise 9-3 (page 162)
## or Exercise 9-5 (page 167). Add an attribute, privileges, that stores a list
## of strings like "can add post", "can delete post", "can ban user", and so on.
## Write a method called show_privileges() that lists the administrator’s set of
## privileges. Create an instance of Admin, and call your method.

class User:

      def __init__(self, name, email, cpf, place, state):

            self.name = name.title()
            self.email = email.title()
            self.cpf = cpf
            self.place = place.title()
            self.state = state.title()

      def data_user(self):

            msg_name = "My name is: " + self.name
            msg_email = "My email is: " + self.email
            msg_cpf = "My cpf is: " + self.cpf

            print(" \n " + msg_name)
            print(" \n " + msg_email)
            print(" \n " + msg_cpf) 

      def data_world(self):

            msg_place = " I'm living on place of : " + self.place
            msg_state = " My state is: " + self.state

user = User('Doni', 'doni@gmail.com', '019809823', 'Recife', 'Pernambuco')

user.data_user()
user.data_world()

class Admin(User):

      def __init__(self, name, email, cpf, place, state):

            super().__init__(name, email, cpf, place, state)

            self.privilleges = [ ]

      def show_privilleges(self):

            for privillege in self.privilleges:

                  print(" " + privillege.title())

gustavo = Admin('Gustavo', 'gustavotinho@gmail.com', '90283109', 'Recife', 'Pernambuco')
gustavo.privilleges = ['Add Post', 'Ban Post', 'Deleting the Post is a User']

gustavo.data_user()
gustavo.show_privilleges()
            



                  

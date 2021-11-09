## Add an attribute called login_attempts to your User
## class from Exercise 9-3 (page 162). Write a method called increment_login
## _attempts() that increments the value of login_attempts by 1. Write another
## method called reset_login_attempts() that resets the value of login_attempts
## to 0. Make an instance of the User class and call increment_login_attempts()
## several times. Print the value of login_attempts to make sure it was incremented
## properly, and then call reset_login_attempts(). Print login_attempts again to
## make sure it was reset to 0.

class User():

      def __init__(self, first_name, last_name, email):

            self.first_name = first_name.title()
            self.last_name = last_name.title()
            self.email = email
            self.login_attempts = 0

      def describe_person(self):

            msg_name = " My name is: " + self.first_name + " " +self.last_name
            msg_email = " My email is: " + self.email

            print(msg_name)
            print(msg_email)

      def increment_login_attempts(self):

            self.login_attempts += 1

      def reset_login_attempts(self):

            self.login_attempts = 0 
            
user = User('Gustavo', 'Henrique', 'gustavotinho@gmail.com')

user.describe_person()

## calling the method increment_login_attempts several times

user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

print("Access of User is of: ", str(user.login_attempts))

## Priting the method reset_login_attempts of User
user.reset_login_attempts()
print("Access of User is of: ", str(user.login_attempts))

## 9-3. Users: Make a class called User. Create two attributes called first_name
## and last_name, and then create several other attributes that are typically stored
## in a user profile. Make a method called describe_user() that prints a summary
## of the user’s information. Make another method called greet_user() that prints
## a personalized greeting to the user.
## Create several instances representing different users, and call both methods
## for each user.

class User():

      def __init__(self, first_name, last_name, city, country, marital_status): 

            self.first_name = first_name.title()
            self.last_name = last_name.title()
            self.city = city
            self.country = country
            self.marital_status = marital_status

      def greet_user(self):

            msg = "You're welcome " + self.first_name + " " + self.last_name + " to the our systems, these are data on system: "
            print(msg)

      def describe_user(self):

            msg_name = "My name is: " + self.first_name + " " + self.last_name
            print(msg_name)

            msg_city = "I'm of : " + self.city
            print(msg_city)

            msg_country = "I was born on: " + self.country
            print(msg_country)

            msg_marital_status = "My marital status is: " + self.marital_status
            print(msg_marital_status)

user = User('Gustavo', 'Henrique', 'Recife', 'Brazil', 'not married')
print(user.first_name)
print(user.last_name)
print(user.city)
print(user.country)
print(user.marital_status)

user.greet_user()
user.describe_user()

print("")
print("Second User: ")

user1 = User('Doni', 'Souza', 'Recife', 'Brazil', 'serious relationship')
print(user1.first_name)
print(user1.last_name)
print(user1.city)
print(user1.country)
print(user1.marital_status)

user1.greet_user()
user1.describe_user()

print("")
print("Third User: ")

class User2:

      user2 = User('Gustavsson', 'Silv','Estomcolbo', 'Sweden', 'not married')

      name = f"My name is {user2.first_name} and {user2.last_name}"
      print(name)

      city = f"My city is {user2.city}"
      print(city)

      country = f"My country is {user2.country}"
      print(country)

      material_status = f"I'm {user2.marital_status}"
      print(material_status)



## 5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is not empty

## If the list is empty, print the message We need to find some users !

## Remove all of the usernames from your list, and make sure the correct message is printed.

list_users = []

if list_users != ' ':

      print("We need to find some users")

else:

      print("User on the list")


list_admin = ['Gustavo', 'Henrique']

print("Removing of the list ", list_admin.pop(0))

print(list_admin)

del list_admin[0]

print("Printed the removal from elements of list Users ", list_admin)

print("We need to find some users")

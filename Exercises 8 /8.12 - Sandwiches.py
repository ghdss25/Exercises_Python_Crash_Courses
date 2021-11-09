## Write a function that accepts a list of items a person wants
## on a sandwich. The function should have one parameter that collects as many
## items as the function call provides, and it should print a summary of the sandwich that’s being ordered.
## Call the function three times, using a different number of arguments each time.

list_sandwich = ['break', 'cheese', 'tomates', 'peppiline', 'beef']
list_sandwich2 = ['break', 'cheese', 'onion', 'ketchup', 'beef', 'presunt']
list_sandwich3 = ['Maionese', 'ketchup', 'mustard', 'chocolate', 'banana'] 

def items_sandwich(*first_list):

      print(first_list)

items_sandwich(list_sandwich)

def items_flavor(*second_list):

      print(second_list)

items_flavor(list_sandwich2)

def items_options(*third_sandwich):

      print(third_sandwich)

items_options(list_sandwich3)


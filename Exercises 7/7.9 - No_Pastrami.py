## 7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure
## the sandwich 'pastrami' appears in the list at least three times.

##Add code near the beginning of your program to print a message saying the deli has
## run out of pastrami, and then use a while loop to remove all occurrences of
## 'pastrami' from sandwich_orders.

## Make sure no pastrami sandwiches end up in finished_sandwiches

sandwich_orders = ['Crazy Meat Sandwich', 'Generous ham sandwich', 'Roast beef sandwich', 'Sandwich Pastrami']
finished_sandwiches = []
finished_sandwiches = sandwich_orders

print("saying the deli has run out of pastrami: ", finished_sandwiches[3])

while 'Sandwich Pastrami' in sandwich_orders:

      print("Removing of list Sandwich Orders: ", sandwich_orders.pop(3))
      print(finished_sandwiches)



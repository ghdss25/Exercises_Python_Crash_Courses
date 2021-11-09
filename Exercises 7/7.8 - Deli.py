## Make a list called sandwich_orders and fill it with the names of various sandwiches.
## Then make an empty list called finished_sandwiches.
## Loop through the list of sandwich orders and print a message for each order, such
## as I made your tuna sandwich. As each sandwich is made, move it to the list
## of finished sandwiches. After all the sandwiches have been made, print a
## message listing each sandwich that was made.

sandwich_orders = ['Crazy Meat Sandwich', 'Generous ham sandwich', 'Roast beef sandwich']
finished_sandwiches = []
finished_sandwiches = sandwich_orders

while sandwich_orders:

      for s in sandwich_orders:
            
             print("List of sandwiches: ", s)
            
      break

print("")

print("Listing the sandwich that was made: ")

print("fisrt sandwich: ", finished_sandwiches[0])
print("second sandwich: ", finished_sandwiches[2])

print("")

print("Sandwich not listing: ")
print("fisrt sandwich: ", finished_sandwiches[1])

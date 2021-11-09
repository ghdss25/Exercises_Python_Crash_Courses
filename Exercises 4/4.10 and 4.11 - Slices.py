## 4-10. Slices: Using one of the programs you wrote in this chapter, add several
## lines to the end of the program that do the following:

## Print the message The first three items in the list are:. Then use a slice to
## print the first three items from that program’s list.

sports = ['play soccer', 'voleyball', 'basketball', 'hungby', 'football american', 'athletics',
          'handeball', '']

print(" The first three items in the list are ", sports[:3])

print("")

## Print the message Three items from the middle of the list are:. Use a slice to
## print three items from the middle of the list.

print("Three items from the middle of the list are: ", sports[3:])

## Print the message The last three items in the list are:. Use a slice to print the
## last three items in the list.

print("Three items from the middle of the list are: ", sports[4:])

## 4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1
## (page 56). Make a copy of the list of pizzas, and call it friend_pizzas.
## Then, do the following:

## Add a new pizza to the original list.

print("What's your favorite pizzas? ")
pizzas = ['pepperoni', 'four cheeses', 'ham', 'beef']
print(pizzas.append('bananas'))
print(pizzas)

print("What's your favorite pizzas? ")
friend_pizzas = ['Romeu and Julieta', 'mozzarella', 'chocolate', 'Margherita']
print(friend_pizzas.append('calabrease'))
print(friend_pizzas)

print("")
## Prove that you have two separate lists.
print("Prove", pizzas[:2])
print("Prove two: ", pizzas[2:])

print("Prove", friend_pizzas[:2])
print("Prove two: ", friend_pizzas[2:])

print()
## Print the message My favorite pizzas are:, and then use a for loop to print the first list
print("My favorite pizzas are: ")

for p in pizzas:

      print(p)

print("")

## Print the message My friend’s favorite pizzas are:

print("My friend’s favorite pizzas are")

## and then use a for loop to print the second list

for f in friend_pizzas:

      print("", f)

print("")
## Make sure each new pizza is stored in the appropriate list.

print("My Pizzas is stored in the apropriate are: ", pizzas[:4])
print("Pizzas of my friends in the apropriate are: ", friend_pizzas[:4])

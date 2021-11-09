## Write a loop that prompts the user to enter a series of
## pizza toppings until they enter a 'quit' value. As they enter each topping,
## print a message saying you’ll add that topping to their pizza.

print("Here have many topping of pizza: ")
print("1 - Mozzarella")
print("2 - Calabreasse")
print("3 - Four Cheeses")
print("4 - Pizza Ham")
print("5 - Romeu and Julieta")

while True:

      topping_pizza = int(input("Report the your topping of pizza: "))

      if topping_pizza == 1:

            print("Mozzarella")
            print("saying you’ll add that topping to their pizza.")

      if topping_pizza == 2:

            print("Calabreasse")
            print("saying you’ll add that topping to their pizza.")

      if topping_pizza == 3:

            print("Four Cheeses")
            print("saying you’ll add that topping to their pizza.")

      if topping_pizza == 4:

            print("Pizza Ham")
            print("saying you’ll add that topping to their pizza.")

      if topping_pizza == 5:

            print("Romeu and Julieta")
            print("saying you’ll add that topping to their pizza.")

      if topping_pizza == 6:
      
            print("exit")
            break

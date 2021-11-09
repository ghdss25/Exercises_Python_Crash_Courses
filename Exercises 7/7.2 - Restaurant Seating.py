
print("Report the size of pizzas: ")
print("1 - size of slices eight pizzas: ")
print("2 - size of slices four pizzas: ")

slices_eight = 1
slices_four = 2

option_slices = int(input("Selected the option of pizzas: "))

if option_slices == 1:

      print("Selected the flavors of pizzas: ")

      first_pizza = input("Report the first flavors: ")
      second_pizza = input("Report the second flavors: ")
      third_pizza = input("Report the third flavors: ")
      four_pizza = input("Report the four flavors: ")
      five_pizza = input("Report the five flavor: ")
      six_pizza = input("Report the six flavor: ")
      seven_pizza = input("Report the seven flavor:")
      eight_pizza = input("Report the eight flavor")

      flavors = [first_pizza, second_pizza, third_pizza, four_pizza, five_pizza, six_pizza, seven_pizza, eight_pizza]

      flavors.sort()
      print(flavors)
      
elif option_slices == 2:

      flavors = {

            'first person' : {

                  'Name' : 'Gustavo',
                  'flavor' : 'Marguerita',
            },

            'second person' : {
                  'Name' : 'Henrique',
                  'flavor' : 'Ham', 
            },

            'third person' : {

                  'Name' : 'Oliveira',
                  'flavor' : 'Loin', 
            },

            'four person' : {

                  'Name' : 'Jessica',
                  'flavor' : 'Portuguese', 
            },

      }

for f, data in flavors.items() :

      print("\n flavors: {f}")

      name = f"\t{data['Name']}"
      flavor = f"\t{data['flavor']}"

      print("name of people: ", name)
      print("flavor of pizza: " , flavor)
      
      

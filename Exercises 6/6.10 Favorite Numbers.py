## Modify your program from Exercise 6-2 (page 99) so each person
## can have more than one favorite number.
## Then print each person’s name along with their favorite numbers.

favorites_numbers = {
      
            'first person' : {

                        'name' : 'Gustavo Henrique',
                        'favorite numbers' : 'thirty',
                  },

            'second person' : {
                  
                        'name' : 'Doni Souza',
                        'favorite numbers' : 'twente - nine', 
                  },

              'thirty person' : {

                        'name' : 'Mary Taylor',
                        'favorite numbers' : 'fifteen - seven',
                    },

              'four person' : {

                        'name' : 'Tatiana do Amaral',
                        'favorite numbers' : 'sixty - eight',
                    },
      }

for fn, data in favorites_numbers.items():

      print(f"\n name persons: {fn}")

      name = f"\t{data['name']}"
      numbers = f"\t{data['favorite numbers']}"

      print(f"\t Name: " + name.title())
      print(f"\t numbers: " + numbers.title())


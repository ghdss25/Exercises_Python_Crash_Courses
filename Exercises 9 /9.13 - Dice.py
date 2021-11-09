## 9-13. Dice: Make a class Die with one attribute called sides, which has a default
## value of 6. Write a method called roll_die() that prints a random number
## between 1 and the number of sides the die has. Make a 6-sided die and roll it 10 times.
## Make a 10-sided die and a 20-sided die. Roll each die 10 times.

from random import randint

class Die:
      
      def roll_die():

            nl = 6
            nl1 = 10
            nl2 = 20

            numero = randint(1, nl)

            print("number of sides the die has: ", numero)

            print("\nMake a 6-slided die and roll it 10: ")
            
            for nl in range(1, 10):
                  
                  dado6 = randint(1, 6)

                  print("Number of side: ", [dado6])

            print("\nMake a 10 - slide: ")

            for nl1 in range(1, 10):

                  dado10 = randint(1, nl1)

                  print("Number of side: ", [dado10])


            print("\nMake a 20 - slide: ")

            for nl2 in range(1, 10):

                  dado20 = randint(1, 20)

                  print("Number of side: ", [dado20])

           
          
      roll_die()


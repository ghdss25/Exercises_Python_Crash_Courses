## 5-5. Alien Colors: Turn your if-else chain from Exercise 5-4 into an if-elifelse chain.

## If the alien is green, print a message that the player earned 5 points.
## If the alien is yellow, print a message that the player earned 10 points.
## If the alien is red, print a message that the player earned 15 points.

allen_colors = ('green', 'yellow', 'red')

request = input("What's your favorite color: ")

if request == 'yellow':

      print("that the player earned 10 points")

elif request == 'green':

      print('that the player earned 5 points')

elif request == 'red':

      print('that the player earned 15 points')

## Write three versions of this program, making sure each message is printed for the appropriate color alien.

version1 = ('red', 'yellow', 'green')
version2 = ('black', 'blue', 'white')
version3 = ('pink', 'brown', 'grey')

request1 = input("Request your first favorite colors: ")
request2 = input("Request your second favorite colors: ")
request3 = input("Request your third favorite colors: ")

if (request1 == 'green') and (request2 == 'blue') and (request3 == 'pink') :

      print("That the player earned 45 points")

elif (request2 == 'red') and (request3 == 'white') and (request1 == 'black') :

      print("That the player earned 78 points")

elif (request3 == 'brown') and (request2 == 'black') and (request1 == 'yellow'):

      print("That the player earned 98 points")

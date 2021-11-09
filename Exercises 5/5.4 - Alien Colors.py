## 5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3, and
## write an if-else chain

print("If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien.")

allen_color = ('green', 'blue', 'black')

request = input("What's your favorite color: ")

if request == 'green':

      print("5 points for shooting the allen")

elif request == 'blue':

      print("3 points for shooting the allen")

elif request == 'black':

      print("1 points for shooting the allen")

else:

      print("Nothing")

print("")
print("")

print ("If the alien’s color isn’t green, print a statement that the player just earned 10 points")

allen_color = ('green', 'blue', 'black')

request = input("What's your favorite color: ")

if request != 'green':

      print("10 points for shooting the allen")

print("")
print("")

print("Write one version of this program that runs the if block and another that runs the else block")

allen_color = ('white', 'yellow', 'red')

request = input("Request your favorite color on list")

if request == 'white':

      print("You have 34 points, it's on my time is Manchester United")

elif request == 'yellow':

      print("You have 50 points, It's on my time is Nantes")

else:
      
      print("Nothing points, You are not have nothing time")

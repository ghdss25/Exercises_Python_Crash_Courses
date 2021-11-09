## 5-3. Alien Colors #1: Imagine an alien was just shot down in a game. Create a
## variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.

## Write an if statement to test whether the alien’s color is green. If it is, print
## a message that the player just earned 5 points.

print("Report your color: ")
print("1 green")
print("2 yellow")
print("3 red")

alien_color = int(input("What's your favorite color: "))

option_green = 1
option_yellow = 2
option_red = 3

if alien_color == 1:

      print(1)
      print("Congratulations people you selected is color green, that player just earned 5 points ")

elif alien_color == 2:

      print(2)
      print("it lost")


elif allen_color == 3:

      print(3)
      print("You have 2 points")

print("")
print("")

## Write one version of this program that passes the if test and another that
## fails. (The version that fails will have no output.)

allen_color = ['green', 'blue', 'black']

report = (input("Report your favorite color: "))

if report == 'green':

      print("You have five points")

elif report == 'blue':

      print("failure on color blue")
      
elif report == 'black':

      print("You have nothing")

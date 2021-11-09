## 7-6. Three Exits: Write different versions of either Exercise 7-4 or Exercise 7-5
## that do each of the following at least once:

## Use a conditional test in the while statement to stop the loop.
## Use an active variable to control how long the loop runs.
## Use a break statement to exit the loop when the user enters a 'quit' value.

import time

while True:
      
      number = int(input("Report the number: "))

      if number == 0:

            print("exit")
            break

      elif number >= 1:

            for n in range(number, 501):

                  print(n)
                  time.sleep(1)

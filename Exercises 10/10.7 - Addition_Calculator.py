## 10-7. Addition Calculator: Wrap your code from Exercise 10-6 in a while loop
## so the user can continue entering numbers even if they make a mistake and
## enter text instead of a number.

while True:

      try:

            number1 = int(input("Selected the first number: "))
            number2 = int(input("Selected the second number: "))

            addition = number1 + number2 


      except ValueError:

            print("You can't write letters on form")

      else:

            print(addition)

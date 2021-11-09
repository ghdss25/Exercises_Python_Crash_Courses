## 10-11. Favorite Number: Write a program that prompts for the user’s favorite
## number. Use json.dump() to store this number in a file.
## Write a separate program that reads in this value and prints the message,
## “I know your favorite
## number! It’s _____.”

import json

number = int(input("What's your favorite number: "))

with open('json/number_favorite.json', 'w') as f:

      json.dump(number, f)
      print("Thank you by number favorite. ")



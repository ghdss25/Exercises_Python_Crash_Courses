import json

with open('txt/number_favorite.json') as f:

      number = json.load(f)

      print("I know your favorite number! It's " + str(number))

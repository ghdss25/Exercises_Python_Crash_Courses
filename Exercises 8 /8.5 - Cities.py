## 8-5. Cities: Write a function called describe_city() that accepts the name of
## a city and its country. The function should print a simple sentence, such as
## Reykjavik is in Iceland. Give the parameter for the country a default value.
## Call your function for three different cities, at least one of which is not in the
## default country

def describe_city(country , city = "London"):

      menssage = " The city " + city.title() + " it isn't of " + country
      print(menssage)

describe_city("Spanish")
describe_city("Nerthelands")
describe_city("Germany")

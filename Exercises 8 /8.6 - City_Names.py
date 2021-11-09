## 8-6. City Names: Write a function called city_country() that takes in the name
## of a city and its country. The function should return a string formatted like this:

## Call your function with at least three city-country pairs, and print the
## values that are returned.

def city_country(city, country):

      data = f"{city} {country}"
      return data.title()

finish = city_country('Santigo', 'Chile')
finish1 = city_country('Armstedam', 'Netherlands')
finish2 = city_country('Bratislav', 'Hungria')

print("The Country and City with captions are: ")
print("Country and City is: ", finish)
print("Country and City is: ", finish1)
print("Country and City is: ", finish2)

      

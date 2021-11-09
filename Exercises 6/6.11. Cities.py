## Make a dictionary called cities. Use the names of three cities as keys in your dictionary.
## Create a dictionary of information about each city and
## include the country that the city is in, its approximate population, and one fact
## about that city. The keys for each city’s dictionary should be something like
## country, population, and fact. Print the name of each city and all of the information you have stored about it.

data_city = {

            'Manchester' : {

                  'country' : 'England',
                  'population' : '553.230',
                  'fact' : 'city cultural activites',
            },

            'Recife' : {

                  'country' : 'Brazil',
                  'population' : '1,555 milão',
                  'fact' : 'city of Carnival',
            },

             'Milão' : {

                  'country' : 'Italy',
                  'population' : '1,352 milão',
                  'fact' : 'city fashion',
            },

            'Barcelona' : {

                  'country' : 'Italy',
                  'population' : '1,352 milão',
                  'fact' : 'city cultural of museum',
            },

             'Miami' : {

                  'country' : 'EUA',
                  'population' : '2,5 milhões',
                  'fact' : 'city of beach',
            },
      }

for dc, data in data_city.items():

      print(f"\n city: {dc}")

      country = f"\t{data['country']}"
      population = f"\t{data['population']}"
      fact = f"\t{data['fact']}"

      print(f"\t Country: " + country.title())
      print(f"\t Population: " + population.title())
      print(f"\t Fact: " + fact.title())

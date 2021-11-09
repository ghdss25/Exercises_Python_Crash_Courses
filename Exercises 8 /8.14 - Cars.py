## Write a function that stores information about a car in a dictionary. The function should always receive a manufacturer and a model name. It
## should then accept an arbitrary number of keyword arguments. Call the function with the required information and two other name-value pairs, such as a
## color or an optional feature. Your function should work for a call like this one:

def data_cars(manufacturer, model_name, **user_info):

      cars = {

            'manufacturer' : manufacturer.title(),
            'Model Name' : model_name.title(), 
      }

      for ca, data in user_info.items():

            cars['ca'] = data

      return user_info

profile = data_cars('Civic', 'Honda', location = 'United States', year = 2003, situacion = True)
profile1 = data_cars('Skyline', 'Booster', location = 'England', year = 2009, situacion = True)
profile2 = data_cars('Fuska', 'Ristrom', location = 'New Zeland', year = 2014, situacion = True)

print(profile)
print(profile1)
print(profile2)

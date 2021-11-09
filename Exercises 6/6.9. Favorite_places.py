## Favorite Places: Make a dictionary called favorite_places. Think of three
## names to use as keys in the dictionary, and store one to three favorite places
## for each person. To make this exercise a bit more interesting, ask some friends
## to name a few of their favorite places. Loop through the dictionary, and print
## each person’s name and their favorite places

favorite_place = {
      
            'Data of Person' : {

                  'Name' : 'Gustavo Henrique',
                  'Age' : '30 years old',
                  'City' : 'Recife',
                  'State' : 'Pernambuco',
                  'District' : 'Cordeiro',
                  'Favorite Place' : 'Shopping Recife',    
            },
      }

for fp, data in favorite_place.items():

      print(f"\t {fp}")

      name = f"\t{data['Name']}"
      city = f"\t{data['City']}"
      state = f"\t{data['State']}"
      district = f"\t{data['District']}"
      favorite_place = f"\t{data['Favorite Place']}"

      print("\t Name: " + name.title())
      print("\t City: " + city.title())
      print("\t State: " + state.title())
      print("\t District: " + district.title())
      print("\t Favorite Place: " + favorite_place.title())

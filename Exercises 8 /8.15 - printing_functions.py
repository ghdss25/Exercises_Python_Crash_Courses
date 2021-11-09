##  Put the functions for the example printing_models.py in a
## separate file called printing_functions.py. Write an import statement at the top
## of printing_models.py, and modify the file to use the imported functions.

def printing_models(name, specialty, **user_languages) :

      language = {

            'name' : name.title(),
            'specialty' : specialty.title(), 
      }

      for la, data in user_languages.items():

            language['la'] = data

      return user_languages

result = printing_models('Python', 'Data Science', language = 'Python', typical = 'Language', Situacion = True)

print(result)


## We’re now working with examples that are complex enough that they can be extended in any number of ways.
## Use one of the example programs from this chapter, and extend it by adding new keys and values,
## changing the context of the program or improving the formatting of the output.

languages = {

            'python' : ['back end', 'data science', 'artificial inteligente', 'neural networks', 'facial face', 'automation', 'natural process'],
            'java' : ['back end', 'embarked', 'desktop', 'games', 'engenieer data', 'mobile phone', 'IA'],
            'js' : ['data science', 'back end', 'front end', 'mobile phone Ios', 'mobile phone play store', 'games', 'servers', 'Animation'],
            'php' : ['Back end']
      }

for language, definition in languages.items():

      print(f"\n {language.title()}")

      for language in definition:

            print(f"\t {language.title()}")

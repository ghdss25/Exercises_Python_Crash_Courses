## 10-9. Silent Cats and Dogs: Modify your except block in Exercise 10-8 to fail
## silently if either file is missing.

filenames = ['txt/cat.txt', 'txt/dog.txt']

for filename in filenames:

      try:

            with open(filename) as f:

                  contents = f.read()

      except FileNotFoundError:

            pass

      else:

            print("Reading: " + filename)
            print(contents)

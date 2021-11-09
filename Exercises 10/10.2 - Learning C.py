## 10-2. Learning C: You can use the replace() method to replace any word in a
## string with a different word. Here’s a quick example showing how to replace
## 'dog' with 'cat' in a sentence:

## Read in each line from the file you just created, learning_python.txt, and
## replace the word Python with the name of another language, such as C. Print
## each modified line to the screen.

message = 'learning_python.txt'

with open(message) as file_object:

      texts = file_object.readlines()

for text in texts:

      print(text.replace('if', 'data Science'))
      print(text.replace('language', 'C'))

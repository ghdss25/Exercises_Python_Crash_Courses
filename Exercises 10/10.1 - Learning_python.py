## 10-1. Learning Python: Open a blank file in your text editor and write a few
## lines summarizing what you’ve learned about Python so far. Start each line
## with the phrase In Python you can. . . . Save the file as learning_python.txt in
## the same directory as your exercises from this chapter. Write a program that
## reads the file and prints what you wrote three times. Print the contents once by
## reading in the entire file, once by looping over the file object,
## and once by storing the lines in a list and then working with them outside the with block

file_patch = 'learning_python.txt'

with open(file_patch) as file_object:

      contents = file_object.read()

      print(contents)

## Loop

print("Doing Loop of txt")

with open(file_patch) as file_object:

      for fine in file_object:

            print(fine.rstrip())

# working with lines the txt of text

## on List

print("On List")

with open(file_patch) as file_object:

      lines = file_object.readlines()

for line in lines:

      print(line.rstrip())

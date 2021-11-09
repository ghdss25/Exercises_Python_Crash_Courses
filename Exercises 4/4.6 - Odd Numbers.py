## 4-6. Odd Numbers: Use the third argument of the range() function to make a
## list of the odd numbers from 1 to 20. Use a for loop to print each number.

for c in range(1, 20, 2):

      print(c)

print("")

print("Questão 4-7 Threes")
      
## 4-7. Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to
## print the numbers in your list.

c = []

for value in range(3, 30):

      c =  value ** 3
      print(c)

print("")
print("Count Threes",  c)

print("")
print("")
print("4-8. Cubes")

## 4-8. Cubes: A number raised to the third power is called a cube. For example,
## the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that
## is, the cube of each integer from 1 through 10), and use a for loop to print out
## the value of each cube

c = []

for cube in range(1, 10):

      c = cube ** 2 ** 3

      print(c)

print("Cubes of 1 the 10: ", c)

print("")
print("")
print("4-9. Cubes")
## 4-9:  Cube Comprehension: Use a list comprehension to generate a list of the
## first 10 cubes.

values = [value ** 2 ** 3 for value in range(1, 11)]
print("the numbers are of cubes: ", values)



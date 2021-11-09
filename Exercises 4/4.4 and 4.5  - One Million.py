## 4-4. One Million: Make a list of the numbers from one to one million, and then
## use a for loop to print the numbers. (If the output is taking too long, stop it by
## pressing ctrl-C or by closing the output window.)

list_count = [ ]

for value in range(1, 1000000, 3):

      list_count = value * 2

print("Possui uma contagem de: ", list_count)

## 4-5. Summing a Million: Make a list of the numbers from one to one million,
## and then use min() and max() to make sure your list actually starts at one and
## ends at one million. Also, use the sum() function to see how quickly Python can
## add a million numbers

list_numbers = [99, 120, 234, 456, 887, 972, 1000000]

for value in range(1, list_count):

      list_count = value * 2

print(min(list_numbers))
print(max(list_numbers))
print(sum(list_numbers))

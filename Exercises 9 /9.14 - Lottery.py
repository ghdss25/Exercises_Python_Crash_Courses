## 9-14. Lottery: Make a list or tuple containing a series of 10 numbers and
## five letters. Randomly select four numbers or letters from the list and print a
## message saying that any ticket matching these four numbers or letters wins a
## prize.

from random import choice

data = [9, 4, 5, 6, 91, 30, 45, 89, 13, 'G', 'U', 'S', 'T', 'A', 'V', 'O']

randomly = choice(data)
randomly1 = choice(data)
randomly2 = choice(data)
randomly3 = choice(data)

print("Prize draw of list ")

print([randomly], [randomly1], [randomly2], [randomly3])

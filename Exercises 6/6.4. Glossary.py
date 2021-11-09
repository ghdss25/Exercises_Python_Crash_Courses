# Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) by replacing your series of print()
# calls with a loop that runs through the dictionary’s keys and values.

## When you’re sure that your loop works, add five more Python terms to your glossary.
# When you run your program again, these new words and meanings should
# automatically be included in the output.

words = {'Pop' : 'Method removes the item at the given index from the list and returns the removed item.',
            'Hex' : 'function is one of the built-in functions in Python 3, which is used to convert an integer number into it is corresponding hexadecimal form',
            'Insert' : 'the specified value at the specified position',
            'Range' : 'function returns a sequence of numbers, starting from 0 by default, and increments by 1',
            'Sort' : 'function that orden in a list',
            'if' : 'do path of logic on software'}

for w, description in words.items():

      print(" \n " + w.title() + " " + description)

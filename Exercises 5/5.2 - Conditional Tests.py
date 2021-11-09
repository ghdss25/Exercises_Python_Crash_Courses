## 5-2. More Conditional Tests: You don’t have to limit the number of tests you
## create to ten. If you want to try more comparisons, write more tests and add
## them to conditional_tests.py. Have at least one True and one False result for
## each of the following:

## Tests for equality and inequality with strings:

print("Television")

device = 'Television'

if device != False:

      print("The Television is device")

else:

      print("The Television isn't device")

## Tests using the lower() method
print("Situacion of Television: ", device.lower != "eletronic")

## Numerical tests involving equality and inequality, greater than and
## less than, greater than or equal to, and less than or equal to

print("<=", 8 <= 29 , ">=", 10 >=93, "==", 89 == 29, "!=", 76 != 87)

## Tests using the and keyword and the or keyword
print(('Gustavo' == 'Gustavo') and ('Souza' == 'Silva'), ('Savio' != 'Ulisses') or ('Henrique' == 'Jackson'))

## Test whether an item is in a list
furniture = ['table', 'chair', 'wardrobe', 'couch']

print("Table is on list: ", 'table' in furniture)

## Test whether an item is not in a list
print("couch is not on list: ", 'couch' not in furniture)

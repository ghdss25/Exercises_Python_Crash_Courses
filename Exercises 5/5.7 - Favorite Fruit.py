## 5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of
## independent if statements that check for certain fruits in your list.

## Make a list of your three favorite fruits and call it favorite_fruits

## Write five if statements. Each should check whether a certain kind of fruit
## is in your list. If the fruit is in your list, the if block should print a statement,
## such as You really like bananas!

favorite_fruits = ['apple', 'pear', 'watermelon']

favorite_fruits.insert(4, 'bananas')
favorite_fruits.insert(5, 'Pineaapple')

if favorite_fruits != 'pear':

      print("Fruits on list is: ", favorite_fruits)
      print("Pear isn't list")

if favorite_fruits != 'grapes':

      print("Fruits on list is. ", favorite_fruits)
      print("Grapes isn't list")

if favorite_fruits == 'bananas':

      print("Fruits on list is", favorite_fruits)
      print("Bananas on list, I like of bananas")

if favorite_fruits == 'Pineaapple':

      print("Fruits on list is", favorite_fruits)
      print("Pineaapple on list, I like of Pineaapple")

if favorite_fruits != 'guava':

        print("Fruits on list is", favorite_fruits)
        print("guava isn't list")



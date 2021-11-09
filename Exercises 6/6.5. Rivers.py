## Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.

## Use a loop to print a sentence about each river, such as The Nile runs through Egypt.

## Use a loop to print the name of each river included in the dictionary.

## Use a loop to print the name of each country included in the dictionary.

pharse = {'the nile runs through' : 'egypt'} 
rivers = {'nilo' : 'egypt'}

# 1 question
for ph, description in pharse.items():

      print("\n" + ph.title() + " " + description.upper())

# 2 question
for river in rivers.keys():
      print(river.title())
      
# 3 question
for r in set(rivers.values()):
      print(r.title())



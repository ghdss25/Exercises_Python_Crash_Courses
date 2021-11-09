## Use the code in favorite_languages.py (page 97).

## Make a list of people who should take the favorite languages poll. Include
## some names that are already in the dictionary and some that are not.

## Loop through the list of people who should take the poll. If they have
## already taken the poll, print a message thanking them for responding.
## If they have not yet taken the poll, print a message inviting them to take
## the poll.

situacion = ['voting', 'not voting']
favorite_frameworks = {'Gustavo' : 'Django and Outsystems', 'Henrique' : 'React and Flutter'}
names = {'Gustavo' : 'Django and Outsystems'}, {'Henrique' : 'React and Flutter'}

for ff in favorite_frameworks.keys():

      print(" Person people voting: " + ff.title())

      if situacion != 'voting':

            print(ff.title(), "take the poll")

      else:

            print(ff.title(), "thanking for responding")

print("")
for n in names:

      print( "Person people voting", n)

if situacion == 'voting':

      print("take the poll", names[0])

else:
      
      print("thanking for responding", names[1])

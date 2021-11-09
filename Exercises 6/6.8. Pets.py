## Pets: Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the owner’s name.
## Store these dictionaries in a list called pets. Next, loop through your list and as
## you do, print everything you know about each pet.

pet = {'animal name' : ['dolly'],
        'age' : ['10 yearls old'],
        'breed' : ['shepherd'],
        'weight' : ['25,23 kg'],
        'country' : ['Brazil'],
        'owner' : ['Gerson']}

pet1 = {'animal name' : ['ryo'],
        'age' : ['02 yearls old'],
        'breed' : ['shiba inu'],
        'weight' : ['54,23 kg'],
        'country' : ['Japão'],
        'owner' : ['João Paulo']} 

for p, description in pet.items():

      print(f"\n {p.title()}'s animal historic")

      for pe in description:

            print(f"\t {pe.title()}")

print("")
print("Historic two")

for p1, description in pet1.items():

     print(f"\n {p1.title()}'s animal historic")

     for pe1 in description:

             print(f"\t {pe1.title()}")


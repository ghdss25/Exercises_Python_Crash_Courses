## People: Start with the program you wrote for Exercise 6-1 (page 99).
## Make two new dictionaries representing different people, and store all three
## dictionaries in a list called people. Loop through your list of people. As you
## loop through the list, print everything you know about each person.

dados = {'first name' : 'Gustavo',
             'second name' : 'Henrique',
             'third name' : 'Kelton',
             'four name' : 'Jackson',
             'five name' : 'Yuri Alberto'},

dados2 = {'first name' : 'Oliveira',
              'second name' : 'Ulisses',
              'third name' : 'Camara',
              'four name' : 'Zivech',
              'five name' : 'Trevor'}

dados3 = {'first name' : 'Fabiana',
              'second name' : 'Tereza',
              'third name' : 'Ana Raquel',
              'four name' : 'Mary',
              'five name' : 'Renata'}

person = [dados, dados2, dados3]

for p in person:

      print(p)



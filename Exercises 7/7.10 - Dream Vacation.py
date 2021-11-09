## Write a program that polls users about their dream vacation.
## Write a prompt similar to If you could visit one place in the world, where
## would you go? Include a block of code that prints the results of the poll.

responses = {}

dream_vacation = True

while dream_vacation:

    name = input("What's your favorite country: ?")
    response = input("If you could visit one place in the world, where would you go?")

    responses[name] = response

    repeat = input("would you go ? (yes / no) ")
    
    if repeat == 'no':
        
        dream_vacation = False

for name, response in responses.items():

    print(f" {name} The results of the poll {response} ")

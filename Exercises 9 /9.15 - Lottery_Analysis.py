## 9-15. Lottery Analysis: You can use a loop to see how hard it might be to win
## the kind of lottery you just modeled. Make a list or tuple called my_ticket.
## Write a loop that keeps pulling numbers until your ticket wins. Print a message
## reporting how many times the loop had to run to give you a winning ticket.

from random import choice

def get_winning_ticket(possibilities):

    winning_ticket = [ ]

    while len(winning_ticket) < 4:

        pulled_item = choice(possibilities)

        if pulled_item not in winning_ticket:

            winning_ticket.append(pulled_item)

    return winning_ticket

def check_ticket(played_ticket, winning_ticket):

    for element in played_ticket:

        if element not in winning_ticket:

            return False

    return True

def make_random_ticket(possibilities):

    ticket = [ ]

    while len(ticket) < 4:

        pulled_item = choice(possibilities)

        if pulled_item not in ticket:

            ticket.append(pulled_item)

    return ticket

possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e', 'f', 'g']

winning_ticket = get_winning_ticket(possibilities)

plays = 0

won = False

max_tries = 1_000_000

while not won:

    new_ticket = make_random_ticket(possibilities)
    won = check_ticket(new_ticket, winning_ticket)

    plays += 1

    if plays >= max_tries:

        break

if won:

    print("Winning have a ticket |")
    print(f"Your Ticket: {new_ticket}")
    print(f"Winning Ticket: {winning_ticket}")
    print(f"It only look {plays} tries to won")

else:

    print("Tried {plays} times, without pulling a winner. :(")
    print(f"Your Ticket: {new_ticket}")
    print(f"Winning Ticket: {winning_ticket}")
    




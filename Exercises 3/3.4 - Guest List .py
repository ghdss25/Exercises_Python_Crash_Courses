## Try It Yourse lf

## The following exercises are a bit more complex than those in Chapter 2, but
## they give you an opportunity to use lists in all of the ways described.

## 3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who
## would you invite? Make a list that includes at least three people you’d like to
## invite to dinner. Then use your list to print a message to each person, inviting
## them to dinner.

list_guest = ["Mary Maddison", "Ellen Saint", "Renata Ramos", "Lucia Juliana"]

print("I'm conviction for dinner on my house: ", list_guest[0])
print("I'm conviction for dinner on my house: ", list_guest[1])
print("I'm conviction for dinner on my house: ", list_guest[2])
print("I'm conviction for dinner on my house: ", list_guest[3])

print("")

## 3-5. Changing Guest List: You just heard that one of your guests can’t make the
## dinner, so you need to send out a new set of invitations. You’ll have to think of
## someone else to invite.

## Start with your program from Exercise 3-4. Add a print() call at the end
## of your program stating the name of the guest who can’t make it.

print("The people that's can't appear on dinner is: ", list_guest.pop(2))

## Modify your list, replacing the name of the guest who can’t make it with
## the name of the new person you are inviting.

list_guest.insert(2, 'Julia Taylor')
print(" I'm conviction for dinner on my house ", list_guest[2])
print(list_guest)

## Print a second set of invitation messages, one for each person who is still in your list.
list_guest.insert(4, 'Ana Belcanap')
list_guest.insert(5, 'Stella July')
print(" I'm conviction for dinner on my house ", list_guest[4])
print(" I'm conviction for dinner on my house ", list_guest[5])
print(list_guest)

print("")

## 3-6. More Guests: You just found a bigger dinner table, so now more space is
## available. Think of three more guests to invite to dinner.

## Start with your program from Exercise 3-4 or Exercise 3-5. Add a print()
## call to the end of your program informing people that you found a bigger
## dinner table.

list_guest_better = ["Henrique and Mary", "Jackson and Calleigh", "Eva Laure and May"]

print("I'm founded on bigger ", list_guest_better[0])
print("I'm founded on bigger ", list_guest_better[1])
print("I'm founded on bigger ", list_guest_better[2])

print("")

print("The people that's can't appear on dinner is: ", list_guest_better.pop(0))
print("The people that's can't appear on dinner is: ", list_guest_better.pop(1))

print("")

# Use insert() to add one new guest to the beginning of your list.

list_guest_better.insert(0, 'Elaine and Marcos')
print("I'm founded on bigger ", list_guest_better[0])
print(list_guest_better)

print("")

# Use insert() to add one new guest to the middle of your list.
list_guest_better.insert(1, 'Igor and Înes')
print("I'm founded on bigger ", list_guest_better[1])
print(list_guest_better)

print("")

# Use append() to add one new guest to the end of your list.
list_guest_better.append('Yuri Alberto and Katia maria')
print(list_guest_better)

print("")

# Print a new set of invitation messages, one for each person in your list.

list_guest1 = ["Vania", "Ellen Fabian", "Glecia Ramos", "Luciana Juliana"]

print("I'm conviction for dinner on my house: ", list_guest1[0])
print("I'm conviction for dinner on my house: ", list_guest1[1])
print("I'm conviction for dinner on my house: ", list_guest1[2])
print("I'm conviction for dinner on my house: ", list_guest1[3])

# Working with one of the programs from Exercises use len() to print a message indicating the number of people you are inviting to dinner.
len(list_guest)
len(list_guest1)
len(list_guest_better)

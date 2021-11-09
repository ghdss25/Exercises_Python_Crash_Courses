## Movie Tickets: A movie theater charges different ticket prices depending on
## a person’s age. If a person is under the age of 3, the ticket is free; if they are
## between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is
## $15. Write a loop in which you ask users their age, and then tell them the cost
## of their movie ticket.

while True:

      yearls_old = int(input("How old are you ?"))

      if yearls_old == 1 and yearls_old <= 3:

            print("The ticket is free")

      elif yearls_old == 3 or yearls_old <= 12:

            print("the ticket is $10")

      elif yearls_old >= 12:

            print("the ticket is $15")

      elif yearls_old == 0:

            print("exit")
            break

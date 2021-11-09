## 10-5. Programming Poll: Write a while loop that asks people why they like
## programming. Each time someone enters a reason, add their reason to a file
## that stores all the responses.

programming_poll = 'txt/programming_poll.txt'

answers = [ ]

while True:

      answer = input("Why they like programming: ")
      answers.append(answer)

      continue_poll = input("Would you like to let someone else respond? (y / n)")

      if continue_poll != 'y':

            break

with open(programming_poll, 'a') as file_object:

      for answer in answers:

            file_object.write(answer + "\n")


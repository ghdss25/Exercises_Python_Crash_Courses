## 8-10. Sending Messages: Start with a copy of your program from Exercise 8-9.
## Write a function called send_messages() that prints each text message and
## moves each message to a new list called sent_messages as it’s printed. After
## calling the function, print both of your lists to make sure the messages were
## moved correctly.

list_message = ['Gustavo its learn python', 'Gustavo its doing your projects praticses in Outsystems', 'Im search the first job in Programming']
sent_messages = list_message

def send_messages(titles):

      sent_messages.append('Gustavo is like of Pes 2021')

      for title in titles:

            msg = f"The Message : {title.title()}"

            print(msg)

send_messages(sent_messages)


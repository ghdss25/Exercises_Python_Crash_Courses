## Start with your work from Exercise 8-10. Call the
## function send_messages() with a copy of the list of messages. After calling the
## function, print both of your lists to show that the original list has retained its
## messages.

list_message = ['Gustavo its learn python', 'Gustavo its doing your projects praticses in Outsystems', 'Im search the first job in Programming']
sent_messages = list_message

list_message1 = ['Gustavo its learn python', 'Gustavo its doing your projects praticses in Outsystems', 'Im search the first job in Programming']
sent_messages1 = list_message1

def send_messages(titles):

      sent_messages.append('Gustavo is like of Pes 2021')

      for title in titles:

            msg = f"The Message : {title.title()}"

            print(msg)

send_messages(sent_messages)

def aux_messages(titles1):

      sent_messages1.append('Gustavo is like of Pes 2021')

      for title in titles1:

            msg = f"The Message : {title.title()}"

            print(msg)

aux_messages(sent_messages1)

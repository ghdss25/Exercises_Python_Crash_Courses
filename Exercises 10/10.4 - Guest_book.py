## 10-4. Guest Book: Write a while loop that prompts users for their name. When
## they enter their name, print a greeting to the screen and add a line recording
## their visit in a file called guest_book.txt. Make sure each entry appears on a
## new line in the file.

guest_book = 'txt/guest_book.txt'

while True:

      print("Select a write quit for exit of system")

      name = input("what's your name: ")

      if name == 'quit':

            print("Exit of system: ")
            break

      else:

            with open(guest_book, 'a') as file_object:

                  file_object.write(name + " " +  " Welcome the system ghdss " + " \n ")
                  
            
      

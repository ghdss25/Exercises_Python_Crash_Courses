## 10-3. Guest: Write a program that prompts the user for their name. When they
## respond, write their name to a file called guest.txt.

name = 'txt/guest.txt'

with open(name, 'w') as file_object:

      file_object.write(input(" What's your name: "))


      

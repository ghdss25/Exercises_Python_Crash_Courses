## 8-8. User Albums: Start with your program from Exercise 8-7. Write a while
## loop that allows users to enter an album’s artist and title. Once you have that
## information, call make_album() with the user’s input and print the dictionary
## that’s created. Be sure to include a quit value in the while loop.

def make_album(name, album, tracks = 0):

      artist = {

            'name' : name.title(),
            'album' : album.title(),
            
            }

      if tracks:

            artist['tracks'] = tracks

      return artist

date_name = "Report the name: "
date_album = "Report the Album: "

while True:

      name = input(date_name)

      if name == 'quit':

            break

      album = input(date_album)

      if album == 'quit':

            break

      artist = make_album(name, album)
      print(artist)

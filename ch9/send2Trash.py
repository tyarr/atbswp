# Script to open create a file, write to it, and the safely delete it

import send2trash, os

os.chdir('C:\\Users\\tyya\\Documents\\testenv')  # change directory

baconFile = open('bacon.txt', 'a') # Create the test file

baconFile.write('Bacon is not a veggies!')  # Writes to txt file

baconFile.close()  # Closes txt file

send2trash.send2trash('bacon.txt')  # Safely deletes txt file
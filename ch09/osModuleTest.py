# Script that shows what files exist in a directory
# If os.unlink is uncommented it will delete the files that end in txt
import os

# Change directory
os.chdir('C:\\Users\\tyya\\Documents\\foldertest2')

for filename in os.listdir():
    if filename.endswith('.txt'):
        # os.unlink(filename)
        print(filename)
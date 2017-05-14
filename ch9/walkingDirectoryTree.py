# Script that uses os.walk to display the directory tree

import os

for foldername, subfolders, filenames in os.walk('C:\\Users\\tyya\\Documents\\testenv'):
    print('The current folder is ' + foldername)

    for subfolder in subfolders:
        print('Subfolder of ' + foldername + ': ' + subfolder)

    for filename in filenames:
        print('File inside: ' + foldername + ': ' + filename)

    print('')
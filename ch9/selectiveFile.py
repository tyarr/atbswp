#! python3
# Program: Selective copy that walks through folder tree and searches for files with a certain file extension

import glob, os, shutil

# define file location & extension type
files = glob.iglob(os.path.join('C:\\Users\\tyarboro\\Documents\\scripts\\testfolder', "*.jpg"))

#
for file in files:
    if os.path.isfile(file):
        print('Copying file %s' % file + ' to C:\\Users\\tyarboro\\Documents\\scripts\\testbackup ') # Print out what is done
        shutil.copy2(file, 'C:\\Users\\tyarboro\\Documents\\scripts\\testbackup') # Copy to the new directory

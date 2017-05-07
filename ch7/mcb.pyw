#! python3
# mcb.pyc - Saves and loads pieces of text to the clipboard
# Usage: py.exe mcb.pyw save <keyword> Saves clipboard to keyword.
#       py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#       py.exe mcb.pyw list - Loads all keywords to clipboard

import shelve, pyperclip, sys, os

mcbShelf = shelve.open('mcb')

# define removal
def remove_files():
    mcbShelf.close()
    os.remove('mcb.dat')
    os.remove('mcb.bak')
    os.remove('mcb.dir')

def del_keys():
    print('What key would you like to delete?')
    deleteKey = input()
    try:
        del mcbShelf[str(deleteKey)]
    except KeyError:
        print('No such key exists')
        pass

# Save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    # Various options
    # Copies keywords to clipboard
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    # delete keywords
    if sys.argv[1].lower() == 'delete':
        del_keys()
    # delete all keywords
    if sys.argv[1].lower() == 'nuke':
        remove_files()
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])


mcbShelf.close()


catNames = []
while True:
    print('Enter the name of the cat ' + str(len(catNames) + 1 ) +
          ' (Or enter nothing to stop):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name] #list concatentation

#print the list
print('The cat names are:')
for name in catNames:
    print(' ' + name)

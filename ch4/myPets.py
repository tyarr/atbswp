myPets = ['Archer', 'Lana', 'Pheobus']

print('Enter a pet name')
name = input()

if name not in myPets:
    print('That is not one of my pet names')
if name == 'Archer':
    print(name + ' he is a big boy')
if name == 'Banana':
    print(name + ' that isnt even a pet name')
else:
    print(name + ' is my pet') 

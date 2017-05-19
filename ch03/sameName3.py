def spam():
    global eggs
    eggs = 'spam' #global config

def bacon():
    eggs = 'bacon' #local config

def ham():
    print(eggs) #global call

eggs = 42 #global call
spam()
print(eggs)

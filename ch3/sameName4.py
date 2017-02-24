def spam():
    eggs = 'spam local'
    print(eggs) #ERROR!

eggs = 'global'
spam()

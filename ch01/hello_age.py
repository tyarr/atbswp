# First Python Program
# It says hello, ask for name & age, and informs how old one will be in 15 years

#print('Hello World')
print('Hey you, what is your name?') #Asking for name!

myName = input()
print()
print('It is good to meet you ' +myName)
print()
print('Your name has this many characters in it! ' + str(len(myName)) + ' to be exact!')
print()
#print (len(myName))

print('What is your age?')
myAge = input()

print('Wowza ' +myName + '!')
print ()
print('You are ' +myAge)
print()
print(str(myName) + ', in 15 years you will be ' + str(int(myAge) + 15) + ', that is depressing!')


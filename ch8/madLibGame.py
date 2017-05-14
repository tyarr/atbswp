# This is a madlib game
# User inputs data and it is printed to the console
# The printed text to the console is saved as a text file

# Input data
print('Enter an adjective: ')
a1 = input()
print('Enter a noun: ')
n1 = input()
print('Enter a verb: ')
v1 = input()
print('Enter a noun:')
n2 = input()

# Print to console
print('The ' + a1 + ' panda walked to the ' + n1 + ' and then ' + v1 + '. A nearby ' + n2 + ' was unaffected by these events.')

# Save input
with open('output.txt', 'w') as f:
    print('The ' + a1 + ' panda walked to the ' + n1 + ' and then ' + v1 + '. A nearby ' + n2 + ' was unaffected by these events.', file=f)
while True:
	print('What is your age?')
	age = input()
	if age.isdecimal():
		break
	print('Please enter a numeric value')
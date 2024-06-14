print('Welcome to the simple calculator program! ')
first=float(input('Enter the first number: '))
second=float(input('Enter the second number: '))
operation=input('Select an arithmetic operation(+,-,*,/): ')
game='yes'
#continue the game until game=='no'
while game=='yes':
	if operation=='+':
		print('Result: '+str(first+second))
	elif operation=='-':
		print('Result: '+str(first-second))
	elif operation=='*':
		print('Result: '+str(first*second))
	elif operation=='/' and second!=0:
		print('Result: '+str(first/second))
	#the situation for Division by zero
	elif operation=='/' and second==0:
		print('Error: Division by zero!')
		first=float(input('Enter the first number: '))
		second=float(input('Enter the second number: '))
		operation=input('Select an arithmetic operation(+,-,*,/): ')
		continue
	play=input('Do you want to perform another calculation?(yes or no): ')
	if play=='no':
		game='no'
	else:
		first=float(input('Enter the first number: '))
		second=float(input('Enter the second number: '))
		operation=input('Select an arithmetic operation(+,-,*,/): ')
print('Goodbye!')
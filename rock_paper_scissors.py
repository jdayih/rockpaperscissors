Python 3.8.1 (v3.8.1:1b293b6006, Dec 18 2019, 14:08:53) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> from random import randint
>>> users_choice = input("Make your move: ")
Make your move: rock
>>> users_choice = users_choice.lower()
>>> x = ['rock','paper','scissors']
>>> num = randint(0,2)
>>> computers_choice = x[num]
>>> print (computers_choice)
paper
>>> 
if users_choice == computers_choice:
	print ("It's a tie!")
elif users_choice == 'rock':
	if computers_choice == 'paper':
		print ("Computer wins!")
	else:
		# user input is scissors
		print ("User wins!")
elif computers_choice == 'paper':
	if users_choice == 'scissors':
		print ("User wins!")
	else:
		# user input is rock
		print ("Computer wins!")
elif computers_choice == 'scissors':
	if users_choice == 'paper':
		print ("Computer wins!")
	else:
		# user input is rock
		print ("User wins!")

		
Computer wins!
>>> 
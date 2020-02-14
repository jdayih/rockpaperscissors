from random import randint

users_choice = input("Make your move: ")
users_choice = users_choice.lower()
x = ['rock','paper','scissors']
num = randint(0,2)
computers_choice = x[num]
print (computers_choice)


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

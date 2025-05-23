#Let’s build a guess game. In this game we would have a secret number and then ask the user to Guess the secret number. If the user guesses it right before the 5th guess, the user wins and if he doesn’t the user loses the guess. 

secret_number = 8
guess_limit = 5
guess_count = 0

print("welcome to the game and you have 5 attempts to guess the right answer")

while guess_count < guess_limit:
	user_input = int(input("enter your answer: "))
	guess_count += 1
	
	if user_input == secret_number:
		print("very correct")
		break
		
	else:
	     print("Try again")
else:
   print("You have exhausted your trial limit, so you lose ")

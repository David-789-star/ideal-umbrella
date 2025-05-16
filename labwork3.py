Question = "What is the capital of Lagos"
correct_answer = "ikeja"

while True:
	user_answer = input(Question + "  ")
	if user_answer == correct_answer:
		print("very good")
	else:
		print("try again")
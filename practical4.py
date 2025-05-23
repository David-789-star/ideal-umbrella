# Write a program to keep asking for a number until you enter a negative number. At the end, 
# print the sum of all entered numbers.



Total = 0

while True:
	user_input = int(input("enter your negative number to stop: "))
	if user_input > 0:
		print("try again")
	else:
		print("very good")
		break
	Total += user_input
print("The total number is", Total)


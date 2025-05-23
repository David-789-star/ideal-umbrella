#Write a program to ask for a name until the user enters END. Print the name each time. 
#When you are done, print "I am done."

while True:
	name = input("enter your name: ")
	if name == "END":
		break
	print("I entered", name)
print("i am done")

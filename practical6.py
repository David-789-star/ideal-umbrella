#a program to find the multiples of n, your loop should iterate 10 times.

n = int(input("enter your number to find the multiple: "))

for i in range(1,11):
	print(f"{n} * {i} = {n * i}")

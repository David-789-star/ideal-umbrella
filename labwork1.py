n = int(input())
if n % 2 == 1:
	print("weird")
elif (n % 2 == 0) and (n == 2 or n < 5):
	print("not weird")
elif (n % 2 == 0) and (n == 6 or n < 20):
	print("weird")
elif (n % 2 == 0) and (n > 20):
	print("not weird")
	
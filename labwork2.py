

House_price = 1000000
user_price = int(input("enter your budget price:"))

if (user_price < 500000) and (user_price > 300000):
	down_payment = 10 / 100 * House_price
	print(f"downpayment with 10%: {down_payment}")
elif user_price > 500000:
	down_payment = 20 / 100 * House_price
	print(f"downpayment with 20%: {down_payment}")
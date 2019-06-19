annual_salary = int(input("Enter the starting salary:"))

semi_annual_raise = 0.07
portion_down_payment = 0.25
current_savings = 0
total_cost = 1000000
r = 0.04

def money_after_36months(annual_salary, portion_saved):
	current_savings = 0
	months = 0
	while months <= 36:
		money = current_savings + annual_salary / 12 * portion_saved + current_savings * r / 12
		current_savings = money
		months += 1
		if months % 6 == 0:
			annual_salary = (semi_annual_raise + 1) * annual_salary
	return current_savings

def lowest_money(annual_salary):
	current_savings = 0
	months = 0
	portion_saved = 1
	while months <= 36:
		money = current_savings + annual_salary / 12 * portion_saved + current_savings * r / 12
		current_savings = money
		months += 1
		if months % 6 == 0:
			annual_salary = (semi_annual_raise + 1) * annual_salary
	return current_savings

if lowest_money(annual_salary) < total_cost * portion_down_payment:
	print("It is not possible to pay the down payment in three years.")

else:
	up = 1
	down = 0
	biseciton = 0
	while (current_savings <= portion_down_payment * total_cost + 100 and current_savings >= portion_down_payment * total_cost - 100) == 0:
		portion_saved = 0.5 * (up + down)
		current_savings = money_after_36months(annual_salary, portion_saved)
		if current_savings >= portion_down_payment * total_cost + 100:
			up = portion_saved
		elif current_savings <= portion_down_payment * total_cost - 100:
			down = portion_saved
		biseciton += 1
		# print(biseciton, current_savings)

	print("Best saving rate:", portion_saved)
	print("Steps in biseciton search:", biseciton)
annual_salary = int(input("Enter your annual salary:"))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal:"))
total_cost = int(input("Enter the cost of your dream home:"))

portion_down_payment = 0.25
current_savings = 0
r = 0.04

months = 0
# print(total_cost * portion_down_payment)
while(current_savings < total_cost * portion_down_payment):
    money = current_savings + annual_salary / 12 * portion_saved + current_savings * r / 12
    current_savings = money
    months += 1

print("Number of months:", months)

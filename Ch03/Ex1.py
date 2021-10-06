

##################
# Exercise 3.1
# Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.
# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0
##################


hours = float(input("Enter Hours: "))
rate = float(input("Enter rate: "))

extra_hours = 0

if hours > 40:
    extra_hours = hours - 40

extra_pay = extra_hours * rate * 0.5
pay = hours * rate + extra_pay
print("Pay: ",pay)
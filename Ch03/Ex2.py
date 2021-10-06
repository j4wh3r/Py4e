##################
# Exercise 3.2
# Rewrite your pay program using try and except so that your program handles
# non-numeric input gracefully by printing a message and exiting the
# program. The following shows two executions of the program:
#
#  Enter Hours: 20
#  Enter Rate: nine
#  Error, please enter numeric input
#
#  Enter Hours: forty
#  Error, please enter numeric input
#  Enter Hours: 20
##################


try:
    hours = float(input("Enter Hours: "))
    rate = float(input("Enter rate: "))
except:
    print("Error, please enter numeric input")
    exit(0)

else:
    extra_hours = 0

    if hours > 40:
        extra_hours = hours - 40

    extra_pay = extra_hours * rate * 0.5
    pay = hours * rate + extra_pay
    print("Pay: ",pay)
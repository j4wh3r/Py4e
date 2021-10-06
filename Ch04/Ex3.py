# Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters
# (h and rate).


def computepay(h,r):
    added_hours = 0
    if h > 40:
        added_hours = h - 40
    added_pay = 0.5 * added_hours * r
    pay = h * r + added_pay
    return pay

hours = float(input("enter hours: "))
rate = float(input("enter rate: "))

print(computepay(hours,rate))




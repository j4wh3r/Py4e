#Exercise 2: Write another program that prompts for a list of numbers
#as above and at the end prints out both the maximum and minimum of
#the numbers instead of the average

max = None
min = None
while True:
    str_number = input("enter a number: ")
    if str_number == "done":
        break
    try:
        number = float(str_number)
    except:
        print("invalid input")
        continue
    if max == None or max < number:
        max = number
    if min == None or min > number:
        min = number

print(min,max,sep=" | ")
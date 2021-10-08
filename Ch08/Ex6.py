# Exercise 6: Rewrite the program that prompts the user for a list of
# numbers and prints out the maximum and minimum of the numbers at
# 8.16. EXERCISES 107
# the end when the user enters “done”. Write the program to store the
# numbers the user enters in a list and use the max() and min() functions to
# compute the maximum and minimum numbers after the loop completes.

numbers = []
while True:

    nums = input("enter a number: ")
    if nums == "done":
        break
    else:
        try:
            nums = float(nums)
        except:
            print("no such a number!")
            continue
        numbers.append(nums)

print("maximun: ",max(numbers))
print("minimum: ",min(numbers))
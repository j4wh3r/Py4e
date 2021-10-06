# Exercise 7: Rewrite the grade program from the previous chapter using
# a function called computegrade that takes a score as its parameter and
# returns a grade as a string.


def computegrade(score):
    if score > 1.0 or score < 0.0 and (score is not float):
        print("out of range")
    elif (score >= .9):
        print("A")
    elif score >= .8:
        print("B")
    elif score >= .7:
        print("C")
    elif score >= .6:
        print("D")
    elif (score == 0.0) or (score < .6):
        print("F")

try: score = float(input("Enter a score between 0.0 and 1.0: "))
except: print("Bad score")
else: computegrade(score)

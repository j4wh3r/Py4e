
name = input("enter file name: ")

with open(name,"r") as f:

    count = 0
    total = 0

    for line in f:
        if line.startswith("X-DSPAM-Confidence:"):
            number = float(line[line.index(" ")+1:])  #in the files, u can see the space between the colon character and the start of the float number.
            total += number
            count += 1
    average = total/count
    print(f"average span confidence: {average}")


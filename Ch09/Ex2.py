# Exercise 2: Write a program that categorizes each mail message by
# which day of the week the commit was done. To do this look for lines
# that start with “From”, then look for the third word and keep a running
# count of each of the days of the week. At the end of the program print
# out the contents of your dictionary (order does not matter).
# Sample Line:
# From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
# Sample Execution:
# python dow.py
# Enter a file name: mbox-short.txt
# {'Fri': 20, 'Thu': 6, 'Sat': 1}

l = []
d = {}

with open("../mbox-short.txt","r") as f:
    # making a list that contains the days
    for line in f:
        if line.startswith("From"):
            lines = line.split()
            if len(lines) > 2:
                day = lines[2]
                l.append(day)
    # adding each day to a dict and counting its occurence
    for day in l:
        if day not in d:
            # 'sat' =
            d[day] = 1
        else:
            d[day] += 1

    print(d)

# Exercise 4: Find all unique words in a file
#  List all unique words, sorted
# in alphabetical order, that are stored in a file romeo.txt containing a
# subset of Shakespeare’s work.
# To get started, download a copy of the file www.py4e.com/code3/romeo.txt.
# Create a list of unique words, which will contain the final result. Write
# a program to open the file romeo.txt and read it line by line

name = input("enter a file name: ")
words = []

with open(name,"r") as f:
    for line in f:
        for word in line.split():
            if word not in words:
                words.append(word)

    print(sorted(words))


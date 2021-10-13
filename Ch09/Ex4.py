# xercise 3: Write a program to read through a mail log, build a histogram using a dictionary to count how many messages have come from
# each email address, and print the dictionary.
# Enter file name: mbox-short.txt
# {'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3,
# 'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1,
# 'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3,
# 'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1,
# 'zqian@umich.edu': 4, 'stephen.marquard@uct.ac.za': 2,
# 'ray@media.berkeley.edu': 1}

with open("../mbox-short.txt","r") as f:
    list_of_mails = []
    count = {}

    for line in f:
        if line.startswith("From:"):
            list_of_mails.append(line.split()[1])


    for mail in list_of_mails:
        if mail not in count:
            count[mail] = 1
        else:
            count[mail] += 1

#first method
v = list(count.values())
k = list(count.keys())
max_value = max(v)
max_key = k[v.index(max_value)]
print(max_key, " ", max_value)

#2nd method
dicto = {v:k for k,v in count.items()}
print(dicto[max(dicto)],max(dicto))





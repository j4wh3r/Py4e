

with open("../mbox.txt","r") as f:
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

    print(count)



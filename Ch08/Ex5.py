
# name = input("enter a file name: ")

count = 0
with open("mbox-short.txt","r") as f:
    for line in f:
        if line.startswith("From:"):
            mail = line[line.index(" ")+1:]
            print(mail)
            count += 1
    print(f"there were {count} lines in the file with From as the first word")
    

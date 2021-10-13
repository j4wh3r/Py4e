
with open("../mbox-short.txt","r") as f:
        domains = []
        for line in f:
            if line.startswith("From:"):
                line = line.rstrip()
                domains.append(line[line.index("@")+1:])

d = {}
for domain in domains:
    if domain not in d.keys():
        d[domain] = 1
    else:
        d[domain] += 1

print(d)
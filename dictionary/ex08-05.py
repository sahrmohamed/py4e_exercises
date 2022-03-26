nedic = dict()
fname= input("Enter file name: ")
fhand = open(fname)
for line in fhand:
    if line.startswith("From"):
        words = line.split()
        if len(words)>2:
           emailadd = words[1]
           indexofat = emailadd.find("@")
           domain = emailadd[indexofat+1:]
           nedic[domain] = nedic.get(domain, 0) + 1
           
print(nedic)
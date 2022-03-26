fname = input("Enter file name: ")
fhand = open(fname)
count = 0
total = 0
for line in fhand:
    count = count + 1
    if not line.startswith("X-DSPAM-Confidence: 0.8475"):continue
    indexcolon = line.find(":")
    fnm = line[indexcolon + 1:]
    total = total + 1
print("Average of spam confidence:",total/count)
    




nedic = dict()
fname= input("Enter file name: ")
fhand = open(fname)
for line in fhand:
    if line.startswith("From"):
        words = line.split()
        if len(words)>2:
            dayofweek = words[2]
            nedic[dayofweek] = nedic.get(dayofweek, 0) + 1
print(nedic)

        
       
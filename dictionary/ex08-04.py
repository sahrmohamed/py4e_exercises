largest = None
nedic = dict()

fname= input("Enter file name: ")
fhand = open(fname)
for line in fhand:
    if line.startswith("From"):
        words = line.split()
        if len(words)>2:
           emailadd = words[1]
           nedic[emailadd] = nedic.get(emailadd, 0) + 1


nlist = list(nedic.items())
for key,val in nlist:
    if largest is None or val > largest:
        largest = val
        lkey = key
print(lkey,largest)



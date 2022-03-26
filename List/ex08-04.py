alist = list()
fname = input("Enter a file name: ")
fhand = open(fname)
for line in fhand:
    words = line.split()
    for word in words:
        if word not in alist:
            alist.append(word)
        else:continue
alist.sort()
print(alist)
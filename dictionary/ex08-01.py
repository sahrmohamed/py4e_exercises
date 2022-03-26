ndic = dict()
fhand = open("documents/words.txt")
for line in fhand:
    line.rstrip()
    words = line.split()
    for word in words:
        ndic[word]= ndic.get(word, 0) + 1
print(ndic)
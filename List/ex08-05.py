count = 0
fname = input("Enter a file name: ")
fhand = open(fname)
for line in fhand:
    if line.startswith("From"):
        words = line.split()
        print(words[1])
        count = count + 1

print("There were",count,"lines in the file with From as the first word")
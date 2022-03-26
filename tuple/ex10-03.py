fhand = input("Enter file name: ")
fname = open(fhand)

ledic = dict()
frlist = list()

for line in fname:
    line.lower()
    line.rstrip()
    line.strip()
    line.lstrip()
    for word in line:
        for char in word:
            frlist.append(char)

for lett in frlist:
    ledic[lett]= ledic.get(lett, 0) + 1

print(ledic)
            
        

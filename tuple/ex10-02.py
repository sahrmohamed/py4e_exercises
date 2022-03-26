nedic = dict()

fname= input("Enter file name: ")
fhand = open(fname)
for line in fhand:
    if line.startswith("From"):
        words = line.split()
        if len(words)>2:
           hour = words[5]
           hourlist = hour.split(":")
           time = hourlist[0]
           nedic[time] =nedic.get(time, 0) + 1

hlist = list(nedic.items())
hlist.sort()

for hour, count in hlist:
    print(hour,count)


           

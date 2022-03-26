nlist = list()
while True:
    Nm = input("Enter a Number: ")

    if Nm == "done":
        print("Largest:",max(nlist),"Smallest:",min(nlist))
        quit()
    else:
        try:
            Nm =float(Nm)
            nlist.append(Nm)
        except:
            print("Invalid input")
            continue
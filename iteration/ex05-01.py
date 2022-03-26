count = 0
Total = 0
while True:
    Nm = input("Enter a Number: ")

    if Nm == "done":
        print(Total, count, Total/count)
        quit()
    try:
        Nm =float(Nm)
    except:
        print("Invalid input")
        continue
    Total = Total + Nm
    count = count + 1

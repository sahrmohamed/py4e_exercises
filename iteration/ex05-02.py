smallest = None
largest = None
while True:
    Nm = input("Enter a Number: ")

    if Nm == "done":
        print("Largest:",largest,"Smallest:",smallest)
        quit()
    else:
        try:
            Nm =float(Nm)
            if smallest is None or smallest > Nm:
                smallest = Nm
            if largest is None or largest < Nm:
                largest = Nm
            
        except:
            print("Invalid input")
            continue
    
    

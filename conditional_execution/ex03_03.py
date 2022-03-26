try:
    sc = float(input("Enter score: "))
except:
    print("Bad score")
    quit()
if sc > 1.0:
    print("Bad Score")
    quit()
if sc >= 0.9:
    print("A")
if sc >= 0.8 and sc < 0.9:
    print("B")
if sc >= 0.7 and sc <0.8:
    print("C")
if sc >= 0.6 and sc < 0.7:
    print("D")
if sc < 0.6:
    print("F")

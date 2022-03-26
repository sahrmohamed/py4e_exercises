class MyStuff:

    def __init__(self):
        self.tangerine = "This tangerine variable is a string"

    def apple(self):
        print("This is an apple")
    
    def replace(self):
        self.tangerine = "This %s variable is a string" % "Kangaroo"

thing = MyStuff()


thing.replace()
thing.apple()
print(thing.tangerine)

    
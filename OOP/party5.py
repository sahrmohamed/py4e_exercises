class PartyAnimal:
    x = 0
    name = ''

    def __init__(self, nam):
        self.name = nam
        print(self.name,"constructed")

    def party(self):
        self.x = self.x + 1
        print(self.name,"party count is:",self.x)


#class CricketFan(PartyAnimal):
    #points = 0

    ##def six(self):
     #   #self.points = self.points + 6
     #   self.party()
     #   print(self.name, "points", self.points)
#
#b = CricketFan("Ben")
#b.six()

    


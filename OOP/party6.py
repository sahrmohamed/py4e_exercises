from party5 import PartyAnimal
class CricketFan(PartyAnimal):
    points = 0
    def six(self):
        self.points = self.points + 6
        #self.party()
        print(self.name,"points",self.points)
s = CricketFan("Ben")
s.six()
s.party()
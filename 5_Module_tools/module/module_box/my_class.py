
class Hotel():
    
    hType = "5 star" # class variable
    # method
    def __init__(self, nGuest, nRoom, nHall):
        self.ng = nGuest # instance variables
        self.nr = nRoom
        self.nh = nHall+1
        self.__hidVar = 5 # private, hidden

    def getInfo(self):
        print("Number of guests is {}".format(self.ng))
        print("Number of rooms is {}".format(self.nr))
        print("Number of halls is {}".format(self.nh))
        return "something"
    
    def setGuest(self, nGuest):
        self.ng = nGuest
        
    def getGuest(self):
        return self.ng
        # USD, all, [USD, EUR], date=all, 2015-01-01 - API request www.mongolbank.mn\\getrate\{USD, 2015-01-01}

    def setRoom(self, nRoom):
        self.nr = nRoom

    def setHall(self, nHall):
       self.nh = nHall
   
    def dispHid(self):
       return self.__hidVar
       
# class inheritance
class bigHotel(Hotel):
    
    def __init__(self):
        super().__init__(1500,1000,100)
        # Hotel.__init__(self, 1500, 1000, 100)
        
    def getNumber(self):
        return self.ng + self.nr + self.nh
        


class Client:
    def __init__(self):
        self._name = ""
        self.__address = ""
        self.__dob = None
    #enddef

    def getName(self):
        return self._name

    def setDetails(self, name, address, dob):
        self._name = name
        self.__address = address
        self.__dob = dob
    #enddef
#endclass

class Buyer(Client):
    def __init__(self):
        super().__init__()

        self.__noOfBedroomsRequired = 0
        self.__offStreetParking = False
        self.__areaDesired = ""
    #enddef

    def setDetails(self, name, address, dob):
        super().setDetails(name, address, dob)

        print(self.getName())
    #enddef

    def getNoOfBedroomsRequired(self):
        return self.__noOfBedroomsRequired
    #enddef

    def offStreetParking(self):
        return self.__offStreetParking
    #enddef

    def getAreaDesired(self):
        return self.__areaDesired
    #enddef

    def setNoOfBedroomsRequired(self, rooms):
        self.__noOfBedroomsRequired = rooms
    #enddef

    def setOffStreetParking(self, val):
        self.__offStreetParking = val
    #enddef

    def setAreaDesired(self, area):
        self.__areaDesired = area
    #enddef
#endclass

def deleteClient(buyer):
    buyer.location.delete()
    buyer.delete()

b = Buyer()

b.setDetails("Fahad", "london", "1980")

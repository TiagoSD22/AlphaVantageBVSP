import datetime

class CompanyStock:
    def __init__(self, lastUpdate : datetime = datetime.date.today(), 
                        volume : float = 0,
                        price : float = 0,
                        change : float = 0,
                        changePercent : float = 0,
                        companySymbol : str = ""):

        self.__lastUpdate = lastUpdate
        self.__volume = volume
        self.__price = price
        self.__change = change
        self.__changePercent = changePercent
        self.__companySymbol = companySymbol
    
    def getLastUpdate(self):
        return self.__lastUpdate
    
    def setLastUpdate(self, lastUpdate : datetime = datetime.date.today()):
        self.__lastUpdate = lastUpdate
    
    def getVolume(self):
        return self.__volume
    
    def setVolume(self, volume : float = 0):
        self.__volume = volume
    
    def getPrice(self):
        return self.__price
    
    def setPrice(self, price : float = 0):
        self.__price = price

    def getChange(self):
        return self.__change
    
    def setChange(self, change : float = 0):
        self.__change = change
    
    def getChangePercent(self):
        return self.__changePercent
    
    def setChangePercent(self, changePercent : float = 0):
        self.__changePercent = changePercent

    def getCompanySymbol(self):
        return self.__companySymbol
    
    def setCompanySymbol(self, companySymbol : str):
        self.__companySymbol = companySymbol
    
    def getFormatedTimeStamp(self):
        return self.__lastUpdate.strftime("%m-%d-%y") if self.__lastUpdate is not None else ""

    def toJSON(self):
        data = {
            "lastUpdate" : self.getFormatedTimeStamp(),
            "price" : self.__price,
            "change" : self.__change,
            "changePercent" : self.__changePercent,
            "volume": self.__volume,
            "companySymbol" : self.__companySymbol
        }
        return data

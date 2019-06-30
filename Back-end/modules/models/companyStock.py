import datetime
from modules.models.stockQuoteData import StockQuoteData

class CompanyStock(StockQuoteData):
    def __initi__(self, timeStamp : datetime = datetime.date.today(), 
                        openValue : float = 0,  
                        highValue : float = 0, 
                        lowValue : float = 0,
                        closeValue : float = 0, 
                        volume : float = 0,
                        price : float = 0,
                        change : float = 0,
                        changePercent : float = 0):

        super().__init__(timeStamp, openValue, highValue, lowValue, closeValue, volume)
        self.__price = price
        self.__change = change
        self.__changePercent = changePercent
    
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

    def toJSON(self):
        data = {
            "timeStamp"  : self.getFormatedTimeStamp(),
            "price"  : self.__price,
            "change"  : self.__change,
            "changePercent"   : self.__changePercent,
            "volume": super().getVolume()
        }
        return data

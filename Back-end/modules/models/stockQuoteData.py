import datetime

class StockQuoteData:
    def __init__(self, timeStamp : datetime = datetime.date.today(), openValue : float = 0, highValue : float = 0, lowValue : float = 0, closeValue : float = 0, volume : float = 0):
        self.__timeStamp = timeStamp
        self.__open = openValue
        self.__high = highValue
        self.__low = lowValue
        self.__close = closeValue
        self.__volume = volume
    
    def getTimeStamp(self) :
        return self.__timeStamp
    
    def setTimeStamp(self,timeStamp : datetime):
        self.__timeStamp = timeStamp
    
    def getOpenValue(self):
        return self.__open
    
    def setOpenValue(self,openValue : float):
        self.__open = openValue
    
    def getHighValue(self):
        return self.__high
    
    def setHighValue(self,highValue : float):
        self.__high = highValue
    
    def getLowValue(self):
        return self.__low
    
    def setLowValue(self,lowValue : float):
        self.__low = lowValue
    
    def getCloseValue(self):
        return self.__close
    
    def setCloseValue(self,closeValue : float):
        self.__close = closeValue
    
    def getVolume(self):
        return self.__volume
    
    def setVolume(self,volume : float):
        self.__volume = volume
    
    def getFormatedTimeStamp(self):
        return self.__timeStamp.strftime("%m-%d-%y %H:%M:%S")
    
    def toJSON(self):
        data = {
            "timeStamp"  : self.getFormatedTimeStamp(),
            "open"  : self.__open,
            "high"  : self.__high,
            "low"   : self.__low,
            "close" : self.__close,
            "volume": self.__volume
        }
        return data
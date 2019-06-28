from models.companyStock import CompanyStock

class Company:
    def __init__(self, name : str = "", symbol : str = "", region : str = "", stock : CompanyStock = CompanyStock()):
        self.__name = name
        self.__symbol = symbol
        self.__region = region
    
    def getName(self):
        return self.__name

    def setName(self, name : str):
        self.__name = name
    
    def getSymbol(self):
        return self.__symbol

    def setSymbol(self, symbol : str):
        self.__symbol = symbol
    
    def getRegion(self):
        return self.__region
    
    def setRegion(self, region : str):
        self.__region = region
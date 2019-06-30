from datetime import datetime
from modules.models.companyStock import CompanyStock

def convertDictToCompanyStock(dictionary : dict):
    stock : CompanyStock = CompanyStock()
    
    stock.setPrice(dictionary["05. price"])
    stock.setTimeStamp(datetime.strptime(dictionary["07. latest trading day"],"%Y-%m-%d"))
    stock.setVolume(dictionary["06. volume"])
    stock.setChangePercent(dictionary["10. change percent"])
    stock.setChange(dictionary["09. change"])
    return stock

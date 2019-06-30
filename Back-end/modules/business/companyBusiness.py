from datetime import datetime
from modules.models.companyStock import CompanyStock

def convertDictToCompanyStock(dictionary : dict):
    stock : CompanyStock = CompanyStock()
    
    stock.setPrice(dictionary["05. price"])
    stock.setLastUpdate(datetime.strptime(dictionary["07. latest trading day"],"%Y-%m-%d"))
    stock.setVolume(dictionary["06. volume"])
    stock.setChangePercent(dictionary["10. change percent"].split("%")[0])
    stock.setChange(dictionary["09. change"])
    stock.setCompanySymbol(dictionary["01. symbol"])
    return stock

from datetime import datetime
from modules.models.stockQuoteData import StockQuoteData
from modules.enums.stockQuoteDataEnum import StockQuoteDataEnum

# o response da api do alpha vantage retorna um json que é tratado e convertido para uma lista de dicionários
# cada dicionário corresponde a uma operação (stock quote data) em que a chave é o timestamp da operação
# e o valor é um json com as chaves e valores correspondentes às informações da operação, que são:
# valor de abertura, alta, baixa, fechamento e volume. Esta rotina converte uma entrada desse tipo de dicionário
# para um objeto da classe StockQuoteData 
def convertDictToStockQuoteDataList(dictionary : dict):
    outputList : list = []
    for key, value in dictionary.items():
        stock = StockQuoteData()
        stock.setTimeStamp(datetime.strptime(key,"%Y-%m-%d %H:%M:%S"))
        stock.setOpenValue(value[StockQuoteDataEnum.OPEN.value])
        stock.setHighValue(value[StockQuoteDataEnum.HIGH.value])
        stock.setLowValue(value[StockQuoteDataEnum.LOW.value])
        stock.setCloseValue(value[StockQuoteDataEnum.CLOSE.value])
        stock.setVolume(value[StockQuoteDataEnum.VOLUME.value])
        outputList.append(stock)
    return outputList

# a api do alpha vantage retorna uma série que pode ser além do último dia ao solicitar o intraday, assim 
# para uma série intraday do dia 26, pode haver dados dos dias 25, 24 ou até muito antes, este método retorna
# apenas a série referente ao último dia
def getOnlyLastDailyData(stockList : list):
    latStockDate : datetime = stockList[0].getTimeStamp()
    lastDaily : list = list(filter(lambda stock : ((latStockDate - stock.getTimeStamp()).total_seconds())/86400 < 1 and latStockDate.day == stock.getTimeStamp().day, stockList))
    return lastDaily
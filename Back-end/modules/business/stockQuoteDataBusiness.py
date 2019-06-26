from datetime import datetime
from models.stockQuoteData import StockQuoteData
from enums.stockQuoteDataEnum import StockQuoteDataEnum

# o response da api do alpha vantage retorna um json que é tratado e convertido para uma lista de dicionários
# cada dicionário corresponde a uma operação (stock quote data) em que a chave é o timestamp da operação
# e o valor é um json com as chaves e valores correspondentes às informações da operação, que são:
# valor de abertura, alta, baixa, fechamento e volume. Esta rotina converte uma entrada desse tipo de dicionário
# para um objeto da classe StockQuoteData 
def convertDictToStockQuoteDataList(dictionary : dict):
    outputList : list = []
    stock = StockQuoteData()
    for key, value in dictionary.items():
        stock.setTimeStamp(datetime.strptime(key,"%Y-%m-%d %H:%M:%S"))
        stock.setOpenValue(value[StockQuoteDataEnum.OPEN.value])
        stock.setHighValue(value[StockQuoteDataEnum.HIGH.value])
        stock.setLowValue(value[StockQuoteDataEnum.LOW.value])
        stock.setCloseValue(value[StockQuoteDataEnum.CLOSE.value])
        stock.setVolume(value[StockQuoteDataEnum.VOLUME.value])
        outputList.append(stock)
    return outputList
from itertools import islice
from sanic import Sanic
from sanic.response import json
from sanic_cors import CORS, cross_origin
import requests
import asyncio
import asyncpg
import aiohttp
from modules.models.supportedTimeIntervals import supportedTimeIntervals
from modules.models.stockQuoteData import StockQuoteData
from modules.models.companyStock import CompanyStock
from modules.business import stockQuoteDataBusiness
from modules.utils import config
from modules.persistance import companyPersistence
from modules.business import companyBusiness

app = Sanic(__name__)
CORS(app)

# método para retornar a série da dados do ibovespa no dia atual (intraday)
# @params: timeInterval : valor de tempo para o intervalo de dados utilizado pela api do alpha vantage
# @output: stockDataList : um JSON contendo a lista de ações diárias do ibovespa
@app.route("/bvsp-intraday/<timeInterval:int>", methods=["GET"])
async def getBvspIntraDay(request, timeInterval : int):
    try:
        validateTimeIntervalValue(timeInterval)
    except Exception as exceptionMessage:
        return json(
            {"message" : str(exceptionMessage)},
            status =  406,
        )

    parameters : str = ""
    function : str = "TIME_SERIES_INTRADAY" #parâmetro para intraday do alpha vantage
    symbol : str = "^BVSP" #símbolo para o Bovespa no alpha vantage
    interval : str = supportedTimeIntervals[timeInterval] #obtém a string reconhecida pela api do alpha vantage
    outputsize : str = "full" #série completa
    apiKey : str = config.getApiKey()
    
    #montando url para chamar a api do alpha vantage
    parameters = "function=" + function
    parameters += "&symbol=" + symbol
    parameters += "&interval=" + interval
    parameters += "&outputsize=" + outputsize
    parameters += "&apikey=" + apiKey

    response = requests.get('https://www.alphavantage.co/query?' + parameters)
    jsonResponse : dict = response.json() #em python, ao desserializar o json do response o objeto é do tipo dict
    metadata, timeStampsData = islice(jsonResponse.values(), 2)#os dados da série estão a partir do segunda valor que corresponde à chave Time Stamps 
    stockDataList : list = stockQuoteDataBusiness.convertDictToStockQuoteDataList(timeStampsData)
    stockDataList = stockQuoteDataBusiness.getOnlyLastDailyData(stockDataList)
    return json(
        {"alpha_vantage_data" : [stock.toJSON() for stock in stockDataList]}, 
        headers={'X-Served-By': 'sanic'},
        status = 200,
    )

# método para retornar a lista das 10 maiores empresas brasileiras salvas em banco
# @param: nenhum
# @output: companyList : um JSON contendo a lista das empresas com suas cotações e informações
# de acordo com os valores salvos no banco 
@app.route("/get-top-10", methods=["GET"])
async def getTop10(request):
    companyList = await companyPersistence.getTop10Companies()
    return json(
        {"empresas" : [company.toJSON() for company in companyList]}, 
        headers={'X-Served-By': 'sanic'},
        status = 200,
    )

@app.route("/get-company-stock/<companySymbol>", methods=["GET"])
async def getCompanyStock(request, companySymbol : str):
    parameters : str = ""
    function : str = "GLOBAL_QUOTE" #parâmetro para cotação de uma empresa pelo alpha vantage
    symbol : str = companySymbol #símbolo da empresa a ser consultada
    apiKey : str = config.getApiKey()
    
    #montando url para chamar a api do alpha vantage
    parameters = "function=" + function
    parameters += "&symbol=" + symbol
    parameters += "&apikey=" + apiKey

    response = requests.get('https://www.alphavantage.co/query?' + parameters)
    jsonResponse : dict = response.json() #em python, ao desserializar o json do response o objeto é do tipo dict
    stock : CompanyStock = companyBusiness.convertDictToCompanyStock(jsonResponse["Global Quote"])
    return json(
        {"stock" : stock.toJSON()},
        headers={'X-Served-By': 'sanic'},
        status = 200
    )

def validateTimeIntervalValue(value : int):
    if(value not in supportedTimeIntervals):
        raise Exception("O valor de intervalo (" + str(value) + ") é inválido. Apenas os seguintes valores são suportados: " + str(list(supportedTimeIntervals.keys())) + ".")

def start(port = 5000):
    app.run(debug = True,host="0.0.0.0", port = port)

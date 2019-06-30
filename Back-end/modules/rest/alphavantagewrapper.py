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
from modules.business import stockQuoteDataBusiness
from modules.utils import config

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
        return make_response(str(exceptionMessage), 406)

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


@app.route("/get-top-10", methods=["GET"])
async def getTop10(request):
    return json(
        {"empresas" : ""}, 
        headers={'X-Served-By': 'sanic'},
        status = 200,
    )


def validateTimeIntervalValue(value : int):
    if(value not in supportedTimeIntervals):
        raise Exception("O valor de intervalo (" + str(value) + ") é inválido. Apenas os seguintes valores são suportados: " + str(list(supportedTimeIntervals.keys())) + ".")

def start(port = 5000):
    app.run(debug = True,host="0.0.0.0", port = port)

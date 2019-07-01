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
from marshmallow import Schema, fields, ValidationError, EXCLUDE
from modules.models.companyStockSchema import CompanyStockSchema
from modules.models.companyStockAlphaSchema import CompanyStockAlphaSchema

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
            headers={'AlphaVantageAPI-Served-By': 'sanic'},
            status =  406
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
    try:
        metadata, timeStampsData = islice(jsonResponse.values(), 2)#os dados da série estão a partir do segunda valor que corresponde à chave Time Stamps 
        stockDataList : list = stockQuoteDataBusiness.convertDictToStockQuoteDataList(timeStampsData)
        stockDataList = stockQuoteDataBusiness.getOnlyLastDailyData(stockDataList)
        return json(
            {"alpha_vantage_data" : [stock.toJSON() for stock in stockDataList]}, 
            headers={'AlphaVantageAPI-Served-By': 'sanic'},
            status = 200
        )
    except:
        return json(
            {"message" : "Muitas requisições em poco tempo, considere usar uma chave Premium."}, 
            headers={'AlphaVantageAPI-Served-By': 'sanic'},
            status = 400
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
        headers={'AlphaVantageAPI-Served-By': 'sanic'},
        status = 200,
    )

# método para buscar a cotação de uma empresa dado o seu código reconhecido pela api do Alpha Vantage
# @params: companySymbol: o símbolo que identifica a empresa para qual se quer a cotação
# @output: um JSON contendo a cotação da empresa retornada pela api do Alpha Vantage
@app.route("/get-company-stock/<companySymbol>", methods=["GET"])
async def getCompanyStock(request, companySymbol : str):
    stockSchema = CompanyStockSchema(only = ("companySymbol",))
    try:
        stockSchema.load({"companySymbol" : companySymbol})
    except ValidationError as err:
        return json(
            {"error": err.messages},
            headers={'AlphaVantageAPI-Served-By':'Sanic'},
            status=400,
        )

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
    try :
        schema = CompanyStockAlphaSchema()
        res = jsonResponse["Global Quote"]
        stock = schema.load(res, unknown=EXCLUDE)
        return json(
            {"stock" : stock.toJSON()},
            headers={'AlphaVantageAPI-Served-By': 'sanic'},
            status = 200
        )
    except Exception as exceptMsg:
        return json(
            {"erros": str(exceptMsg)},
            headers={'AlphaVantageAPI-Served-By':'Sanic'},
            status=400
        )

# método para salvar em banco os dados de cotação de uma empresa
# @param: companyStock : um objeto que modela uma cotação de uma empresa
# @output: ao final do método, se não houver nada errado a cotação da empresa com código especificado
# na cotação recebeida terá seu valor salvo/alterado em banco
@app.route("/update-company-stock", methods=["PUT", "OPTIONS"])
async def updateCompanyStock(request):
    if(request.method == "PUT"):
        try:
            stockSchema  = CompanyStockSchema()
            stock = stockSchema.load(request.json)
            await companyPersistence.updateCompanyStock(stock)
            return json(
                {"message" : "Sucesso"},
                headers={'AlphaVantageAPI-Served-By': 'sanic'},
                status = 200
            )
        except Exception as exceptMsg:
            print("Erro ao atualizar cotação da empresa", str(exceptMsg))
            return json(
                {"erros": str(exceptMsg)},
                headers={'AlphaVantageAPI-Served-By':'Sanic'},
                status=400,
            )
    if(request.method != "OPTIONS"):
        return json(
            {"erros": "Método não permitido"},
            headers={'AlphaVantageAPI-Served-By':'Sanic'},
            status=405,
        )
    return json({"message" : "Success"}, status = 200)

def validateTimeIntervalValue(value : int):
    if(value not in supportedTimeIntervals):
        raise Exception("O valor de intervalo (" + str(value) + ") é inválido. Apenas os seguintes valores são suportados: " + str(list(supportedTimeIntervals.keys())) + ".")


def createApp():
    return app



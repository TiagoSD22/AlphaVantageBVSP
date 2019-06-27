from itertools import islice
from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS
from flask import jsonify
from flask import make_response
import requests
import json
from models.supportedTimeIntervals import supportedTimeIntervals
from models.stockQuoteData import StockQuoteData
from business import stockQuoteDataBusiness

app = Flask(__name__)
CORS(app)

@app.route('/bvsp-intraday/<int:timeInterval>', methods=['GET'])
def getBvspIntraDay(timeInterval : int):
    try:
        validateTimeIntervalValue(timeInterval)
    except Exception as exceptionMessage:
        return make_response(str(exceptionMessage), 406)

    parameters : str = ""
    function : str = "TIME_SERIES_INTRADAY" #parâmetro para intraday do alpha vantage
    symbol : str = "^BVSP" #símbolo para o Bovespa no alpha vantage
    interval : str = supportedTimeIntervals[timeInterval]
    outputsize : str = "full" #série completa
    apiKey : str = "M91DUVPKE0907E85" #mudar isso para um arquivo .settings ou .env
    
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
    jsonResponse = json.dumps([stock.toJSON() for stock in stockDataList])
    stockQuoteDataBusiness.getOnlyLastDailyData(stockDataList)
    return make_response(jsonResponse, 200)

def validateTimeIntervalValue(value : int):
    if(value not in supportedTimeIntervals):
        raise Exception("O valor de intervalo (" + str(value) + ") é inválido. Apenas os seguintes valores são suportados: " + str(list(supportedTimeIntervals.keys())) + ".")

if __name__ == '__main__':
   app.run(debug = True, port = 5000)
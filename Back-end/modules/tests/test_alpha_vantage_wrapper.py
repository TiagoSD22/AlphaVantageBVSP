from modules.api import alphaVantageWrapper as api
import requests
import json

app = api.createApp()

# teste de uma busca simples de intraday que deve retornar sucesso(200)
def testGetBvspIntraDay():
    request, response = app.test_client.get("/bvsp-intraday/1")
    assert response.status_code == 200.

# teste de um valor de intervalo invalido que deve retornar not_acceptable(406)
def testInvalideTimeInterval():
    request, response = app.test_client.get("/bvsp-intraday/3")
    assert response.status_code == 406

# teste para verificar se existem 10 empresas no banco
def testGetTop10():
    request, response = app.test_client.get("/get-top-10")
    assert len(response.json["empresas"]) == 10
            
# teste para checar se as empresas em banco estão corretas 
# de acordo com os dados inseridos no migration da aplicacao
def testCheckCompanies():
    request, response = app.test_client.get("/get-top-10")
    companies = [
        {"name":"Petrobras","symbol":"PETR4.SAO","region":"Rio de Janeiro, Rio de Janeiro",
        "rank":1,"sector":"Petróleo e gás"},
        {"name":"Itaú Unibanco","symbol":"ITUB4.SAO","region":"São Paulo, São Paulo",
        "rank":2,"sector":"Bancário"},
        {"name":"Banco Bradesco","symbol":"BBDC4.SAO","region":"Osasco, São Paulo",
        "rank":3,"sector":"Bancário"},
        {"name":"Vale","symbol":"VALE3.SAO","region":"Rio de Janeiro, Rio de Janeiro",
        "rank":4,"sector":"Mineração"},
        {"name":"Banco do Brasil","symbol":"BBAS3.SAO","region":"Brasília, Distrito Federal",
        "rank":5,"sector":"Bancário"},
        {"name":"Eletrobras","symbol":"ELET6.SAO","region":"Rio de Janeiro, Rio de Janeiro",
        "rank":6,"sector":"Energia elétrica"},
        {"name":"JBS","symbol":"JBSS3.SAO","region":"São Paulo, São Paulo",
        "rank":7,"sector":"Alimentício"},
        {"name":"Itaúsa","symbol":"ITSA4.SAO","region":"Brasil",
        "rank":8,"sector":"Finanças e indústria"},
        {"name":"Braskem","symbol":"BRKM5.SAO","region":"São Paulo, São Paulo",
        "rank":9,"sector":"Petroquímica"},
        {"name":"Oi","symbol":"OIBR-C","region":"Rio de Janeiro, Rio de Janeiro",
        "rank":10,"sector":"Telecomunicações"}]
    companiesRes = response.json["empresas"]
    for company in companiesRes:
        del company["stock"]
    assert companies == companiesRes

# teste para obter a cotacao de uma empresa valida que deve retornar sucesso(200)
def testGetCompanyStock():
    request, response = app.test_client.get("/get-company-stock/BBDC4.SAO")
    assert response.status_code == 200

# teste para obter uma cotacao de uma empresa invalida que deve retornar bad_request(400)
def testGetInvalidCompanyStock():
    request, response = app.test_client.get("/get-company-stock/XYZ")
    assert response.status_code == 400

# teste para atualizar a cotacao de uma empresa invalida, pois o simbolo nao e reconhecido 
# e que deve retornar bad_request(400)
def testUpdateInvalidCompanyStock():
    stock = {
        "lastUpdate":"06-28-19",
        "price":27.41,
        "change":0.18,
        "changePercent":"0.6610",
        "volume":39848200,
        "companySymbol":"XYZ" #simbolo invalido
    }
    request, response = app.test_client.put("/update-company-stock/", data=json.dumps(stock))
    assert response.status_code == 400

# teste para atualizar a cotacao de uma empresa valida, porem a cotacao e invalida, pois faltam 
# alguns campos anotados com required(volume,price) e que deve retornar bad_request(400)
def testUpdateCompanyInvalidStock():
    stock = {
        "lastUpdate":"06-28-19",
        "change":0.18,
        "changePercent":"0.6610",
        "companySymbol":"BBDC4.SAO"
    }
    request, response = app.test_client.put("/update-company-stock/", data=json.dumps(stock))
    assert response.status_code == 400 

# teste para atualizar a cotacao de uma empresa valida com cotacao valida
# e que deve retornar sucesso(200)
def testUpdateCompanyStock():
    stock = {
        "lastUpdate":"06-28-19",
        "price":27.41,
        "change":0.18,
        "changePercent":"0.6610",
        "volume":39848200,
        "companySymbol":"BBDC4.SAO"
    }
    request, response = app.test_client.put("/update-company-stock/", data=json.dumps(stock))
    assert response.status_code == 200

    

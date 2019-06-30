import datetime
import asyncio
import asyncpg
from asyncpg.connection import Connection
from datetime import datetime
from modules.utils import config
from modules.persistance import connectionFactory
from modules.models.company import Company
from modules.models.companyStock import CompanyStock

async def getTop10Companies():
    try:
        conn = await connectionFactory.getDBDriverConnection()
        resultSet = list(await conn.fetch('''
            select e.nome as nome, e.simbolo_empresa as simbolo, 
            e.regiao as regiao, e.setor as setor, e.rank as rank, 
            c.preco as preco, c.volume as volume, c.data as dt_u_a, c.variacao as var, c.variacao_por_cento as vp 
            from empresas e left join cotacoes c on e.simbolo_empresa = c.simbolo_empresa;
        '''))
        companyList : list = []
        for item in resultSet:
            dic = dict(item)
            company : Company = Company()
            company.setName(dic["nome"])
            company.setRank(dic["rank"])
            company.setRegion(dic["regiao"])
            company.setSector(dic["setor"])
            company.setSymbol(dic["simbolo"])
            stock : CompanyStock = CompanyStock()
            stock.setChange(dic["var"])
            stock.setChangePercent(dic["vp"])
            stock.setPrice(dic["preco"])
            stock.setLastUpdate(dic["dt_u_a"])
            stock.setVolume(dic["volume"])
            stock.setCompanySymbol(company.getSymbol())
            company.setStock(stock)
            companyList.append(company)

        await conn.close()
        return companyList
    except Exception as exceptMsg:
        print("Falha ao obter lista de empresas top 10.", str(exceptMsg))

async def hasStockData(companySymbol : str):
    conn = await connectionFactory.getDBDriverConnection()
    dataSize : int = await conn.fetchval('''
        SELECT COUNT(*) FROM cotacoes c WHERE c.simbolo_empresa = $1
    ''',companySymbol)

    await conn.close()
    if(dataSize > 0):
        return True
    return False
    
async def updateCompanyStock(stock : CompanyStock):
    hasData = await hasStockData(stock.getCompanySymbol())
    conn = await connectionFactory.getDBDriverConnection()
    if(hasData):
        async with conn.transaction():
            await conn.execute('''
                UPDATE cotacoes SET preco = $1, volume = $2, data = $3, 
                variacao = $4, variacao_por_cento = $5 WHERE simbolo_empresa = $6
                ''',
                stock.getPrice(), stock.getVolume(), 
                stock.getLastUpdate(), stock.getChange(),
                stock.getChangePercent(), stock.getCompanySymbol())
    else:
        async with conn.transaction():
            await conn.execute('''
                INSERT INTO cotacoes VALUES($1, $2, $3, $4, $5, $6)
                ''',
                stock.getPrice(), stock.getVolume(), 
                stock.getLastUpdate(), stock.getChange(),
                stock.getChangePercent(), stock.getCompanySymbol())
    await conn.close()
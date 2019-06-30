import datetime
import asyncio
import asyncpg
from asyncpg.connection import Connection
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
            c.fechamento as preco, c.data as dt_u_a, c.variacao as var, c.variacao_por_cento as vp 
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
            companyStock : CompanyStock = CompanyStock()
            companyStock.setChange(dic["var"])
            companyStock.setChangePercent(dic["vp"])
            companyStock.setPrice(dic["preco"])
            companyStock.setTimeStamp(dic["dt_u_a"])
            company.setStock(companyStock)
            companyList.append(company)

        await conn.close()
        return companyList
    except Exception as exceptMsg:
        print("Falha ao obter lista de empresas top 10.", str(exceptMsg))
import asyncio
import asyncpg
from asyncpg.connection import Connection
from modules.utils import config

async def init():
    try:
        conn = await asyncpg.connect('postgresql://' + config.getDBUser() + "@localhost/" + config.getDBName(), password=config.getDBPwd())
        await createUserTable(conn)
        await createCompanyTable(conn)
        await createStockTable(conn)
        companiesQuantity = await getCompaniesQuantity(conn)
        if(companiesQuantity != 10):
            print("Tabela de empresas com menos de 10 registros (",companiesQuantity,"), inserindo dados das maiores empresas brasileiras.")
            await insertTop10Companies(conn)
        await conn.close()
        return True
    except Exception as exceptMsg:
        print(exceptMsg)
        return False

async def createUserTable(connection : Connection):
    async with connection.transaction():
        await connection.execute('''
            CREATE TABLE IF NOT EXISTS usuarios(
                id bigserial PRIMARY KEY NOT NULL,
                nome character varying(50) NOT NULL,
                login character varying(20) NOT NULL UNIQUE
            )'''
        )

async def createCompanyTable(connection : Connection):
    async with connection.transaction():
        await connection.execute('''
            CREATE TABLE IF NOT EXISTS empresas(
                id bigserial PRIMARY KEY NOT NULL,
                nome character varying(50) NOT NULL,
                simbolo character varying(20) NOT NULL UNIQUE,
                regiao character varying(50),
                setor character varying(20),
                rank int
            )'''
        )

async def createStockTable(connection : Connection):
    async with connection.transaction():
        await connection.execute('''
            CREATE TABLE IF NOT EXISTS cotacoes(
                abertura float(3),
                fechamento float(3),
                alta float(3),
                baixa float(3),
                volume bigint,
                data timestamp without time zone,
                simbolo_empresa character varying(20) NOT NULL,
                CONSTRAINT cotacao_fk FOREIGN KEY(simbolo_empresa) REFERENCES empresas(simbolo)
            )'''
        )

async def getCompaniesQuantity(connection : Connection):
    quantity : int = await connection.fetchval('''
        SELECT COUNT(*) from empresas
        '''
    )
    return quantity

async def insertTop10Companies(connection : Connection):
    async with connection.transaction():
        await connection.execute('''
            DELETE FROM empresas
            '''
        )
        
        await connection.copy_records_to_table(
            "empresas", records = [
                (1, "Oi", "OIBR-C", "Rio de Janeiro, Rio de Janeiro", "Telecomunicações", 10),
                (2, "Braskem", "BRKM5.SAO", "São Paulo, São Paulo", "Petroquímica", 9),
                (3, "Itaúsa", "ITSA4.SAO", "Brasil", "Finanças e indústria", 8),
                (4, "JBS", "JBSS3.SAO", "São Paulo, São Paulo", "Alimentício", 7),
                (5, "Eletrobras", "ELET6.SAO", "Rio de Janeiro, Rio de Janeiro", "Energia elétrica", 6),
                (6, "Banco do Brasil", "BBAS3.SAO", "Brasília, Distrito Federal", "Bancário", 5),
                (7, "Vale", "VALE3.SAO", "Rio de Janeiro, Rio de Janeiro", "Mineração", 4),
                (8, "Banco Bradesco", "BBDC4.SAO", "Osasco, São Paulo", "Bancário", 3),
                (9, "Itaú Unibanco", "ITUB4.SAO", "São Paulo, São Paulo", "Bancário", 2),
                (10, "Petrobras", "PETR4.SAO", "Rio de Janeiro, Rio de Janeiro", "Petróleo e gás", 1)
        ])

    



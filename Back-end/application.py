import asyncio
from modules.persistance import migration
from modules.api import alphaVantageWrapper as api
from modules.utils import config

if __name__ == "__main__":
    result : bool = asyncio.run(migration.init())
    if(result):
        print("Iniciando API")
        app = api.createApp()
        host = config.getApplicationHost()
        debug = config.getApplicationDebug()
        port = config.getApplicationPort()
        app.run(host=host, debug=debug, port=port)
    else:
        print("Falha ao realizar migração do bando de dados, não foi possível iniciar a aplicação.")
import asyncio
from modules.persistance import migration
from modules.api import alphaVantageWrapper as api

if __name__ == "__main__":
    result : bool = asyncio.run(migration.init())
    if(result):
        app = api.createApp()
        app.run(debug=False, port=5000)
    else:
        print("Falha ao realizar migração do bando de dados, não foi possível iniciar a aplicação.")
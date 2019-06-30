import asyncio
from modules.persistance import migration

from modules.rest import alphavantagewrapper as app

if __name__ == "__main__":
    result : bool = asyncio.run(migration.init())
    if(result):
        app.start(5000)
    else:
        print("Falha ao realizar migração do bando de dados, não foi possível iniciar a aplicação.")
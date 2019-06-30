import configparser

def getApiKey():
    config = configparser.ConfigParser()
    config.read("config.ini")
    key = config["api"]["key"]
    return key

def getDBUser():
    config = configparser.ConfigParser()
    config.read("config.ini")
    user = config["database"]["user"]
    return user

def getDBName():
    config = configparser.ConfigParser()
    config.read("config.ini")
    name = config["database"]["name"]
    return name

def getDBPwd():
    config = configparser.ConfigParser()
    config.read("config.ini")
    password = config["database"]["password"]
    return password

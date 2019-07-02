import configparser

def getApplicationHost():
    config = configparser.ConfigParser()
    config.read("config.ini")
    host = config["application"]["host"]
    return host

def getApplicationPort():
    config = configparser.ConfigParser()
    config.read("config.ini")
    port = config["application"]["port"]
    return port

def getApplicationDebug():
    config = configparser.ConfigParser()
    config.read("config.ini")
    debug = config["application"]["debug"]
    return debug

def getApiKey():
    config = configparser.ConfigParser()
    config.read("config.ini")
    key = config["api"]["key"]
    return key

def getDBLocation():
    config = configparser.ConfigParser()
    config.read("config.ini")
    location = config["database"]["location"]
    return location

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

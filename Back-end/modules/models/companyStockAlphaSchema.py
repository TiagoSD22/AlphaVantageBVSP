from marshmallow import Schema, fields, post_load, validates, ValidationError
from modules.models.companyStock import CompanyStock

class CompanyStockAlphaSchema(Schema):
    price = fields.Float(required=True, data_key = "05. price")
    volume = fields.Int(required=True, data_key = "06. volume")
    lastUpdate = fields.DateTime(format="%Y-%m-%d", required=True, data_key = "07. latest trading day")
    change = fields.Float(required=True, data_key = "09. change")
    changePercentStr = fields.Str(required=True, data_key = "10. change percent")
    companySymbol = fields.Str(required=True, data_key= "01. symbol")

    @post_load
    def loadStock(self, data, **kwargs):
        return CompanyStock(**data)
from marshmallow import Schema, fields, post_load, validates, ValidationError
from modules.models.companyStock import CompanyStock
from modules.enums.companyEnum import CompanyEnum

class CompanyStockSchema(Schema):
    price = fields.Float(required=True)
    volume = fields.Int(required=True)
    lastUpdate = fields.DateTime(format="%m-%d-%y", required=True)
    change = fields.Float(required=True)
    changePercent = fields.Float(required=True)
    companySymbol = fields.Str(required=True)

    @post_load
    def dumpStock(self, data, **kwargs):
        return CompanyStock(**data)

    @validates('companySymbol')
    def validateCompanySymbol(self, symbol : str):
        if(symbol not in set(item.value for item in CompanyEnum)):
            raise ValidationError('Símbolo não reconhecido!')
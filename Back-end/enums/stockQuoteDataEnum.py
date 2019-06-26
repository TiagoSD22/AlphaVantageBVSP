from enum import Enum

class StockQuoteDataEnum(Enum):
    OPEN   = "1. open"
    HIGH   = "2. high"
    LOW    = "3. low"
    CLOSE  = "4. close"
    VOLUME = "5. volume"
from scrapy.item import Item, Field

class FIIs(Item):
  
    code = Field()
    sector = Field()
    actual_price = Field()
    liquidity = Field()
    dividend = Field()
  
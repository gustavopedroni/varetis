import scrapy
from src.utils import get_logger
from src.scrawlers.items import FIIs


class FundsExplorerSpider(scrapy.Spider):
  
    name = 'Funds Explorer Spider'
    logger = get_logger('Funds Explorer')
  
    allowed_domains = ['fundsexplorer.com.br']
    start_urls = [
      'https://fundsexplorer.com.br/ranking'
    ]
  
    custom_settings = {
      'ITEM_PIPELINES': {
        'src.scrawlers.pipelines.JsonWriterPipeline': 900
      }
    }
  
    def parse(self, response):
        self.logger.info('Response arrived!')
    
        rows = response.xpath('//*[@id="table-ranking"]//tbody//tr')

        self.logger.info(f'Found {len(rows)}')
    
        for row in rows:
            
            item = FIIs()
            item['code'] = row.xpath('td[1]/a/text()').get()
            
            yield item

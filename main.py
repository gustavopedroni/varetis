import os
import click
from scrapy.crawler import CrawlerProcess

pass_process = click.make_pass_decorator(CrawlerProcess, ensure=True)

@click.group()
@click.option('--debug/--no-debug')
def cli(debug=False):
    os.environ['debug'] = 'TRUE' if debug else 'FALSE'

@cli.command()
@pass_process
def scrape_fiis(process, *args, **kwargs):
    """ Scrape data from https://fundsexplorer.com.br/
    """
    from src.scrawlers.spiders.funds_explorer import FundsExplorerSpider
    process.crawl(FundsExplorerSpider)
    process.start()    

if __name__ == '__main__':
    cli()
    
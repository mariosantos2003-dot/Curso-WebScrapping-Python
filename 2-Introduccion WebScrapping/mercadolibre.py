# importamos todo lo necesario de la biblioteca de scrapy
from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from bs4 import BeautifulSoup


# cREAMOS LA CLASE SOBRE LO QUE VAMOS A BUSCAR
class Articulo(item):
    titulo = Field()
    descripcion = Field()


class MercadoLibreCrawler(CrawlSpider):
    name = 'mercadolibre'

    custom_settings = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    'CLOSESPIDER_PAGECOUNT': 10  # numero de paginas a descargar items, se cierra scrappy al llegar ahi
    }

    # DOMINIOS DONDE VAMOS A BUSCAR
    allowed_domains = ['articulo.mercadolibre.com.pe' , 'listado.mercadolibre.com.pe']
    # URL DEL SITIO
    start_urls = ['https://listado.mercadolibre.com.pe/celulares-smartphones']

    download_delay = 1

    #CREAMOS UNA TUPLA DONDE ALMACENAMOS LAS REGLAS
    rules = (
        #UNA REGLA SIRVE PARA QUE CUANDO BUSQUEMOS , RECOJA LOS PARAMETROS QUE CONTENGAN LAS REGLAS QUE LE INDICAMOS
            Rule(
        LinkExtractor(
            allow=r'/_Desde_\d+'
    ), follow=True),
    Rule(
        LinkExtractor(
            allow=r'/MPE+'
    ), follow=True, callback='parse_items'),

    )

    def parse_items(self, response):
        item = ItemLoader(Articulo(), response)

        item.add_xpath('titulo' , '//h1/text()')
        item.add_xpath('descripcion' , '//p[@class="ui-pdp-description__content"]/text()')

        yield item.load_item()

    

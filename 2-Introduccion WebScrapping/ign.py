from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader


class Articulo(Item):
    titulo = Field()
    contenido = Field()


class Reviews(Item):
    titulo = Field()
    calificacion = Field()


class Video(Item):
    titulo = Field()
    fecha_de_publicacion = Field()


class IGNCrawler(CrawlSpider):
    name = 'ign'

    custom_settings = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    'CLOSESPIDER_PAGECOUNT': 20  # numero de paginas a descargar items, se cierra scrappy al llegar ahi
    }  # DOMINIOS DONDE VAMOS A BUSCAR
    allowed_domains = ['latam.ign.com']

    start_url = ['https://latam.ign.com/se/?model=article&q=ps4']

    dowload_delay = 1

    rules = (

        Rule(
            LinkExtractor(
                allow=r'type='
                ), follow=True),
        Rule(
            LinkExtractor(
                allow=r'/review/'
            ), follow=True, callback='parse_review'),
        Rule(
            LinkExtractor(
                allow=r'/video/'
            ), follow=True, callback='parse_video'),
        Rule(
            LinkExtractor(
                allow=r'/news/'
            ), follow=True, callback='parse_news')
        )
    

    def parse_video(self,response):
        item= ItemLoader(Video(),response)
        item.add_xpath('titulo','//h1/text()')
        item.add_xpath('fecha_de_publicacion','//span[@class="pulish-date"]/text()')

        yield item.load_item()
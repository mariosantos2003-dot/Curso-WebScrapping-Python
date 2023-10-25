#importamos todo lo necesario de la biblioteca de scrapy
from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.loader import ItemLoader


# scrapy runspider stackoverflow-scrap.py -O result.json -t json
#scrapy runspider stackoverflow-scrap.py -O result.json:json

#creamos la clase pregunta donde entra la pregunta y la descripcion
class Pregunta(Item):
    pregunta = Field()
    descripcion = Field()

#creamos la araña para que recoja los datos de la web
class StackOverFlowSpider(Spider):
    name = "miPrimerSpider" 
    # USER AGENT CONTRA BANEOS
    custom_settings = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
    }
    #url
    start_urls=['https://www.igrupos.com/whatsapp']
    #con el parse recogemos lo que queremos
    def parse(self , response):

        sel = Selector(response)
        #donde tiene que ir a buscar las preguntas
        preguntas=sel.xpath('//div[@class="media-body"]')

        #bucle for para que nos muestre todas las preguntas de la pagina
        for pregunta in preguntas:
            #con el item cargamos tanto la pregunta como la descripcion
            item = ItemLoader(Pregunta(), pregunta)
            item.add_xpath('pregunta' , './/a/span/text()')
            item.add_xpath('descripcion' , './/a/text()')
            #ejecutamos la busqueda
            yield item.load_item()

            
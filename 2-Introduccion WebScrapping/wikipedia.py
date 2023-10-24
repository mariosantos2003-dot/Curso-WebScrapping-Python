import requests
from lxml import html
#aqui creamos el usuario para que no piense que eres un robot
encabezado={
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
    
    
}

#url de la web para hacer scrapping
url="https://www.wikipedia.org/"

#peticion mediantes metodo get, headers sirve para que la pagina web que vas a hacer scrapp, no se crea que eres un robot
respuesta= requests.get(url,headers=encabezado)

#imprimira todo el contenido html y css de la pagina que le pasemos
#print(respuesta.text)

#para buscar un id concrecto dentro de la pagina
#metodo 1
#con esta biblioteca, podemos parsear directamente el texto de la pagina
parser = html.fromstring(respuesta.text)

#para parsear un id concrecto de la pagina
espanol = parser.get_element_by_id("js-link-box-es")

#para imprimir lo que esta dentro del id
print(espanol.text_content())

#metodo 2
#con este segundo metodo podemos hacer que nos pase exclusivamente el texto, dentro del xpath indicaremos la ruta general "//" el tipo de etiqueta que estamos buscando "a" con su id, dentro de la etiqueta despues de / indicaremos exactamente el hijo que queremos que nos imprima y el formato "text()"
spanish = parser.xpath("//a[@id='js-link-box-es']/strong/text()")

print(spanish)

#ejemplo, sacar todos los idiomas a partir de parsear por clase

idiomas= parser.xpath("//div[contains(@class,'central-featured-lang')]//strong/text()")

for idioma in idiomas:
    print(idioma)
import requests
from bs4 import BeautifulSoup

#USER AGENT CONTRA BANEOS
headers={
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
    
    
}

url="https://stackoverflow.com/questions"


#petitcion al servidor
respuesta = requests.get(url,headers=headers)


#PARSEO CON BS4
soup = BeautifulSoup(respuesta.text)

#buscamos dentro del codigo el id llamado question
contenedor_de_preguntas = soup.find(id="questions")

#buscamos dentro del id question todos las etiquetas que contengan en su div una clase llamada s-post-summary
lista_preguntas =contenedor_de_preguntas.find_all('div',class_="s-post-summary")

#ejecutamos un bucle for para que nos devuelvan todas las etiquetas h3 dentro del div
for pregunta in lista_preguntas:
    titulo_pregunta= pregunta.find('h3').text
    descripcion_pregunta=pregunta.find(class_='s-post-summary--content-excerpt').text
    #para cambiar los saltos de linea y que quede mas limpio el texto
    descripcion_pregunta=descripcion_pregunta.replace('\n', '').replace('\r', 'v ')
    print(titulo_pregunta)
    print(descripcion_pregunta)
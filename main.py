from wordcloud import WordCloud
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np

#URL (Esta parte hay q cambiarla, se debe ingresar la URL y que busque al usuario)
url = "https://es.stackoverflow.com/users/22851/pablo-lozano?tab=tags"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')


#Scrapping de etiquetas
et = soup.find_all('a', class_='post-tag')
frec = soup.find_all('span', class_='item-multiplier-count')

#lista etiquetas
etiquetas = list()
for i in et:
    etiquetas.append(i.text)

#lista frecuencia de etiquetas
frecuencia = list()
for i in frec:
    frecuencia.append(i.text)

#Se comprueba que la cantidad de etiquetas y valores de frecuencia sea el mismo (Esta parte se tendra que quitar)
print(etiquetas)
print(len(etiquetas))
print(frecuencia)
print(len(frecuencia))

#La lista etiquetas pasa a texto (Hay que cambiar esta parte ya que no se toma en cuenta la frecuencia para hacer el WordCloud y deben tomarse en cuenta)
text= " ".join(etiquetas)

#Se genera el WordCloud con las etiquetas
cloud = WordCloud(background_color="white").generate(text)

#Se presenta el WordCloud
plt.imshow(cloud)
plt.axis('off')
plt.show()

from wordcloud import WordCloud
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
from PIL import Image

#URL del perfil con las etiquetas de SO (Esta parte hay q cambiarla, se debe ingresar la URL y que busque al usuario)

url = "https://es.stackoverflow.com/users/22851/pablo-lozano?tab=tags"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

#Scrapping de etiquetas
et = soup.find_all('a', class_='post-tag')
frec = soup.find_all('span', class_='item-multiplier-count')

#lista etiqueta
etiquetas = list()
for i in et:
    etiquetas.append(i.text)

#lista frecuencia de etiquetas
frecuencia = list()
for i in frec:
    #Aquí añadimos int() porque el método generate_from_frequencies() necesita enteros no string
    frecuencia.append(int(i.text))

#Aquí utilizamos zip para unir las etiquetas con sus repsectivas frecuencias
etfrecuencias = dict(zip(etiquetas, frecuencia))

#Se establece que imagen se usara para el WordCloud
custom_mask = np.array(Image.open("mancha.jpg"))

#Utilizamos el método .generate_from_frequencies pasandole las frecuencias
cloud = WordCloud(background_color="black",scale=2,relative_scaling=0.1, mask=custom_mask,contour_width=1, contour_color='steelblue').generate_from_frequencies(etfrecuencias)

#Se guarda la imagen
cloud.to_file('wcloud.png')

#Se presenta el WordCloud
plt.figure()
plt.imshow(cloud, interpolation="bilinear")
plt.axis("off")
plt.show()

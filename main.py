from wordcloud import WordCloud
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
from PIL import Image

# Ingreso de ID de usuario de StackOverflow por teclado
print("Introduzca la ID del usuario: ")
ID = input()

# Se obtiene la pagina de etiquetas a partir de la URL del usuario
url = f'https://es.stackoverflow.com/users/{ID}?tab=tags'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

# Scrapping de etiquetas
et = soup.find_all('a', class_='post-tag')
frec = soup.find_all('span', class_='item-multiplier-count')

# lista etiqueta
etiquetas = list()
for i in et:
    etiquetas.append(i.text)
# Hay veces en las que un perfil muestra la etiqueta principal y al tomar los datos esa etiqueta queda repetida.
# Con este if nos aseguramos que en caso de que se este tomando una etiqueta principal, esta se elimina para que no cause irregularidades.
if etiquetas[0] == etiquetas[1]:
    etiquetas.pop(0)

# lista frecuencia de etiquetas
frecuencia = list()
for i in frec:
    # Aquí añadimos int() porque el método generate_from_frequencies() necesita enteros no string
    frecuencia.append(int(i.text))

# Aquí utilizamos zip para unir las etiquetas con sus repsectivas frecuencias
etfrecuencias = dict(zip(etiquetas, frecuencia))

# Se establece que imagen se usara para el WordCloud, descomentar linea de código siguiente si esque se usa imagen
custom_mask = np.array(Image.open("mancha.jpg"))

# Utilizamos el método .generate_from_frequencies pasandole las frecuencias

# Con imagen "mancha.jpg"
cloud = WordCloud(background_color="black", scale=2, relative_scaling=0.1, mask=custom_mask, contour_width=1, contour_color='steelblue').generate_from_frequencies(etfrecuencias)

# Sin imagen "mancha.jpg", si se utiliza esto hay q comentar el cloud anterior y el custom_mask
#cloud = WordCloud(background_color="black", scale=2, relative_scaling=0.1, contour_width=1,contour_color='steelblue').generate_from_frequencies(etfrecuencias)

# Se guarda la imagen
cloud.to_file('wcloud.png')

# Se presenta el WordCloud
plt.figure()
plt.imshow(cloud, interpolation="bilinear")
plt.axis("off")
plt.show()

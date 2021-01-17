from bs4 import BeautifulSoup
import requests
import pandas as pd
url = "https://es.stackoverflow.com/users/153371/franacuna?tab=tags"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

#etiquetas
et = soup.find_all('a', class_='post-tag')

etiquetas = list()

for a in et:
    etiquetas.append(a.text)

print(etiquetas)
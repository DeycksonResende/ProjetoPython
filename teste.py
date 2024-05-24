from flask import Flask, render_template, request
import requests
import bs4
from flask_cors import CORS



app = Flask(__name__)
CORS(app)



@app.route('/')
def raspa_veja():
    response = requests.get('https://veja.abril.com.br/')
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    mais_lidas = soup.find_all('section', {'class': 'block most-read dark'})
    conteudos = mais_lidas[0].find_all('div', {'class': 'our-carousel-item'})
    noticias = []

    for conteudo in conteudos:
        titulo = conteudo.find('h2').text
        link = conteudo.find('a').get('href')
        noticias.append((titulo, link)) 
    print(noticias)


raspa_veja()
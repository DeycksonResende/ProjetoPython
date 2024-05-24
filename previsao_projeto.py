from flask import Flask, render_template, request
import requests
import bs4
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Busca de previsões do tempo
        cidade = request.form.get('cidade')
        with open('./ProjetoPython/api_keys.txt', 'r') as f:
            key = f.read()
        url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={key}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            temperatura_min = data["main"]["temp_min"]
            temperatura_max = data["main"]["temp_max"]
            pressure = data['main']['pressure']
            humidity = data['main']['humidity']
            clouds = data['wind']['speed']
            name = data["name"]
            
            # Raspagem de notícias
            response_news = requests.get('https://veja.abril.com.br/')
            soup = bs4.BeautifulSoup(response_news.text, 'html.parser')
            mais_lidas = soup.find_all('section', {'class': 'block most-read dark'})
            conteudos = mais_lidas[0].find_all('div', {'class': 'our-carousel-item'})
            noticias = []

            for conteudo in conteudos:
                titulo = conteudo.find('h2').text
                link = conteudo.find('a').get('href')
                noticias.append((titulo, link))

            return render_template('pagina_pesquisa.html', min=temperatura_min, nome=name, max=temperatura_max, pressão=pressure, umidade=humidity, nuvens=clouds, notícias=noticias)
        else:
            return "Erro ao buscar dados da API", 400
    else:
        
        return render_template('pagina_pesquisa.html')  


if __name__ == '__main__':
    app.run(debug=True)
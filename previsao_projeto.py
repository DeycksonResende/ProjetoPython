from flask import Flask, render_template, request
import requests
import bs4



app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        cidade = request.form['text']
        with open('./ProjetoPython/api_keys.txt', 'r') as f:
            key = f.read()
        url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={key}&units=metric"
<<<<<<< HEAD
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            temperatura = data["main"]["temp"]
            name = data["name"]
            humidity = data["main"]["humidity"]
           
            return render_template('pagina_pesquisa.html', weather_data = temperatura, nome = name, umidade = humidity)
=======
        print("Passou")
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            temperatura = data["main"]
            name = data["name"]
            return render_template('pagina_pesquisa.html', weather_data=temperatura, nome = name)
>>>>>>> a8293d9911010823ab7ac89c453ae173ad9970ff
        else:
            return "Erro ao buscar dados da API", 400
    else:
        return render_template('pagina_pesquisa.html')



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
        noticias.append(f"{titulo}\n{link}")
    return render_template('pagina_pesquisa.html', resultado = "\n\n".join(noticias))


if __name__ == '__main__':
    app.run(debug=True)
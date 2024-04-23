from flask import Flask, render_template, request
import requests


app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    cidade = request.form['name']
    with open('api_keys.txt', 'r') as f:
        key = f.read()
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return render_template('pagina_pesquisa.html', weather_data=data)
    else:
        return "Erro ao buscar dados da API", 400

@app.route('/noticias')
def noticias():
    return render_template('pagina_noticias')

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    cidade = request.form['name']
    api_key = "8b08d97d1c73496296b98abf0ba86b82" # Mover para variáveis de ambiente
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}"
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

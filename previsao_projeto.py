from Flask import Flask, render_template, request
import requests

app = Flask(__name__)



@app.route('/', )
def index():
    cidade = request.form['name']
    url = "http://api.openweathermap.org/data/2.5/weather?q={cidade} &appid=8b08d97d1c73496296b98abf0ba86b82"
    response = requests.get(url)
    return render_template('pagina_pesquisa.html')



@app.route('/noticias')
def noticias():
    
    return render_template('pagina_noticias')
from flask import Flask, render_template, request, flash, redirect, url_for
import requests

app = Flask(__name__)
app.secret_key = "mysecret"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city_name = request.form['name']
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID=Your API Key here'
        response = requests.get(url.format(city_name)).json()
        
        if 'main' in response and 'weather' in response:
            temp = response['main']['temp']
            weather = response['weather'][0]['description']
            min_temp = response['main']['temp_min']
            max_temp = response['main']['temp_max']
            icon = response['weather'][0]['icon']
            return render_template('index.html', temp=temp, weather=weather, min_temp=min_temp, max_temp=max_temp, icon=icon, city_name=city_name)
        else:
            flash('Error fetching data. Please try again later.', 'error')
            return redirect(url_for('index'))

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)

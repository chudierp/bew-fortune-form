from flask import Flask, render_template, request
import requests
import pprint

app = Flask(__name__)

pp = pprint.PrettyPrinter(indent=4)
weather_url = "https://api.openweathermap.org/data/2.5/weather"

@app.route('/')
def index():
    """Renders the home page with links to Fortune and Weather."""
    return render_template('index.html')

@app.route('/fortune')
def fortune_form():
    """Displays fortune teller form"""
    return render_template('fortune_form.html')

@app.route('/fortune_results')
def fortune_results():
    """Displays the user's fortune."""
    users_favorite_animal = request.args.get('animal')
    # ... etc

    if users_favorite_animal == 'dog':
        fortune = "Change can hurt, but it leads a path to something better."
    
    elif users_favorite_animal == 'cat':
        fortune = "People are naturally attracted to you." 
    
    elif users_favorite_animal == "reptile":
        fortune = "What ever you're goal is in life, embrace it visualize it, and for it will be yours."
    
    elif users_favorite_animal == 'bird':
        fortune = "Be on the lookout for coming events; They cast their shadows beforehand."
    
    elif users_favorite_animal == 'aquatic':
        fortune = "A dream you have will come true."

    elif users_favorite_animal == 'wild':
        fortune = "Serious trouble will bypass you."    

    else:
        fortune = "good luck in life!"

    return render_template('fortune_results.html', fortune=fortune)

@app.route('/weather')
def weather_form():
    """ display the weather form page"""
    return render_template('weather_form.html') 

@app.route('/weather_results')
def weather_results_page():
    users_city = request.args.get('city')
   
    params = {
        'q': users_city,
        'appid': '2608f679d4594364525f6c6cc2246c79'
    }

    response = requests.get(weather_url, params=params)

    if not response.status_code == 200:
        print("error")
    results = response.json()
    
    city = results['name']
    temp = kelvin_to_farenheit(results['main']['temp'])
    
    return render_template('weather_results.html', city=city, temp=temp)

def kelvin_to_farenheit(k):
    results = 1.8 * (k-273) + 32
    return int(results)

if __name__ == '__main__':
    app.run()

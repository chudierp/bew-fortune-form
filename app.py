from flask import Flask, render_template, request

app = Flask(__name__)

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
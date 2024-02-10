
from flask import request, Flask, render_template
import random
import psycopg2

app = Flask(__name__, template_folder='templates')

# Sample data
adjectives = ["strong", "weak", "cold", "warm", "wise", "brave", "clever", "kind", "funny"]

def generate_sentence():
    adjective = random.choice(adjectives)
    name = request.form['name']
    year = request.form['year']
    city = request.form['city']
    return f"{name} the {adjective} was born in {city} in {year}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_sentence', methods=['POST'])
def random_sentence():
    sentence = generate_sentence()
    return render_template('random_sentence.html', sentence=sentence)


if __name__ == '__main__':
    my_port = 5123
    app.run(host='0.0.0.0', port = my_port)

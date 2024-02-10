from flask import request, Flask, render_template
import random
import psycopg2

app = Flask(__name__, template_folder='templates')

# Sample data
adjectives = ["strong", "weak", "cold", "warm", "wise", "brave", "clever", "kind", "funny"]

# Connect to PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="choir",
    user="choir",
    password="spam889books"
)

def generate_sentence():
    try:
        cursor = conn.cursor()
        
        # Retrieve form data
        name = request.form['name']
        year = request.form['year']
        city = request.form['city']

        # Query population for the city
        query_population = "SELECT population FROM city_population WHERE city = %s"
        cursor.execute(query_population, (city,))
        population = cursor.fetchone()

        if population:
            adjective = random.choice(adjectives)
            sentence = f"{name} the {adjective} was born in {city} in {year}. Population of {city}: {population[0]}"
        else:
            adjective = random.choice(adjectives)
            sentence = f"{name} the {adjective} was born in {city} in {year}. Population data not available for {city}"
        
        return render_template('random_sentence.html', sentence=sentence)

    except psycopg2.Error as e:
        return flask.jsonify({'error': 'Database error: ' + str(e)}), 500

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_sentence', methods=['POST'])
def generate_sentence_route():
    return generate_sentence()

if __name__ == '__main__':
    app.run(debug=True)


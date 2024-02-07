import flask
import psycopg2

app = flask.Flask(__name__)

#
@app.route('/hello')
def my_function():
    return "Hello World!"

@app.route('/display/<word1>/<word2>')
def my_display(word1, word2):
    the_string = "The words are: " + word1 + " and " + word2;
    return the_string

@app.route('/color/<word1>')
def my_color(word1):
    return '<h1 style="color:Blue">' + word1 + '</h1>'

@app.route('/add/<num1>/<num2>')
def my_add(num1, num2):
    sum = int(num1) + int(num2)
    return '<h2 style="color:Purple">' + num1 + '+' + num2 + '=' + str(sum) + '</h1>'

@app.route('/pop/<code>')
def get_state_area(code):
    try:
        conn = psycopg2.connect(
	    host="localhost",
	    port=5432,
	    database="choir",
	    user="choir",
	    password="spam889books"
        )
        cursor = conn.cursor()

        query_pop = "SELECT population FROM state_population WHERE code = %s"
        cursor.execute(query_pop, (code,))
        population = cursor.fetchone()

        query_state = "SELECT state FROM state_population WHERE code = %s"
        cursor.execute(query_state, (code,))
        state = cursor.fetchone()

        if population is None:
            return flask.jsonify({'error': 'State population not found'}), 404

        return '<center> <h1 style="color:Blue"> Population of ' + str(state[0]) + ' is ' + str(population[0]) + '</h1> </center>'

    except psycopg2.Error as e:
        return flask.jsonify({'error': 'Database error: ' + str(e)}), 500

    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    my_port = 5123
    app.run(host='0.0.0.0', port = my_port)

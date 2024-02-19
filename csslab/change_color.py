from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('/index.html')

@app.route('/random_color')
def random_color():
    colors = ['red','orange','yellow','green','blue','indigo', 'purple']
    random_color = random.choice(colors)
    return random_color

if __name__ == '__main__':
    app.run(debug=True)


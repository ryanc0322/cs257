from flask import Flask, render_template
import random

app = Flask(__name__)

# create main webpage
@app.route('/')
def index():
    return render_template('/index.html')

# update the background color of the webpage 
@app.route('/random_color')
def random_color():
    colors = ['red','orange','yellow','green','blue','indigo', 'purple']
    random_color = random.choice(colors)
    return random_color

if __name__ == '__main__':
    app.run(debug=True)


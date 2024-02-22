from flask import Flask, render_template
import random

app = Flask(__name__)

# create main webpage
@app.route('/')
def index():
    return render_template('/index.html')

if __name__ == '__main__':
    my_port = 5123
    app.run(host='0.0.0.0', port = my_port)

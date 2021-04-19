from flask import Flask, render_template
from flask_nofloc import NoFLoC

app = Flask(__name__)
# Use your own random secret key
app.secret_key = b'96iGXSNCLYfU5SCU6pzn2hH87gFF4PUrgxl7V5uKLLE'
NoFLoC(app)


@app.route('/')
def index():
    """
    Renders the index page.
    """
    return render_template('index.html')


if __name__ == '__main__':
    app.run('127.0.0.1', 5000, debug=True)

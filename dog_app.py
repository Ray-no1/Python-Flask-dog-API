from flask import Flask, render_template
from dog_api import get_dog_info
from waitress import serve

app = Flask(__name__)


@app.route('/')
def home():
    dogs = get_dog_info()
    return render_template('home.html', dogs=dogs)


if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=8000)

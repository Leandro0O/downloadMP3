from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = '314159'


from .Mp3Downloader import routes



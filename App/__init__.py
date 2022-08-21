from flask import Flask
import os


dirbase = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(dirbase,'C:/Users/Leandro/Downloads')

app = Flask(__name__)

app.config['SECRET_KEY'] = '314159'


from .Mp3Downloader import routes



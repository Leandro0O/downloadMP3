from flask import Flask
import os


dirbase = os.path.abspath(os.path.dirname(__file__))
musicpath = os.path.join(dirbase,'C:/Users/Leandro/Music')
videocpath = os.path.join(dirbase,'C:/Users/Leandro/Videos')

app = Flask(__name__)

app.config['SECRET_KEY'] = '314159'


from .Mp3Downloader import routes



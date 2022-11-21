from flask import Flask
import os


dirbase = os.path.abspath(os.path.dirname(__file__))
musicpath = f"{os.getenv('USERPROFILE')}\\Music"

videocpath = f"{os.getenv('USERPROFILE')}\\Videos"


app = Flask(__name__)

app.config['SECRET_KEY'] = '314159'


from .Mp3Downloader import routes



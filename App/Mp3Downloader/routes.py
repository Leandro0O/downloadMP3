
from App import app
from flask import render_template, redirect, url_for, request,flash, send_file
import time

from .modules import Download

@app.route('/',methods=['POST','GET'])
def Index():

    return render_template('index.html')

@app.route('/downloadmp3',methods=['POST','GET'])
def download_mp3():
    
    if request.method == 'POST':

        try:
            link = request.form.get('link')
            download = Download(link)
            flash(f'Download de {download.downloadmp3()}!', 'success')
            return redirect(url_for('Index'))
        except Exception as e:
            flash(f'Erro ao fazer download:\n {e}!', 'danger')
            redirect(url_for('Index'))
    
    return render_template('index.html')

@app.route('/downloadmp4',methods=['POST','GET'])
def download_mp4():
   
    if request.method == 'POST':     
        try:
            link = request.form.get('link')
            download = Download(link)
            flash(f'Download de {download.downloadmp4()}!', 'success')
            return redirect(url_for('Index'))
        except Exception as e:
            flash(f'Erro ao fazer download:\n {e}!', 'danger')
            redirect(url_for('Index'))
    return render_template('index.html')
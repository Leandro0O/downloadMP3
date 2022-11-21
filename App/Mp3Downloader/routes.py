
from App import app
from flask import render_template, redirect, url_for, request,flash, send_file

from .modules import Download

@app.route('/',methods=['POST','GET'])
def Index():

    return render_template('index.html')

@app.route('/downloadmp3',methods=['POST','GET'])
def download_mp3():

    if request.method == 'POST':
        link = request.form.get('link')
        download = Download(link)
        mp3 = download.downloadmp3()
        if mp3 == True:
            convert = download.convertmp3()
            flash('Download concluido!', 'success')
            return redirect(url_for('Index'))
        else:
            flash('Erro','danger')
    return render_template('index.html')

@app.route('/downloadmp4',methods=['POST','GET'])
def download_mp4():
    if request.method == 'POST':
        link = request.form.get('link')
        download = Download(link)
        mp4 = download.downloadmp4()
        flash('Download do vídeo concluido!', 'success')
        return redirect(url_for('Index'))        
    else:
        flash('Erro','danger')
    return render_template('index.html')
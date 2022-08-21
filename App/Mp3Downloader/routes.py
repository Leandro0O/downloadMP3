
from App import app
from flask import render_template, redirect, url_for, request,flash, send_file

from .modules import Download

@app.route('/',methods=['POST','GET'])
def Index():

    return render_template('index.html')

@app.route('/download',methods=['POST','GET'])
def download_file():

    if request.method == 'POST':
        link = request.form.get('link')
        download = Download(link)
        mp3 = download.downloadmp3()
        if mp3 == True:
            convert = download.convertmp3()
            flash('Download Concluido!', 'success')
            return redirect(url_for('Index'))
        else:
            flash('Erro','danger')
    return render_template('index.html')
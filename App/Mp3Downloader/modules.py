from pytube import YouTube
import moviepy.editor as editor
import re
import os 
from App import path

class Download():
    
    def __init__(self,link):
        self.link = link
        
    def downloadmp3(self):

        ypath = YouTube(self.link)
        ysource = ypath.streams.filter(only_audio=True).first().download(path)

        return True      

    def convertmp3(self):

        for file in os.listdir(path):
            if re.search('mp4',file):
                mp4 = os.path.join(path, file)
                mp3 = os.path.join(path, os.path.splitext(file)[0]+'.mp3')
                new = editor.AudioFileClip(mp4)
                new.write_audiofile(mp3)
                os.remove(mp4)
        return str(mp3)

    def downloadmp4(self):

       ypath = YouTube(self.link)
       ysource = ypath.streams.filter(progressive=True, file_extension= 'mp4').order_by('resolution').desc().first().download(path)

       return True      
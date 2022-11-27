from pytube import YouTube
import re
import os 

MUSICDIR = f"{os.getenv('USERPROFILE')}\\Music"
VIDEODIR = f"{os.getenv('USERPROFILE')}\\Videos"





class Download():
    
    def __init__(self,link):
        self.link = link
        
    def downloadmp3(self):

        yt = YouTube(self.link)
        yt.streams.filter(only_audio=True).first().download(MUSICDIR)
        return yt.title

    def downloadmp4(self):

        yt = YouTube(self.link)
        yt.streams.filter(only_video=True).first().download(VIDEODIR)
        return yt.title
      
import pytube
import moviepy.editor as mp
import os
import logging

def downloading_YT_mp3(urls, destination_path):
    os.chdir(destination_path)
    for url in urls:
        try:
            youtube = pytube.YouTube(url)
            video = youtube.streams.get_highest_resolution()
            file_path = video.download(destination_path) 
            name_file = video.title+".mp3"
            clip = mp.VideoFileClip(file_path)
            ndir = os.getcwd()+'/'+'Songs'
            os.mkdir(ndir)
            os.chdir(ndir)
            clip.audio.write_audiofile(name_file)
            os.remove(file_path)
            logging.basicConfig(filename="logfilename.log", level=logging.INFO)
            logging.info('The song' +video.title+ 'has been download correctly.' )
            
        except:
            
            logging.error('The song' +video.title+ 'had an error while it was downloading.' )
            
#Example
downloading_YT_mp3(['https://www.youtube.com/watch?v=VtM2fspH3CE'], '/home/user/Downloads/')

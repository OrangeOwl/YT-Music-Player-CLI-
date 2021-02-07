import os
import sys
import vlc
import random
import pafy
import time
from mechanize import Browser
import threading

#Loading some empty variables to manipulate
duration = None
start_timer = None
music = None

def pick_song():
    global music
    file = open("playlist.m3u")
    music = file.read().split('\n')
    file.close()
    music.remove("")

# THE ROOT FUNCTION
def shuffle_track():
    global start_timer
    global media
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(1000):
        pick_song()
        track = random.choice(music)
    ## PAFY STUFF
    # getting video
        video = pafy.new(track)
    # getting all the available streams
        streams = video.allstreams
    # selecting one stream
        stream = streams[1]
    # getting url of stream
        song = stream.url
    #------------------------
        media = vlc.MediaPlayer(song)
        print("#####################################################")
        title(track)
        print("-----------------------------------------------------")
        media.play()
        time.sleep(1.5)
        duration = media.get_length() / 1000
        minutes = duration / 60
        length = int(minutes)
        print("LENGTH: " + str(length) + " minute(s)")
        print("-----------------------------------------------------")
        SECONDS = int(duration) + 3
        try:
        #cancel current timer if running
           start_timer.cancel()
           #print("TIMER RESTARED")
        #start new timer   
           start_timer = threading.Timer(SECONDS, shuffle_track)
           start_timer.start()
           playing()
        except:
        #start new timer
           #print("TIMER ACTIVE")
           start_timer = threading.Timer(SECONDS, shuffle_track)
           start_timer.start()
           playing()
          
def title(arg):
    # Getting the Title of the Song
    br = Browser()
    br.open(arg)
    print (br.title())
        
def playing():
    print("#####################################################")
    print("Hit Enter to Skip the Song")
    choice = input('>>> ')
    if choice.lower() == '':
        media.stop()
        shuffle_track()    
    else:
        playing()

shuffle_track()

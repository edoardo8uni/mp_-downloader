import sys
from pytube import YouTube
from moviepy.editor import AudioFileClip
import os
import shutil
import sys


video_path = "C:\\Users\\utente\\Desktop\\edoardo\\Python 3.7\\programmi_1.0\\tracce_mp4"
audio_path = "C:\\Users\\utente\\Desktop\\edoardo\\Python 3.7\\programmi_1.0\\tracce_mp3"
file_name = sys.argv[1]
if file_name not in os.listdir():
    print("ERROR: file does not exist - program crash")
    exit(0)

def read_line():
    f = open(file_name, "rt")
    url_list = []
    while True:
        url = f.readline()
        if url != '':
            url_list.append(str(url))  
        else:
            break

    f.close()
    return url_list


def download_mp4(url_video,f):
    d = " "*(70-len(url_video))
    try:
        yt = YouTube(url_video)
        track = yt.streams.filter(only_audio=True)
        track[0].download('tracce_mp4')
        strang = url_video[:-1] + d + "COMPLETE"
        print(strang, file = f)
    except:
        strang = url_video[0:-1] + d + "ERROR"
        print(strang, file = f)
        print("url [{url_}] not valid".format(url_  = url_video[:-1]))


def extract_mp3(video_file):
    path_ = "tracce_mp4//"+ video_file
    audio_name = video_file[0:-3]+"mp3"
    clip = AudioFileClip(path_)
    clip.write_audiofile(audio_name)
    shutil.move(str(audio_name), audio_path)
    clip.close()

def delete_mp4():
    for i in os.listdir(video_path):
        i = video_path + "\\" + i
        os.remove(i)

urls = read_line()
f = open(file_name, "wt")
for url in urls:
    download_mp4(str(url),f)

f.close()
for i in os.listdir(video_path):
    extract_mp3(i)

delete_mp4()


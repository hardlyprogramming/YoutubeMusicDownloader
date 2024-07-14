import yt_dlp
import pytube
import json
import os
import argparse

parser = argparse.ArgumentParser(description='Download music from youtube')
parser.add_argument('youtube_link')

args = parser.parse_args()

URL = args.youtube_link
### CHANGE PATH TO MUSIC DIRECTORY ###
path = 'D:\\hp\\Media\\Music\\'
######################################

with yt_dlp.YoutubeDL() as ydl:
	info = info = ydl.extract_info(URL, download=False)
	author = info['uploader']
	chapters = info['chapters']
if chapters is None:
	delete_original = False
else:
	delete_original = True

yt_opts = {
#'extract_audio': True,
'format': 'bestaudio[ext=m4a]/best',
'writethumbnail': True,
'paths':{'home':path+author+'\\'},
'outtmpl':{'chapter':path+author+'\\'+'%(title)s' +'\\'+ '%(section_title)s.%(ext)s'},
'postprocessors':[{'key':'EmbedThumbnail'},{'key':'FFmpegSplitChapters'}]}

with yt_dlp.YoutubeDL(yt_opts) as ydl:
	info = ydl.extract_info(URL, download=True)

file = info['requested_downloads'][0]['filepath']
if delete_original:
	print('----Removing Original File----')
	trash_file = os.path.join(path, file)
	os.remove(trash_file)

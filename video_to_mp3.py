# convert videos to mp3
import os
import subprocess as s

files = os.listdir("videos")
for index,file in enumerate(files):
    file_name= f"{index+1}_{file.split("_-_")[0]}"
    print(file_name)
    s.run(["ffmpeg","-i",f"videos/{file}",f"audios/{file_name}.mp3"])
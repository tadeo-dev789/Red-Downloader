from typing import Union
from fastapi import FastAPI
from fastapi.responses import FileResponse
from pathlib import Path

import os
import yt_dlp

app = FastAPI()

downloads_dir  = Path ("./downloads")
downloads_dir.mkdir(parents=True, exist_ok=True)

@app.get("/")
def read_root():
    return{"Hello":"World"}

@app.get("/download/")
def download(url:str):
    ydl_opts = {
        'outtmpl': str(downloads_dir / '%(title)s.%(ext)s'),
        'format' : 'bestaudio/best',
        'postprocessors':[{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality':'320',
        }]
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url,download=False)
        predicted_filename = ydl.prepare_filename(info)
        error_code = ydl.download(url)
    
    mp3_filename = Path(predicted_filename).with_suffix('.mp3')
    
    return FileResponse(mp3_filename)
    
    

    
  
from typing import Union
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

from pathlib import Path

import os
import yt_dlp

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

downloads_dir  = Path ("./downloads")
downloads_dir.mkdir(parents=True, exist_ok=True)

@app.get("/")
def read_root():
    return{"Hello":"World"}

@app.get("/download/")
def download(url: str):
    try:
        ydl_opts = {
            'outtmpl': str(downloads_dir / '%(title).100s.%(ext)s'), 
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',
            }],
            'quiet': False,
            'restrictfilenames': True,  
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            predicted_filename = ydl.prepare_filename(info)
            ydl.download([url])
        
        mp3_path = Path(predicted_filename).with_suffix('.mp3')
        
        if not mp3_path.exists():
            import glob
            mp3_files = glob.glob(str(downloads_dir / "*.mp3"))
            if mp3_files:
                mp3_path = Path(mp3_files[-1])  # Get the latest
            else:
                raise HTTPException(status_code=500, detail="File not found after download")
        
        return FileResponse(
            mp3_path,
            filename=mp3_path.name,
            media_type='audio/mpeg'
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Download failed: {str(e)}")
    
    

    
  
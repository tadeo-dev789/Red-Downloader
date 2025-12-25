from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
from urllib.parse import quote
import os
import glob
import yt_dlp

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["Content-Disposition", "X-Filename"] 
)

downloads_dir = Path("./downloads")
downloads_dir.mkdir(parents=True, exist_ok=True)

def cleanup_file(path: str):
    try:
        if os.path.exists(path):
            os.remove(path)
    except Exception:
        pass

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/download")
def download(url: str, background_tasks: BackgroundTasks):
    try:
        ydl_opts = {
            'outtmpl': str(downloads_dir / '%(title)s.%(ext)s'),
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'quiet': False,
            'restrictfilenames': False,
        }
        
        predicted_filename = ""
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            predicted_filename = ydl.prepare_filename(info)
            ydl.download([url])
        
        mp3_path = Path(predicted_filename).with_suffix('.mp3')
        
        if not mp3_path.exists():
            list_of_files = glob.glob(str(downloads_dir / "*.mp3"))
            if list_of_files:
                latest_file = max(list_of_files, key=os.path.getctime)
                mp3_path = Path(latest_file)
            else:
                raise HTTPException(status_code=500, detail="File not found after download")
        
        background_tasks.add_task(cleanup_file, str(mp3_path))

        safe_filename = quote(mp3_path.name)

        return FileResponse(
            mp3_path,
            filename=mp3_path.name,
            media_type='audio/mpeg',
            headers={"X-Filename": safe_filename}
        )
        
    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))
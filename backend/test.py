import yt_dlp

URLS = ['https://youtu.be/Kq_plVrBPx4?si=fhnf3nVpMSa3pcg9']

ydl_opts = {
    'format': 'm4a/bestaudio/best',
    # ℹ️ See help(yt_dlp.postprocessor) for a list of available Postprocessors and their arguments
    'postprocessors': [{  # Extract audio using ffmpeg
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality':'320',
    }],'outtmpl': '%(title)s.%(etx)s'
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    error_code = ydl.download(URLS)
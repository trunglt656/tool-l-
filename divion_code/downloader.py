import os
import yt_dlp
import requests
from datetime import datetime
from tkinter import messagebox

# Tải video từ TikTok
def download_video_tiktok(video_url):
    folder_path = r"D:\Affiliate\tool_sp\download_video\asset"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    video_filename = f"video_tiktok_{timestamp}.mp4"
    video_path = os.path.join(folder_path, video_filename)

    ydl_opts = {
        'format': 'best',
        'noplaylist': True,
        'outtmpl': video_path,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        return video_path
    except Exception as e:
        messagebox.showerror("Lỗi", f"Đã xảy ra lỗi khi tải video: {e}")
        return None

# Tải video từ URL
def download_video_from_url(video_url):
    folder_path = r"D:\Affiliate\tool_sp\download_video\asset"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    video_filename = f"video_url_{timestamp}.mp4"
    video_path = os.path.join(folder_path, video_filename)

    try:
        response = requests.get(video_url, stream=True)
        if response.status_code == 200:
            with open(video_path, 'wb') as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)
            return video_path
        else:
            messagebox.showerror("Lỗi", f"Không thể tải video. Mã lỗi: {response.status_code}")
            return None
    except Exception as e:
        messagebox.showerror("Lỗi", f"Đã xảy ra lỗi khi tải video: {e}")
        return None

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

def download_video_from_url(video_url):
    folder_path = r"D:\Affiliate\tool_sp\download_video\asset"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    video_filename = f"video_{timestamp}.mp4"
    video_path = os.path.join(folder_path, video_filename)

    ydl_opts = {
        'outtmpl': video_path,
        'format': 'bestvideo+bestaudio/best',  # Chọn chất lượng cao nhất
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        print("Tải video thành công:", video_path)
        return video_path
    except Exception as e:
        print("Lỗi khi tải video:", e)
        return None


# Tải video từ YouTube Shorts
def download_video_youtube_shorts(video_url):
    folder_path = r"D:\Affiliate\tool_sp\download_video\asset"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    video_filename = f"video_youtube_shorts_{timestamp}.mp4"
    video_path = os.path.join(folder_path, video_filename)

    ydl_opts = {
        'outtmpl': video_path,
        'format': 'bestvideo[height<=1920]+bestaudio/best',  # Ưu tiên video 1080x1920
        'merge_output_format': 'mp4',  # Đảm bảo xuất ra định dạng MP4
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        print(f"Tải video thành công: {video_path}")
        return video_path
    except Exception as e:
        print(f"Lỗi khi tải video: {e}")
        return None

from tkinter import filedialog

def download_video_douyin(video_url):
    try:
        # Chọn nơi lưu tệp
        save_path = filedialog.asksaveasfilename(
            defaultextension=".mp4",
            filetypes=[("Video files", "*.mp4")],
            title="Chọn nơi lưu video"
        )
        if not save_path:
            raise Exception("Không chọn đường dẫn lưu tệp.")

        response = requests.get(video_url, stream=True)
        if response.status_code == 200:
            with open(save_path, "wb") as file:
                for chunk in response.iter_content(chunk_size=1024):
                    file.write(chunk)
            return save_path
        else:
            raise Exception("Không thể tải video từ Douyin.")
    except Exception as e:
        raise Exception(f"Lỗi khi tải video: {e}")

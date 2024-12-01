import os
import tkinter as tk
from tkinter import filedialog
import yt_dlp
from datetime import datetime

# Hàm tải video
def download_video():
    video_url = url_entry.get()  # Lấy URL từ ô nhập
    folder_path = folder_entry.get()  # Lấy đường dẫn thư mục lưu

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)  # Tạo thư mục nếu chưa tồn tại

    # Tạo tên file duy nhất bằng cách sử dụng thời gian hiện tại
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    video_filename = f"video_tiktok_{timestamp}.%(ext)s"

    # Cấu hình tải video
    ydl_opts = {
        'format': 'best',  # Tải video chất lượng tốt nhất
        'noplaylist': True,  # Tắt playlist
        'outtmpl': os.path.join(folder_path, video_filename),  # Lưu vào thư mục đã chọn với tên duy nhất
        'writeinfojson': False,  # Không ghi file info.json
    }

    # Tải video
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

    result_label.config(text="Video tải về thành công!")

# Hàm mở hộp thoại chọn thư mục
def browse_folder():
    folder_selected = filedialog.askdirectory()
    folder_entry.delete(0, tk.END)  # Xóa nội dung cũ trong ô nhập
    folder_entry.insert(0, folder_selected)  # Chèn thư mục đã chọn vào ô nhập

# Tạo cửa sổ GUI
root = tk.Tk()
root.title("Tải Video TikTok Không Logo")

# URL nhập vào
url_label = tk.Label(root, text="Nhập URL Video TikTok:")
url_label.pack(padx=10, pady=5)

url_entry = tk.Entry(root, width=50)
url_entry.pack(padx=10, pady=5)

# Thư mục lưu video
folder_label = tk.Label(root, text="Chọn thư mục lưu video:")
folder_label.pack(padx=10, pady=5)

folder_entry = tk.Entry(root, width=50)
folder_entry.pack(padx=10, pady=5)

browse_button = tk.Button(root, text="Chọn thư mục", command=browse_folder)
browse_button.pack(padx=10, pady=5)

# Nút tải video
download_button = tk.Button(root, text="Tải Video", command=download_video)
download_button.pack(padx=10, pady=10)

# Label hiển thị kết quả
result_label = tk.Label(root, text="")
result_label.pack(padx=10, pady=5)

# Chạy ứng dụng
root.mainloop()


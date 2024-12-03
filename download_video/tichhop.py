# import os
# import tkinter as tk
# from tkinter import filedialog, messagebox
# from moviepy import VideoFileClip, AudioFileClip
# from datetime import datetime
# import yt_dlp

# # Tải video TikTok
# def download_video():
#     video_url = url_entry.get()
#     folder_path = r"D:\Affiliate\tool_sp\download_video\asset"  # Thư mục lưu video tải về

#     if not os.path.exists(folder_path):
#         os.makedirs(folder_path)

#     # Tên file duy nhất
#     timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
#     video_filename = f"video_tiktok_{timestamp}.mp4"
#     video_path = os.path.join(folder_path, video_filename)

#     # Cấu hình tải video
#     ydl_opts = {
#         'format': 'best',
#         'noplaylist': True,
#         'outtmpl': video_path,
#     }

#     try:
#         with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#             ydl.download([video_url])
#         result_label.config(text="Video tải về thành công!", fg="green")
#         return video_path
#     except Exception as e:
#         result_label.config(text=f"Lỗi: {e}", fg="red")
#         return None

# # Chỉnh sửa video
# def edit_video(input_video_path, input_audio_path):
#     try:
#         video = VideoFileClip(input_video_path)
#         audio = AudioFileClip(input_audio_path)

#         if audio.duration > video.duration:
#             audio = audio.subclipped(0, video.duration)

#         video_with_new_audio = video.with_audio(audio)

#         # Thư mục lưu video đầu ra
#         output_folder = r"D:\Affiliate\tool_sp\download_video\done_video"
#         if not os.path.exists(output_folder):
#             os.makedirs(output_folder)

#         # Tạo tên file đầu ra tự động
#         timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
#         output_video_path = os.path.join(output_folder, f"edited_video_{timestamp}.mp4")

#         # Lưu video
#         video_with_new_audio.write_videofile(output_video_path, codec="libx264", audio_codec="aac")
#         messagebox.showinfo("Thành công", f"Video đã được chỉnh sửa và lưu tại:\n{output_video_path}")
#     except Exception as e:
#         messagebox.showerror("Lỗi", f"Đã xảy ra lỗi: {e}")

# # Tích hợp tải và chỉnh sửa
# def download_and_edit():
#     video_path = download_video()
#     if not video_path:
#         return

#     # Yêu cầu chọn nhạc
#     input_audio_path = filedialog.askopenfilename(filetypes=[("Audio files", "*.mp3 *.wav")])
#     if not input_audio_path:
#         messagebox.showwarning("Cảnh báo", "Vui lòng chọn file âm thanh!")
#         return

#     edit_video(video_path, input_audio_path)

# # Giao diện
# root = tk.Tk()
# root.title("Tải và Chỉnh sửa Video TikTok")

# # Nhập URL video
# url_label = tk.Label(root, text="Nhập URL Video TikTok:")
# url_label.pack(padx=10, pady=5)

# url_entry = tk.Entry(root, width=50)
# url_entry.pack(padx=10, pady=5)

# # Nút tải và chỉnh sửa video
# process_button = tk.Button(root, text="Tải và Chỉnh sửa Video", command=download_and_edit, bg="blue", fg="white")
# process_button.pack(padx=10, pady=10)

# # Hiển thị kết quả
# result_label = tk.Label(root, text="")
# result_label.pack(padx=10, pady=5)

# # Chạy ứng dụng
# root.mainloop()



# import os
# import tkinter as tk
# from tkinter import filedialog, messagebox
# from moviepy import VideoFileClip, AudioFileClip
# from datetime import datetime
# import yt_dlp
# import subprocess

# # Tải video TikTok
# def download_video():
#     video_url = url_entry.get()
#     folder_path = r"D:\Affiliate\tool_sp\download_video\asset"  # Thư mục lưu video tải về

#     if not os.path.exists(folder_path):
#         os.makedirs(folder_path)

#     # Tên file duy nhất
#     timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
#     video_filename = f"video_tiktok_{timestamp}.mp4"
#     video_path = os.path.join(folder_path, video_filename)

#     # Cấu hình tải video
#     ydl_opts = {
#         'format': 'best',
#         'noplaylist': True,
#         'outtmpl': video_path,
#     }

#     try:
#         with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#             ydl.download([video_url])
#         result_label.config(text="Video tải về thành công!", fg="green")
#         return video_path
#     except Exception as e:
#         result_label.config(text=f"Lỗi: {e}", fg="red")
#         return None

# # Chỉnh sửa video
# def edit_video(input_video_path, input_audio_path):
#     try:
#         video = VideoFileClip(input_video_path)
#         audio = AudioFileClip(input_audio_path)

#         if audio.duration > video.duration:
#             audio = audio.subclipped(0, video.duration)

#         video_with_new_audio = video.with_audio(audio)

#         # Thư mục lưu video đầu ra
#         output_folder = r"D:\Affiliate\tool_sp\download_video\done_video"
#         if not os.path.exists(output_folder):
#             os.makedirs(output_folder)

#         # Tạo tên file đầu ra tự động
#         timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
#         output_video_path = os.path.join(output_folder, f"edited_video_{timestamp}.mp4")

#         # Lưu video
#         video_with_new_audio.write_videofile(output_video_path, codec="libx264", audio_codec="aac")
#         messagebox.showinfo("Thành công", f"Video đã được chỉnh sửa và lưu tại:\n{output_video_path}")
        
#         # Gửi video qua ADB
#         send_video_to_phone(output_video_path)

#     except Exception as e:
#         messagebox.showerror("Lỗi", f"Đã xảy ra lỗi: {e}")

# # Gửi video qua ADB
# def send_video_to_phone(video_path):
#     try:
#         # Kiểm tra thiết bị Android đã kết nối
#         result = subprocess.run(["adb", "devices"], capture_output=True, text=True)
#         if "device" not in result.stdout:
#             messagebox.showerror("Lỗi", "Không tìm thấy thiết bị Android. Hãy chắc chắn rằng thiết bị đã kết nối và bật USB Debugging.")
#             return

#         # Đường dẫn lưu video trên thiết bị Android
#         phone_video_path = "/sdcard/Download/edited_video.mp4"
        
#         # Lệnh ADB để gửi video tới thiết bị Android
#         subprocess.run(["adb", "push", video_path, phone_video_path])
#         messagebox.showinfo("Thành công", f"Video đã được gửi đến thiết bị Android: {phone_video_path}")
#     except Exception as e:
#         messagebox.showerror("Lỗi", f"Đã xảy ra lỗi khi gửi video: {e}")

# # Tích hợp tải và chỉnh sửa
# def download_and_edit():
#     video_path = download_video()
#     if not video_path:
#         return

#     # Yêu cầu chọn nhạc
#     input_audio_path = filedialog.askopenfilename(filetypes=[("Audio files", "*.mp3 *.wav")])
#     if not input_audio_path:
#         messagebox.showwarning("Cảnh báo", "Vui lòng chọn file âm thanh!")
#         return

#     edit_video(video_path, input_audio_path)

# # Giao diện
# root = tk.Tk()
# root.title("Tải và Chỉnh sửa Video TikTok")

# # Nhập URL video
# url_label = tk.Label(root, text="Nhập URL Video TikTok:")
# url_label.pack(padx=10, pady=5)

# url_entry = tk.Entry(root, width=50)
# url_entry.pack(padx=10, pady=5)

# # Nút tải và chỉnh sửa video
# process_button = tk.Button(root, text="Tải và Chỉnh sửa Video", command=download_and_edit, bg="blue", fg="white")
# process_button.pack(padx=10, pady=10)

# # Hiển thị kết quả
# result_label = tk.Label(root, text="")
# result_label.pack(padx=10, pady=5)

# # Chạy ứng dụng
# root.mainloop()


import os
import tkinter as tk
from tkinter import filedialog, messagebox
from moviepy import VideoFileClip, AudioFileClip
from datetime import datetime
import yt_dlp
import subprocess

# Tải video TikTok
def download_video(video_url):
    folder_path = r"D:\Affiliate\tool_sp\download_video\asset"  # Thư mục lưu video tải về

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Tên file duy nhất
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    video_filename = f"video_tiktok_{timestamp}.mp4"
    video_path = os.path.join(folder_path, video_filename)

    # Cấu hình tải video
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

# Chỉnh sửa video
def edit_video(input_video_path, input_audio_path):
    try:
        video = VideoFileClip(input_video_path)
        audio = AudioFileClip(input_audio_path)

        if audio.duration > video.duration:
            audio = audio.subclipped(0, video.duration)

        video_with_new_audio = video.with_audio(audio)

        # Thư mục lưu video đầu ra
        output_folder = r"D:\Affiliate\tool_sp\download_video\done_video"
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Tạo tên file đầu ra tự động
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_video_path = os.path.join(output_folder, f"edited_video_{timestamp}.mp4")

        # Lưu video
        video_with_new_audio.write_videofile(output_video_path, codec="libx264", audio_codec="aac")
        messagebox.showinfo("Thành công", f"Video đã được chỉnh sửa và lưu tại:\n{output_video_path}")
        
        # Gửi video qua ADB
        send_video_to_phone(output_video_path)

    except Exception as e:
        messagebox.showerror("Lỗi", f"Đã xảy ra lỗi khi chỉnh sửa video: {e}")

# Gửi video qua ADB
def send_video_to_phone(video_path):
    try:
        # Kiểm tra thiết bị Android đã kết nối
        result = subprocess.run(["adb", "devices"], capture_output=True, text=True)
        if "device" not in result.stdout:
            messagebox.showerror("Lỗi", "Không tìm thấy thiết bị Android. Hãy chắc chắn rằng thiết bị đã kết nối và bật USB Debugging.")
            return

        # Đường dẫn lưu video trên thiết bị Android
        phone_video_path = "/sdcard/Download/edited_video.mp4"
        
        # Lệnh ADB để gửi video tới thiết bị Android
        subprocess.run(["adb", "push", video_path, phone_video_path])
        messagebox.showinfo("Thành công", f"Video đã được gửi đến thiết bị Android: {phone_video_path}")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Đã xảy ra lỗi khi gửi video: {e}")

# Quy trình tải và chỉnh sửa video
def start_process():
    # Lấy URL video và âm nhạc
    video_url = url_entry.get()
    audio_file_path = audio_entry.get()

    if not video_url or not audio_file_path:
        messagebox.showwarning("Cảnh báo", "Vui lòng nhập đầy đủ thông tin (URL và âm nhạc).")
        return

    # Tải video về
    video_path = download_video(video_url)
    if not video_path:
        return

    # Chỉnh sửa video
    edit_video(video_path, audio_file_path)

# Chọn file âm nhạc
def select_audio_file():
    audio_path = filedialog.askopenfilename(filetypes=[("Audio files", "*.mp3 *.wav")])
    if audio_path:
        audio_entry.delete(0, tk.END)
        audio_entry.insert(0, audio_path)

# Tạo giao diện
root = tk.Tk()
root.title("Tải và Chỉnh sửa Video TikTok")

# Nhập URL video
url_label = tk.Label(root, text="Nhập URL Video TikTok:")
url_label.pack(padx=10, pady=5)

url_entry = tk.Entry(root, width=50)
url_entry.pack(padx=10, pady=5)

# Nhập đường dẫn âm nhạc
audio_label = tk.Label(root, text="Chọn âm nhạc để ghép:")
audio_label.pack(padx=10, pady=5)

audio_entry = tk.Entry(root, width=50)
audio_entry.pack(padx=10, pady=5)

audio_button = tk.Button(root, text="Chọn âm nhạc", command=select_audio_file)
audio_button.pack(padx=10, pady=5)

# Nút bắt đầu quá trình
start_button = tk.Button(root, text="Tải và Chỉnh sửa Video", command=start_process, bg="blue", fg="white")
start_button.pack(padx=10, pady=10)

# Hiển thị kết quả
result_label = tk.Label(root, text="")
result_label.pack(padx=10, pady=5)

# Chạy ứng dụng
root.mainloop()

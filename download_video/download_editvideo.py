import os
import tkinter as tk
from tkinter import filedialog, messagebox
from moviepy import VideoFileClip, AudioFileClip
from datetime import datetime
import yt_dlp
import subprocess
import time

# Hàm chạy lệnh ADB
def run_adb_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        result.check_returncode()
        print(f"Đã chạy lệnh: {command}")
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Lỗi khi chạy lệnh: {e}")
        return ""

# Hàm nhập chuỗi ký tự từng ký tự một (bao gồm ký tự đặc biệt)
def input_text_by_character(text):
    for char in text:
        if char == ' ':
            # Nếu là dấu cách, dùng keyevent 62 (phím space)
            run_adb_command("adb shell input keyevent 62")
        elif char == '#':
            # Nếu là dấu #, dùng keyevent cho ký tự #
            run_adb_command("adb shell input text '#'")
        else:
            # Các ký tự khác sử dụng lệnh input text
            run_adb_command(f"adb shell input text {char}")
        time.sleep(0.1)  # Thêm thời gian chờ giữa các ký tự
    print(f"Đã nhập: {text}")

# Mở ứng dụng Shopee
def open_shopee():
    print("Đang mở ứng dụng Shopee...")
    run_adb_command("adb shell monkey -p com.shopee.vn -c android.intent.category.LAUNCHER 1")
    time.sleep(3)


# Mở ứng dụng thư viện video
def open_library_video():
    print("Đang mở ứng dụng Thư viện video...")
    run_adb_command("adb shell am start -n com.miui.gallery/.activity.HomePageActivity")
    time.sleep(8)

# Nhấn nút upload video
def upload_video():
    print("Đang tải video lên...")
    run_adb_command("adb shell input tap 1015 157")  # Nhấn nút upload
    time.sleep(3)
    run_adb_command("adb shell input tap 865 1875")  # Chọn thư viện
    time.sleep(2)
    run_adb_command("adb shell input tap 145 471")  # Chọn video đầu tiên
    time.sleep(2)
    run_adb_command("adb shell input tap 945 2253")  # Nhấn Tiếp theo
    time.sleep(2)
    run_adb_command("adb shell input tap 969 2189")  # Nhấn Tiếp theo lần nữa
    time.sleep(2)

# Thêm sản phẩm bằng link
def add_product_link(link):
    print("Đang thêm sản phẩm bằng link...")
    run_adb_command("adb shell input tap 821 685")  # Nhấn thêm sản phẩm
    time.sleep(2)
    run_adb_command("adb shell input tap 1041 171")  # Chọn link
    time.sleep(2)
    run_adb_command("adb shell input tap 533 601")  # Nhấn vào ô nhập link
    time.sleep(2)
    run_adb_command(f"adb shell input text '{link}'")  # Nhập link sản phẩm
    time.sleep(2)
    run_adb_command("adb shell input tap 519 847")  # Nhấn nút Nhập
    time.sleep(2)
    run_adb_command("adb shell input tap 67 2225")  # Chọn tất cả sản phẩm
    time.sleep(1)
    run_adb_command("adb shell input tap 571 2183")  # Nhấn thêm sản phẩm
    time.sleep(1)

# Hàm nhập mô tả sản phẩm
def add_product_description(description):
    print("Đang nhập mô tả sản phẩm...")
    
    # Nhấn vào ô mô tả sản phẩm
    run_adb_command("adb shell input tap 593 417")  # Chỉnh lại tọa độ nếu cần
    time.sleep(2)

    # Sử dụng hàm nhập chuỗi ký tự từng ký tự một
    input_text_by_character(description)
    time.sleep(2)

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
        print("Thành công", f"Video đã được chỉnh sửa và lưu tại:\n{output_video_path}")
        
        # Gửi video qua ADB
        send_video_to_phone(output_video_path)

    except Exception as e:
        messagebox.showerror("Lỗi", f"Đã xảy ra lỗi khi chỉnh sửa video: {e}")

import os
import subprocess
from tkinter import messagebox

import os
import subprocess

# Gửi video qua ADB
def send_video_to_phone(video_path):
    try:
        # Kiểm tra thiết bị Android đã kết nối
        result = subprocess.run(["adb", "devices"], capture_output=True, text=True)
        if "device" not in result.stdout:
            print("Lỗi: Không tìm thấy thiết bị Android. Hãy chắc chắn rằng thiết bị đã kết nối và bật USB Debugging.")
            return
        
        # Lấy tên video gốc từ đường dẫn
        video_name = os.path.basename(video_path)
        
        # Đường dẫn lưu video trên thiết bị Android (sử dụng tên gốc của video)
        phone_video_path = f"/sdcard/Download/{video_name}"
        
        # Lệnh ADB để gửi video tới thiết bị Android
        subprocess.run(["adb", "push", video_path, phone_video_path])
        
        # In thông báo thành công ra terminal
        print(f"Video đã được gửi đến thiết bị Android: {phone_video_path}")
    except Exception as e:
        print(f"Lỗi: Đã xảy ra lỗi khi gửi video: {e}")



# Quy trình tải và chỉnh sửa video
def start_process():
    # Lấy URL video, âm nhạc, link sản phẩm và mô tả sản phẩm
    video_url = url_entry.get()
    audio_file_path = audio_entry.get()
    product_link = product_link_entry.get()
    product_description = product_desc_entry.get()

    if not video_url or not audio_file_path:
        messagebox.showwarning("Cảnh báo", "Vui lòng nhập đầy đủ thông tin (URL và âm nhạc).")
        return

    # Hiển thị thông tin sản phẩm (có thể thêm logic xử lý nếu cần)
    print(f"Link sản phẩm: {product_link}")
    print(f"Mô tả sản phẩm: {product_description}")

    # Tải video về
    video_path = download_video(video_url)
    if not video_path:
        return

    # Chỉnh sửa video
    edit_video(video_path, audio_file_path)

    # Sau khi video đã chỉnh sửa xong, thực hiện các bước đăng lên Shopee
    open_shopee()
    open_library_video()
    open_shopee()
    upload_video()
    add_product_link(product_link)
    add_product_description(product_description)

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

select_audio_button = tk.Button(root, text="Chọn âm nhạc", command=select_audio_file)
select_audio_button.pack(padx=10, pady=5)

# Nhập link sản phẩm và mô tả
product_link_label = tk.Label(root, text="Nhập Link sản phẩm Shopee:")
product_link_label.pack(padx=10, pady=5)

product_link_entry = tk.Entry(root, width=50)
product_link_entry.pack(padx=10, pady=5)

product_desc_label = tk.Label(root, text="Nhập mô tả sản phẩm:")
product_desc_label.pack(padx=10, pady=5)

product_desc_entry = tk.Entry(root, width=50)
product_desc_entry.pack(padx=10, pady=5)

# Nút bắt đầu
start_button = tk.Button(root, text="Bắt đầu", command=start_process)
start_button.pack(padx=10, pady=20)

root.mainloop()

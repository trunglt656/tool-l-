
import tkinter as tk
from tkinter import filedialog, messagebox
from downloader import download_video_tiktok, download_video_from_url, download_video_youtube_shorts, download_video_douyin
from video_editor import edit_video, send_video_to_phone
from shopee_actions import open_shopee, open_library_video, upload_video, add_product_link, add_product_description
import tkinter as tk
from tkinter import filedialog, messagebox

def select_audio_file():
    audio_path = filedialog.askopenfilename(filetypes=[("Audio files", "*.mp3 *.wav")])
    if audio_path:
        audio_entry.delete(0, tk.END)
        audio_entry.insert(0, audio_path)

def start_process():
    # Xóa nội dung log trước khi bắt đầu
    log_box.config(state="normal")
    log_box.delete(1.0, tk.END)
    log_box.insert(tk.END, "Bắt đầu quá trình...\n")
    log_box.config(state="disabled")

    video_url = url_entry.get()
    audio_file_path = audio_entry.get()
    product_link = product_link_entry.get()
    product_description = product_desc_entry.get()
    download_type = download_choice.get()
    add_music = add_music_var.get()

    if not video_url:
        log_callback("Cảnh báo: Vui lòng nhập URL video.")
        return

    if add_music and not audio_file_path:
        log_callback("Cảnh báo: Vui lòng chọn tệp âm nhạc khi chọn ghép nhạc.")
        return

    log_callback("Bắt đầu tải video...")
    try:
        if download_type == "tiktok":
            video_path = download_video_tiktok(video_url)
        elif download_type == "url":
            video_path = download_video_from_url(video_url)
        elif download_type == "youtube_short":
            video_path = download_video_youtube_shorts(video_url)
        else:
            log_callback("Cảnh báo: Hãy chọn loại video cần tải.")
            return

        if not video_path:
            log_callback("Lỗi: Không tải được video.")
            return

        log_callback("Tải video thành công. Bắt đầu chỉnh sửa video...")
        output_video_path = edit_video(video_path, audio_file_path, add_music, log_callback)


        if output_video_path:
            log_callback("Bắt đầu gửi video sang điện thoại...")
            send_video_to_phone(output_video_path, log_callback)

        log_callback("Bắt đầu tải lên Shopee...")
        open_library_video(log_callback)
        open_shopee(log_callback)
        upload_video(log_callback)

        log_callback("Quá trình hoàn tất!")
    except Exception as e:
        log_callback(f"Lỗi: {e}")

def log_callback(*messages):
    combined_message = " ".join(messages)
    log_box.config(state="normal")
    log_box.insert(tk.END, f"{combined_message}\n")
    log_box.see(tk.END)
    log_box.config(state="disabled")
    log_box.update_idletasks()


def open_tab(tab_name):
    for tab in tabs.values():
        tab.grid_remove()  # Ẩn tất cả các tab

    if tab_name not in tabs:
        tabs[tab_name] = tk.Frame(main_frame)
        tabs[tab_name].grid(row=0, column=0, sticky="nsew")

        if tab_name == "Voice Over":
            tk.Label(tabs[tab_name], text="Chọn video:").grid(pady=5)
            tk.Entry(tabs[tab_name], width=60).grid(pady=5)
            tk.Button(tabs[tab_name], text="Browse").grid(pady=5)

            tk.Label(tabs[tab_name], text="Nhập văn bản:").grid(pady=5)
            tk.Text(tabs[tab_name], width=60, height=10).grid(pady=5)

            tk.Label(tabs[tab_name], text="Lưu video tại:").grid(pady=5)
            tk.Entry(tabs[tab_name], width=60).grid(pady=5)
            tk.Button(tabs[tab_name], text="Browse").grid(pady=5)

            tk.Button(tabs[tab_name], text="Tạo Video", bg="green", fg="white").grid(pady=20)

        elif tab_name == "Download Video":
            tk.Label(tabs[tab_name], text="Nhập URL video Douyin:").grid(pady=5)
            douyin_url_entry = tk.Entry(tabs[tab_name], width=60)
            douyin_url_entry.grid(pady=5)
        
            def start_download_douyin():
                video_url = douyin_url_entry.get()
                if not video_url:
                    messagebox.showerror("Lỗi", "Vui lòng nhập URL Douyin.")
                    return
        
                try:
                    file_path = download_video_douyin(video_url)
                    messagebox.showinfo("Thành công", f"Video đã được lưu tại: {file_path}")
                except Exception as e:
                    messagebox.showerror("Lỗi", str(e))
        
            tk.Button(tabs[tab_name], text="Tải Video Douyin", command=start_download_douyin).grid(pady=10)

        elif tab_name == "Duplicate Video":
            tk.Label(tabs[tab_name], text="Sao chép video:").grid(pady=5)
            tk.Entry(tabs[tab_name], width=60).grid(pady=5)
            tk.Button(tabs[tab_name], text="Chọn File").grid(pady=5)

            tk.Label(tabs[tab_name], text="Lưu bản sao tại:").grid(pady=5)
            tk.Entry(tabs[tab_name], width=60).grid(pady=5)
            tk.Button(tabs[tab_name], text="Browse").grid(pady=5)

            tk.Button(tabs[tab_name], text="Sao chép Video", bg="blue", fg="white").grid(pady=20)

    tabs[tab_name].grid(row=0, column=0, sticky="nsew")

root = tk.Tk()
root.title("Tải và Chỉnh sửa Video TikTok")
root.geometry("800x600")

nav_frame = tk.Frame(root, bg="#f0f0f0", height=50)
nav_frame.pack(side="top", fill="x")

main_frame = tk.Frame(root)
main_frame.pack(padx=10, pady=10, fill="both", expand=True)
main_frame.grid_rowconfigure(0, weight=1)
main_frame.grid_columnconfigure(0, weight=1)

tabs = {}

nav_buttons = [
    ("Upload & Edit Video", lambda: open_tab("Upload & Edit Video")),
    ("Voice Over", lambda: open_tab("Voice Over")),
    ("Download Video", lambda: open_tab("Download Video")),
    ("Duplicate Video", lambda: open_tab("Duplicate Video")),
]

for text, command in nav_buttons:
    nav_button = tk.Button(nav_frame, text=text, command=command, bg="#4CAF50", fg="white", padx=10, pady=5)
    nav_button.pack(side="left", padx=5, pady=5)

# Tab mặc định
open_tab("Upload & Edit Video")

# Tạo tab "Upload & Edit Video"
tabs["Upload & Edit Video"] = tk.Frame(main_frame)
tabs["Upload & Edit Video"].grid(row=0, column=0, sticky="nsew")

url_label = tk.Label(tabs["Upload & Edit Video"], text="URL Video:")
url_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)
url_entry = tk.Entry(tabs["Upload & Edit Video"], width=50)
url_entry.grid(row=0, column=1, padx=5, pady=5)

download_choice = tk.StringVar(value="tiktok")
radio_tiktok = tk.Radiobutton(tabs["Upload & Edit Video"], text="Tải từ TikTok", variable=download_choice, value="tiktok")
radio_tiktok.grid(row=1, column=0, sticky="w", padx=5, pady=5)
radio_url = tk.Radiobutton(tabs["Upload & Edit Video"], text="Tải từ URL", variable=download_choice, value="url")
radio_url.grid(row=1, column=1, sticky="w", padx=5, pady=5)
radio_youtube_short = tk.Radiobutton(tabs["Upload & Edit Video"], text="Tải từ YouTube Shorts", variable=download_choice, value="youtube_short")
radio_youtube_short.grid(row=1, column=2, sticky="w", padx=5, pady=5)

audio_label = tk.Label(tabs["Upload & Edit Video"], text="Chọn âm nhạc để ghép:")
audio_label.grid(row=2, column=0, sticky="w", padx=5, pady=5)
audio_entry = tk.Entry(tabs["Upload & Edit Video"], width=50)
audio_entry.grid(row=2, column=1, padx=5, pady=5)
select_audio_button = tk.Button(tabs["Upload & Edit Video"], text="Chọn âm nhạc", command=select_audio_file)
select_audio_button.grid(row=2, column=2, padx=5, pady=5)

add_music_var = tk.BooleanVar(value=True)
add_music_checkbox = tk.Checkbutton(tabs["Upload & Edit Video"], text="Ghép nhạc vào video", variable=add_music_var)
add_music_checkbox.grid(row=3, column=0, sticky="w", padx=5, pady=5)

product_link_label = tk.Label(tabs["Upload & Edit Video"], text="Nhập Link sản phẩm Shopee:")
product_link_label.grid(row=4, column=0, sticky="w", padx=5, pady=5)
product_link_entry = tk.Entry(tabs["Upload & Edit Video"], width=50)
product_link_entry.grid(row=4, column=1, padx=5, pady=5)

product_desc_label = tk.Label(tabs["Upload & Edit Video"], text="Nhập mô tả sản phẩm:")
product_desc_label.grid(row=5, column=0, sticky="w", padx=5, pady=5)
product_desc_entry = tk.Entry(tabs["Upload & Edit Video"], width=50)
product_desc_entry.grid(row=5, column=1, padx=5, pady=5)

start_button = tk.Button(tabs["Upload & Edit Video"], text="Bắt đầu", command=start_process, bg="#4CAF50", fg="white", padx=10, pady=5)
start_button.grid(row=6, column=1, pady=20)

log_box = tk.Text(tabs["Upload & Edit Video"], height=15, width=70, state="normal", bg="#f9f9f9")
log_box.grid(row=7, column=0, columnspan=3, padx=10, pady=10)
log_box.insert(tk.END, "Quá trình thực hiện...\n")

root.mainloop()

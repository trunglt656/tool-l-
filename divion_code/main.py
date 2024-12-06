import tkinter as tk
from tkinter import filedialog, messagebox
from downloader import download_video_tiktok, download_video_from_url
from video_editor import edit_video
from shopee_actions import open_shopee, open_library_video, upload_video, add_product_link, add_product_description

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

    if not video_url or not audio_file_path:
        log_callback("Cảnh báo: Vui lòng nhập đầy đủ thông tin (URL và âm nhạc).")
        return

    log_callback("Bắt đầu tải video...")
    try:
        if download_type == "tiktok":
            video_path = download_video_tiktok(video_url)
        elif download_type == "url":
            video_path = download_video_from_url(video_url)
        else:
            log_callback("Cảnh báo: Hãy chọn loại video cần tải.")
            return

        if not video_path:
            log_callback("Lỗi: Không tải được video.")
            return

        log_callback("Tải video thành công. Bắt đầu chỉnh sửa video...")
        edit_video(video_path, audio_file_path, log_callback)

        log_callback("Bắt đầu tải lên Shopee...")
        # open_shopee(log_callback)
        open_library_video(log_callback)
        open_shopee(log_callback)
        upload_video(log_callback)
        add_product_link(product_link, log_callback)
        add_product_description(product_description, log_callback)

        log_callback("Quá trình hoàn tất!")
    except Exception as e:
        log_callback(f"Lỗi: {e}")


def log_callback(*messages):
    combined_message = " ".join(messages)  # Ghép các thông báo lại thành một chuỗi
    log_box.config(state="normal")
    log_box.insert(tk.END, f"{combined_message}\n")
    log_box.see(tk.END)
    log_box.config(state="disabled")
    log_box.update_idletasks()  # Làm mới giao diện



def select_audio_file():
    audio_path = filedialog.askopenfilename(filetypes=[("Audio files", "*.mp3 *.wav")])
    if audio_path:
        audio_entry.delete(0, tk.END)
        audio_entry.insert(0, audio_path)

    


# Tạo giao diện
root = tk.Tk()
root.title("Tải và Chỉnh sửa Video TikTok")

# URL video
url_label = tk.Label(root, text="URL Video:")
url_label.pack(padx=10, pady=5)
url_entry = tk.Entry(root, width=50)
url_entry.pack(padx=10, pady=5)

# Tuỳ chọn loại tải video
download_choice = tk.StringVar(value="tiktok")

radio_tiktok = tk.Radiobutton(root, text="Tải từ TikTok", variable=download_choice, value="tiktok")
radio_tiktok.pack(padx=10, pady=5)

radio_url = tk.Radiobutton(root, text="Tải từ URL", variable=download_choice, value="url")
radio_url.pack(padx=10, pady=5)

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

# Thêm ô hiển thị log
log_box = tk.Text(root, height=15, width=70, state="normal")
log_box.pack(padx=10, pady=10)
log_box.insert(tk.END, "Quá trình thực hiện...\n")

root.mainloop()

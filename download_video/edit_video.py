import tkinter as tk
from tkinter import filedialog, messagebox
from moviepy import VideoFileClip, AudioFileClip, CompositeAudioClip

def edit_video(input_video_path, input_audio_path, output_video_path):
    try:
        # Load video gốc
        video = VideoFileClip(input_video_path)

        # Load nhạc mới
        audio = AudioFileClip(input_audio_path)

        # Cắt âm thanh nếu nó dài hơn video
        if audio.duration > video.duration:
            audio = audio.subclipped(0, video.duration)

        # Ghép nhạc mới vào video
        video_with_new_audio = video.with_audio(audio)

        # Xuất video mới
        video_with_new_audio.write_videofile(output_video_path, codec="libx264", audio_codec="aac")
        messagebox.showinfo("Thành công", "Video đã được chỉnh sửa và lưu thành công!")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Đã xảy ra lỗi: {e}")

def select_file(entry_widget, file_type):
    file_path = filedialog.askopenfilename(filetypes=file_type)
    if file_path:
        entry_widget.delete(0, tk.END)
        entry_widget.insert(0, file_path)

def save_file(entry_widget):
    file_path = filedialog.asksaveasfilename(defaultextension=".mp4", filetypes=[("MP4 files", "*.mp4")])
    if file_path:
        entry_widget.delete(0, tk.END)
        entry_widget.insert(0, file_path)

def start_editing():
    input_video = video_input_entry.get()
    input_audio = audio_input_entry.get()
    output_video = video_output_entry.get()

    if not input_video or not input_audio or not output_video:
        messagebox.showwarning("Cảnh báo", "Vui lòng chọn đầy đủ các tệp cần thiết!")
        return

    edit_video(input_video, input_audio, output_video)

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Chỉnh sửa Video")

# Giao diện chọn file
tk.Label(root, text="Video gốc:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
video_input_entry = tk.Entry(root, width=50)
video_input_entry.grid(row=0, column=1, padx=10, pady=5)
tk.Button(root, text="Chọn tệp", command=lambda: select_file(video_input_entry, [("Video files", "*.mp4 *.avi *.mkv")])).grid(row=0, column=2, padx=10, pady=5)

tk.Label(root, text="Âm thanh mới:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
audio_input_entry = tk.Entry(root, width=50)
audio_input_entry.grid(row=1, column=1, padx=10, pady=5)
tk.Button(root, text="Chọn tệp", command=lambda: select_file(audio_input_entry, [("Audio files", "*.mp3 *.wav")])).grid(row=1, column=2, padx=10, pady=5)

tk.Label(root, text="Video đầu ra:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
video_output_entry = tk.Entry(root, width=50)
video_output_entry.grid(row=2, column=1, padx=10, pady=5)
tk.Button(root, text="Lưu tại", command=lambda: save_file(video_output_entry)).grid(row=2, column=2, padx=10, pady=5)

# Nút bắt đầu chỉnh sửa
tk.Button(root, text="Chỉnh sửa Video", command=start_editing, bg="blue", fg="white").grid(row=3, column=0, columnspan=3, pady=20)

# Chạy ứng dụng
root.mainloop()












# from moviepy.video.io.VideoFileClip import VideoFileClip
# from moviepy.audio.io.AudioFileClip import AudioFileClip
# from moviepy.audio.AudioClip import CompositeAudioClip
# from moviepy import vfx, afx
# import os

# def edit_video_with_voiceover_and_effects(input_video_path, input_music_path, input_voice_path, output_video_path):
#     try:
#         # Kiểm tra sự tồn tại của tệp video và âm thanh
#         if not os.path.exists(input_video_path):
#             raise FileNotFoundError(f"Không tìm thấy tệp video: {input_video_path}")
#         if not os.path.exists(input_music_path):
#             raise FileNotFoundError(f"Không tìm thấy tệp nhạc: {input_music_path}")
#         if not os.path.exists(input_voice_path):
#             raise FileNotFoundError(f"Không tìm thấy tệp giọng nói: {input_voice_path}")

#         # Load video, nhạc nền và giọng nói
#         with VideoFileClip(input_video_path) as video, \
#                 AudioFileClip(input_music_path) as music, \
#                 AudioFileClip(input_voice_path) as voice:
            
#             # Điều chỉnh độ dài nhạc nền để khớp với video
#             if music.duration > video.duration:
#                 music = music.subclipped(0, video.duration)
#             elif music.duration < video.duration:
#                 music = music.loop(duration=video.duration)

#             # Giảm âm lượng nhạc nền (70%)
#             music = music.with_effects([afx.MultiplyVolume(0.5)])

#             # tăng âm lượng giọng nói
#             # voice = video.with_effects([afx.MultiplyStereoVolume(1.5)])

#             # Đặt thời điểm bắt đầu chèn giọng nói (ví dụ: xuất hiện sau 5 giây)
#             voice_start_time = 2  # Thay đổi thời gian này nếu cần
#             voice = voice.with_start(voice_start_time)

#             # Kết hợp nhạc nền và giọng nói
#             combined_audio = CompositeAudioClip([music, voice])

#             # Thêm âm thanh kết hợp vào video
#             video = video.with_audio(combined_audio)

#             # Áp dụng hiệu ứng: thay đổi tốc độ, giảm độ sáng
#             # video = video.with_effects([
#             #     vfx.MultiplySpeed(1.5),  # Tăng tốc độ video lên 1.5 lần
#             #     vfx.MultiplyColor(0.8)  # Giảm độ sáng 20%
#             # ])

#             # Xuất video
#             video.write_videofile(
#                 output_video_path,
#                 codec="libx264",
#                 audio_codec="aac",
#                 audio_bitrate="192k",
#                 threads=4,
#                 preset="medium"
#             )

#         print("Hoàn thành chỉnh sửa video với giọng nói, nhạc nền và hiệu ứng!")
#     except Exception as e:
#         print(f"Lỗi: {e}")

# # Đường dẫn file
# input_video = os.path.join("download_video", "asset", "video.mp4")  # Video gốc
# input_music = os.path.join("download_video", "asset", "amthanh.mp3")  # Nhạc nền
# input_voice = os.path.join("download_video", "asset", "amthanh_Gpt.mp3")  # Giọng nói
# output_video = os.path.join(".", "done_video_with_effects.mp4")  # Video đầu ra

# # Thực hiện chỉnh sửa
# edit_video_with_voiceover_and_effects(input_video, input_music, input_voice, output_video)

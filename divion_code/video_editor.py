from moviepy import VideoFileClip, AudioFileClip
from datetime import datetime
import os
import subprocess
from tkinter import filedialog, messagebox


def edit_video(input_video_path, input_audio_path, log_callback):
    try:
        video = VideoFileClip(input_video_path)
        audio = AudioFileClip(input_audio_path)
        log_callback(f"Đang chỉnh sửa video với audio nhạc được chọn...")

        if audio.duration > video.duration:
            audio = audio.subclipped(0, video.duration)

        video_with_new_audio = video.with_audio(audio)


        output_folder = r"D:\Affiliate\tool_sp\download_video\done_video"
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_video_path = os.path.join(output_folder, f"edited_video_{timestamp}.mp4")

        video_with_new_audio.write_videofile(output_video_path, codec="libx264", audio_codec="aac")
        log_callback(f"Thành công", f"Video đã được chỉnh sửa và lưu tại:\n{output_video_path}")
        print("Thành công", f"Video đã được chỉnh sửa và lưu tại:\n{output_video_path}")
        
        send_video_to_phone(output_video_path, log_callback)
    except Exception as e:
        messagebox.showerror("Lỗi", f"Đã xảy ra lỗi khi chỉnh sửa video: {e}")

# Hàm gửi video qua ADB
def send_video_to_phone(video_path, log_callback):
    try:
        result = subprocess.run(["adb", "devices"], capture_output=True, text=True)
        if "device" not in result.stdout:
            print("Lỗi: Không tìm thấy thiết bị Android.")
            return
        
        video_name = os.path.basename(video_path)
        phone_video_path = f"/sdcard/Download/{video_name}"
        
        subprocess.run(["adb", "push", video_path, phone_video_path])
        log_callback(f"Video đã được gửi đến thiết bị Android: {phone_video_path}")
        print(f"Video đã được gửi đến thiết bị Android: {phone_video_path}")
    except Exception as e:
        print(f"Lỗi: Đã xảy ra lỗi khi gửi video: {e}")

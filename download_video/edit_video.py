# from moviepy import VideoFileClip, AudioFileClip, CompositeAudioClip

# def edit_video(input_video_path, input_audio_path, output_video_path):
#     # Load video gốc
#     video = VideoFileClip(input_video_path)

#     # Load nhạc mới
#     audio = AudioFileClip(input_audio_path)

#     # Cắt âm thanh nếu nó dài hơn video
#     if audio.duration > video.duration:
#         audio = audio.subclipped(0, video.duration)

#     # Ghép nhạc mới vào video
#     new_audio = CompositeAudioClip([audio])
#     video_with_new_audio = video.with_audio(new_audio)

#     # Xuất video mới
#     video_with_new_audio.write_videofile(output_video_path, codec="libx264", audio_codec="aac")

# # Đường dẫn file
# input_video = "./asset/video.mp4"  # Video gốc
# input_audio = "./asset/amthanh.mp3"  # Nhạc mới
# output_video = "./done_video.mp4"  # Video đầu ra

# # Thực hiện chỉnh sửa
# edit_video(input_video, input_audio, output_video)




from moviepy import VideoFileClip, AudioFileClip, CompositeAudioClip, vfx

def edit_video(input_video_path, input_audio_path, output_video_path):
    # Load video gốc
    video = VideoFileClip(input_video_path)

    # Load âm thanh mới
    audio = AudioFileClip(input_audio_path)

    # Tăng tốc độ âm thanh lên 1.1 lần (sử dụng vfx.speedx)
    audio = audio.fx(vfx.speedx, factor=1.1)

    # Cắt âm thanh nếu nó dài hơn video
    if audio.duration > video.duration:
        audio = audio.subclip(0, video.duration)

    # Ghép âm thanh mới vào video
    video_with_audio = video.set_audio(audio)

    # Xuất video mới
    video_with_audio.write_videofile(output_video_path, codec="libx264", audio_codec="aac")

# Đường dẫn file
input_video = "./asset/video.mp4"  # Video gốc
input_audio = "./asset/amthanh.mp3"  # Nhạc mới
output_video = "./done_video.mp4"  # Video đầu ra

# Thực hiện chỉnh sửa
edit_video(input_video, input_audio, output_video)

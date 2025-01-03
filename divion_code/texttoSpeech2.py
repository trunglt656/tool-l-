import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"D:\Affiliate\buik video\apiKey.json"

import tkinter as tk
from tkinter import filedialog, messagebox
from moviepy import VideoFileClip, AudioFileClip
from google.cloud import texttospeech
import os

# Function to select video
def select_video():
    video_path = filedialog.askopenfilename(title="Select a Video File", filetypes=[("MP4 files", "*.mp4")])
    video_entry.delete(0, tk.END)
    video_entry.insert(0, video_path)

# Function to specify output file
def specify_output():
    output_path = filedialog.asksaveasfilename(title="Save Merged Video As", defaultextension=".mp4", filetypes=[("MP4 files", "*.mp4")])
    output_entry.delete(0, tk.END)
    output_entry.insert(0, output_path)

# Function to generate Vietnamese speech using Google Cloud TTS
def generate_vietnamese_speech(text_input, output_audio_path):
    client = texttospeech.TextToSpeechClient()

    synthesis_input = texttospeech.SynthesisInput(text=text_input)

    voice = texttospeech.VoiceSelectionParams(
        language_code="vi-VN",  # Vietnamese
        name="vi-VN-Neural2-A",  # High-quality Vietnamese voice
        ssml_gender=texttospeech.SsmlVoiceGender.FEMALE
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3,
        speaking_rate=1.4,  # Tốc độ giọng nói
        pitch=1.3,  # Độ cao của giọng nói
    )

    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    with open(output_audio_path, "wb") as out:
        out.write(response.audio_content)
    print("Vietnamese speech audio saved successfully!")

# Function to process the video
def process_video():
    video_path = video_entry.get()
    text_input = text_box.get("1.0", tk.END).strip()
    output_path = output_entry.get()

    if not video_path or not text_input or not output_path:
        messagebox.showerror("Error", "Please fill in all fields!")
        return

    try:
        # Generate Vietnamese speech
        audio_path = "temp_audio.mp3"
        generate_vietnamese_speech(text_input, audio_path)

        # Load the video and attach the generated audio
        video_clip = VideoFileClip(video_path)
        audio_clip = AudioFileClip(audio_path)

        final_clip = video_clip.with_audio(audio_clip)
        final_clip.write_videofile(output_path, codec="libx264", audio_codec="aac")

        # Cleanup temporary audio file
        os.remove(audio_path)

        messagebox.showinfo("Success", f"Video saved successfully at {output_path}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# GUI Layout
root = tk.Tk()
root.title("Vietnamese Text-to-Speech Video Merger")
root.geometry("600x450")

# Select Video Section
tk.Label(root, text="Select Video File:").pack(pady=5)
video_entry = tk.Entry(root, width=60)
video_entry.pack(pady=5)
tk.Button(root, text="Browse", command=select_video).pack()

# Text Input Section
tk.Label(root, text="Enter Text for Speech:").pack(pady=5)
text_box = tk.Text(root, width=60, height=10)
text_box.pack(pady=5)

# Output File Section
tk.Label(root, text="Specify Output File:").pack(pady=5)
output_entry = tk.Entry(root, width=60)
output_entry.pack(pady=5)
tk.Button(root, text="Browse", command=specify_output).pack()

# Process Button
tk.Button(root, text="Generate Video", command=process_video, bg="green", fg="white").pack(pady=20)

root.mainloop()

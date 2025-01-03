# # # cau lenh kiem tra list voice edge-tts --list-voice
# # vi-VN-HoaiMyNeural                 Female    General                Friendly, Positive
# # vi-VN-NamMinhNeural 

# # apikey: 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

# # openai.api_key = "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"  # Khóa API của OpenAI


# from openai import OpenAI

# # Paste your OpenAI API key here!
# client = OpenAI(api_key="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")

# # Audio file path
# audio_file = "./download_video/asset/textTospeech/test.wav"

# # Speech to text
# audio_file = open(audio_file,'rb')
# transcript = client.audio.transcriptions.create(model='whisper-1',file=audio_file, response_format='text')
# print(transcript)

# # Text to speech
# speech_file_path = "voice.mp3"
# response = client.audio.speech.create(model='tts-1', voice='shimmer', input=transcript)
# response.stream_to_file(speech_file_path)
# print("Audio Generated Successfully")




import subprocess
import time

def run_adb_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        result.check_returncode()
        print(f"Đã chạy lệnh: {command}")
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Lỗi khi chạy lệnh: {e}")
        return ""

while True:
    run_adb_command("adb shell input tap 391 736")
    time.sleep(1)  # Đợi 1 giây giữa các lần click
    run_adb_command("adb shell input tap 684 740")
    time.sleep(1)  # Đợi 1 giây giữa các lần click


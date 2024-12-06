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

# def input_text_by_character(text):
#     for char in text:
#         if char == ' ':
#             run_adb_command("adb shell input keyevent 62")
#         elif char == '#':
#             run_adb_command("adb shell input keyevent 8")
#         else:
#             run_adb_command(f"adb shell input text '{char}'")
#         time.sleep(0.1)


# Hàm nhập chuỗi ký tự từng ký tự một (bao gồm ký tự đặc biệt)
def input_text_by_character(text, log_callback):
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
        # time.sleep(0.1)  # Thêm thời gian chờ giữa các ký tự
    log_callback(f"Đã nhập: {text}")
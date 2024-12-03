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
    time.sleep(2)

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

# Main
if __name__ == "__main__":
    # Nhập link sản phẩm và mô tả
    product_link = input("Nhập link sản phẩm: ")
    product_description = input("Nhập mô tả sản phẩm: ")

    # Kiểm tra kết nối thiết bị
    print("Kiểm tra kết nối thiết bị...")
    devices = run_adb_command("adb devices")
    if "device" not in devices:
        print("Không có thiết bị nào được kết nối. Hãy kiểm tra lại.")
    else:
        # Thực hiện các thao tác tự động
        open_shopee()
        upload_video()
        add_product_link(product_link)
        add_product_description(product_description)

        print("Hoàn tất!")

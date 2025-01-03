import time
from adb_utils import run_adb_command, input_text_by_character

def open_shopee(log_callback):
    log_callback(f"Đang mở ứng dụng Shopee...")
    run_adb_command("adb shell monkey -p com.shopee.vn -c android.intent.category.LAUNCHER 1")
    time.sleep(5)

def open_library_video(log_callback):
    log_callback(f"Đang mở ứng dụng Thư viện video...")
    run_adb_command("adb shell am start -n com.miui.gallery/.activity.HomePageActivity")
    time.sleep(3)

def upload_video(log_callback):
    log_callback(f"Đang tải video lên...")
    run_adb_command("adb shell input tap 1015 157")  # Nhấn nút upload
    time.sleep(2)

    # Chọn đăng video(tùy tk)
    run_adb_command("adb shell input tap 486 2000")  # Nhấn nút upload
    time.sleep(4)


    run_adb_command("adb shell input tap 865 1875")  # Chọn thư viện
    time.sleep(3)
    run_adb_command("adb shell input tap 145 471")  # Chọn video đầu tiên
    time.sleep(5)
    run_adb_command("adb shell input tap 945 2253")  # nhấn tiếp theotheo
    time.sleep(3)

    # nhấn cái thiện video 
    run_adb_command("adb shell input tap 999 546")  # Nhấn làm đẹp 
    time.sleep(10)


    run_adb_command("adb shell input tap 969 2189")  # Nhấn Tiếp theo lần nữa
    time.sleep(3)
    # cho nhanh , co the xóa
    run_adb_command("adb shell input tap 821 685")  # Nhấn thêm sản phẩm
    time.sleep(4)
    run_adb_command("adb shell input tap 1041 171")  # Chọn link
    time.sleep(2)
    run_adb_command("adb shell input tap 533 601")  # Nhấn vào ô nhập link

def add_product_link(link, log_callback):
    log_callback(f"Đang thêm sản phẩm bằng link...")
    run_adb_command("adb shell input tap 821 685")  # Nhấn thêm sản phẩm
    time.sleep(4)
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

# def add_product_description(description):
#     print("Đang nhập mô tả sản phẩm...")
#     run_adb_command("adb shell input tap 593 417")  # Chỉnh lại tọa độ nếu cần
#     time.sleep(2)
#     input_text_by_character(description)
#     time.sleep(2)

# Hàm nhập mô tả sản phẩm
def add_product_description(description, log_callback):
    log_callback("Đang nhập mô tả sản phẩm...")
    
    # Nhấn vào ô mô tả sản phẩm
    run_adb_command("adb shell input tap 593 417")  # Chỉnh lại tọa độ nếu cần
    time.sleep(2)

    # Sử dụng hàm nhập chuỗi ký tự từng ký tự một
    input_text_by_character(description,log_callback)
    time.sleep(2)

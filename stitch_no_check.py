import subprocess
import time

# Hàm khởi tạo
def run_adb_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        result.check_returncode()  # Kiểm tra mã trả về
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Lỗi khi chạy lệnh: {e}")
        return ""

# Hàm này chạm vào nút chia sẻ
def chose_video():
    time.sleep(1)
    # Chạm vào nút chia sẻ
    run_adb_command("adb shell input tap 1003 1981")
    time.sleep(5)  # Đợi 5 giây

    # Thao tác vuốt để xem nút ghép
    run_adb_command("adb shell input swipe 712 2183 261 2183 500")




# Hàm này kiểm tra xem nút stitch có tồn tại không
def check_button_exists(button_text):
    # Tạo bản sao UI
    run_adb_command("adb shell uiautomator dump /sdcard/window_dump.xml")
    
    # Lấy tệp về
    run_adb_command("adb pull /sdcard/window_dump.xml .")

    # Kiểm tra nút có tồn tại không
    try:
        with open("window_dump.xml", "r", encoding="utf-8") as file:
            content = file.read()
            return button_text in content  # Kiểm tra sự tồn tại của button_text
    except FileNotFoundError:
        print("Tệp window_dump.xml không tìm thấy.")
        return False
    
    

# lấy link sản phẩm 
def get_product_link():
    # Lấy link sản phẩm
    run_adb_command("adb shell input tap 180 1800")  # Click vào giỏ hàng ---  vấn đề  
    time.sleep(8)
    run_adb_command("adb shell input tap 812 422")  # Click nút chia sẻ ko full màn
    # run_adb_command("adb shell input tap 806 160")  # Click nút chia sẻ full màn
    time.sleep(7)
    run_adb_command("adb shell input tap 322 2183")  # Click sao chép link
    time.sleep(5)
    # Quay lại 2 lần
    run_adb_command("adb shell input keyevent 4")
    time.sleep(3)
    run_adb_command("adb shell input keyevent 4")


# kéo timeline video                                     -------------------- cần chỉnh sửa
def swipe_full_timeline():
    # Kéo khung timeline
    time.sleep(5)
    # # Nhấn giữ tại (500, 1500) trong 1000 milliseconds 366 2150
    # run_adb_command("adb shell input swipe 320 2160 320 2160 1000")
    # Kéo đến (500, 800)
    run_adb_command("adb shell input swipe 366 2150 1030 2160 400")




# Quy trình chính
# chose_video()  # Gọi hàm chose_video

    # Gọi hàm kiểm tra với hai hình
print("Thực hiện ghép nối video.")
time.sleep(3)
# Thực hiện ghép nối video ở đây
get_product_link()
# Nhấn chia sẻ và nhấn ghép nối
time.sleep(5)
run_adb_command("adb shell input tap 1000 1963")  # Nhấn chia sẻ
print("Nhấn nút chia sẻ")
time.sleep(5)
# kéo xem nút ghép 
run_adb_command("adb shell input swipe 712 2183 261 2183 500")
time.sleep(3)
print("Nhấn nút ghép nối")
run_adb_command("adb shell input tap 595 2165")  # Nhấn ghép nối
print("Kéo Timeline")
time.sleep(5)
swipe_full_timeline()  # Kéo full timeline
time.sleep(10)
# # nhấn núp tiếp theo
run_adb_command("adb shell input tap 955 160")
time.sleep(10)
# time.sleep(7)
print("nhấn ghi hình")
run_adb_command("adb shell input swipe 531 1853 531 1853 300") #ghi hinhf
time.sleep(3)
run_adb_command("adb shell input keyevent 3")
time.sleep(2)
# run_adb_command("adb shell input swipe 531 1853 531 1853 1500") #ghi hinh
run_adb_command("adb shell monkey -p com.shopee.vn -c android.intent.category.LAUNCHER 1")
time.sleep(10)

# quayai
run_adb_command("adb shell input tap 67 163")
time.sleep(5)
# đồng ý hủy 
run_adb_command("adb shell input tap 525 2196")
# kéo timeline dự phòng
run_adb_command("adb shell input swipe 547 2155 1030 2160 400")
time.sleep(5)
# # nhấn núp tiếp theo
run_adb_command("adb shell input tap 955 160")
time.sleep(9)
print("Nhấn ghi hình lần 2")
run_adb_command("adb shell input swipe 531 1853 531 1853 500") #ghi hinhf
time.sleep(5)
# tiếp theo
run_adb_command("adb shell input tap 861 1862")
time.sleep(7)
run_adb_command('adb shell input tap 923 2183') # tiep theo
time.sleep(6)
run_adb_command('adb shell input tap 755 685') #them sp
time.sleep(6)
# ko ở trong profile
# run_adb_command('adb shell input tap 1008 161')
# ở trg profile
run_adb_command('adb shell input tap 1006 136') #link
print("link button")
time.sleep(5)
run_adb_command('adb shell input tap 220 480') # o link 
time.sleep(5)
run_adb_command('adb shell input tap 568 815')# paste link 
time.sleep(3)
run_adb_command('adb shell input tap 547 827')# nhap lin
time.sleep(4)
run_adb_command('adb shell input tap 70 2210')#chon tat ca
time.sleep(4)
run_adb_command('adb shell input tap 618 2210')#them sp 
time.sleep(4)
# run_adb_command('adb shell input tap 381 561')#click them hasta
run_adb_command('adb shell input tap 381 561')#click them hastag
run_adb_command('adb shell input tap 150 780')#click them hastag 
run_adb_command('adb shell input tap 381 561')#click them hastag
run_adb_command('adb shell input tap 172 882')#click them hastag 
run_adb_command('adb shell input tap 381 561')#click them hastag
run_adb_command('adb shell input tap 171 980')#click them hastag 
# run_adb_command('adb shell input tap 400 550') #them hastag
# time.sleep(4)
# run_adb_command('adb shell input tap 160 666')# chon hastag
# time.sleep(4)
# run_adb_command('adb shell input tap 592 1751')# dóng hasrag
# time.sleep(4)
# run_adb_command('adb shell input tap 590 2277') #đang len
# hoàn thành
# tiếp đến lướt sang trái rồi xuống dưới để lên video mớ
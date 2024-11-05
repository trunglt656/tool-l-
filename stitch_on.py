import subprocess
import time
import cv2

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
    



# Hàm này kiểm tra giỏ hàng với hai hình ảnh khác nhau
def check_cart_icon_images():
    # Đọc ảnh chụp màn hình và ảnh mẫu biểu tượng giỏ hàng
    screen = cv2.imread('screen.png')
    cart_icon_1 = cv2.imread('cart_icon_template.png')  # Hình mẫu giỏ hàng 1
    cart_icon_2 = cv2.imread('cart_icon_template_2.png')  # Hình mẫu giỏ hàng 2

    # So khớp mẫu cho biểu tượng giỏ hàng đầu tiên
    res1 = cv2.matchTemplate(screen, cart_icon_1, cv2.TM_CCOEFF_NORMED)
    _, max_val1, _, max_loc1 = cv2.minMaxLoc(res1)

    # So khớp mẫu cho biểu tượng giỏ hàng thứ hai
    res2 = cv2.matchTemplate(screen, cart_icon_2, cv2.TM_CCOEFF_NORMED)
    _, max_val2, _, max_loc2 = cv2.minMaxLoc(res2)

    # Kiểm tra xem có ít nhất một biểu tượng giỏ hàng nào được phát hiện
    if max_val1 > 0.8 or max_val2 > 0.5:  # Ngưỡng khớp mẫu, có thể điều chỉnh
        if max_val1 > 0.8:
            print(f"Giỏ hàng 1 được phát hiện tại {max_loc1}")
        if max_val2 > 0.5:
            print(f"Giỏ hàng 2 được phát hiện tại {max_loc2}")
        return True
    else:
        print("Không tìm thấy giỏ hàng!")
        return False
    

# lấy link sản phẩm 
def get_product_link():
    # Lấy link sản phẩm
    run_adb_command("adb shell input tap 180 1800")  # Click vào giỏ hàng ---  vấn đề  
    time.sleep(12)
    # run_adb_command("adb shell input tap 812 422")  # Click nút chia sẻ ko full màn
    run_adb_command("adb shell input tap 806 160")  # Click nút chia sẻ full màn
    time.sleep(9)
    run_adb_command("adb shell input tap 322 2183")  # Click sao chép link
    time.sleep(8)
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
chose_video()  # Gọi hàm chose_video
button_text = "Ghép nối"  # Thay bằng tên nút bạn muốn kiểm tra
if check_button_exists(button_text):
    print("Nút 'Ghép nối' tồn tại! Tiến hành kiểm tra giỏ hàng.")
    time.sleep(4)
    # Chụp ảnh màn hình để kiểm tra giỏ hàng
    run_adb_command("adb shell input keyevent 4")
    time.sleep(8)
    run_adb_command("adb shell screencap -p /sdcard/screen.png")
    time.sleep(1)
    run_adb_command("adb pull /sdcard/screen.png .")
    
    if check_cart_icon_images():  # Gọi hàm kiểm tra với hai hình
        print("Thực hiện ghép nối video.")
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
        # run_adb_command("adb shell input swipe 531 1853 531 1853 1500") #ghi hinhf

        run_adb_command("adb shell monkey -p com.shopee.vn -c android.intent.category.LAUNCHER 1")
        time.sleep(10)
        
# quay lai
        run_adb_command("adb shell input tap 67 163")
        time.sleep(5)
        # đồng ý hủy 
        run_adb_command("adb shell input tap 525 2196")

        # kéo timeline dự phòng
        run_adb_command("adb shell input swipe 461 2162 1030 2160 400")


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

# ở trong profile
        run_adb_command('adb shell input tap 1006 136') #link 


        print("link button")
        time.sleep(5)
        run_adb_command('adb shell input tap 220 480') # o link 
        time.sleep(5)
        run_adb_command('adb shell input tap 568 815')# paste link 
        time.sleep(3)
        run_adb_command('adb shell input tap 547 827')# nhap link

        time.sleep(4)
        run_adb_command('adb shell input tap 70 2210')#chon tat ca
        time.sleep(4)
        run_adb_command('adb shell input tap 618 2210')#them sp 
        time.sleep(4)


        # run_adb_command('adb shell input tap 381 561')#click them hastag

        run_adb_command('adb shell input tap 381 561')#click them hastag
        run_adb_command('adb shell input tap 150 780')#click them hastag 2

        run_adb_command('adb shell input tap 381 561')#click them hastag
        run_adb_command('adb shell input tap 172 882')#click them hastag 3

        run_adb_command('adb shell input tap 381 561')#click them hastag
        run_adb_command('adb shell input tap 163 670')#click them hastag 3



        # run_adb_command('adb shell input tap 400 550') #them hastag
        # time.sleep(4)
        # run_adb_command('adb shell input tap 160 666')# chon hastag
        # time.sleep(4)
        # run_adb_command('adb shell input tap 592 1751')# dóng hasrag
        # time.sleep(4)
        # run_adb_command('adb shell input tap 590 2277') #đang len 

        # hoàn thành
        # tiếp đến lướt sang trái rồi xuống dưới để lên video mới


 


    else:
        print("Không có giỏ hàng. Kéo xuống video dưới và thực hiện lại.")
        # run_adb_command("adb shell input keyevent 4")
        time.sleep(4)
        run_adb_command("adb shell input swipe 500 1376 500 500 200") 
else:
    print("Nút 'Ghép nối' không tồn tại! Kéo xuống video dưới và thực hiện lại.")
    run_adb_command("adb shell input keyevent 4")
    time.sleep(3)
    run_adb_command("adb shell input swipe 500 1376 500 500 200") 



# Smart_home_chatGPT
Hướng dẫn cài đặt thư viện và setup hệ thống Nhà thông minh sử dụng chatGPT.

Hệ thống sử dụng ngôn ngữ lập trình Python với máy tính nhúng Raspberry Pi chạy trên hệ điều hành Linux.

*Cài đặt các thư viện sử dụng: Để cài đặt thư viện python hỗ trợ ta mở Terminal vào thực hiện các lệnh sau:

    - cài đặt thư viện 'openai'
        pip install openai

    - cài đặt thư viện 'playsound'
        pip install playsound

    - cài đặt thư viện 'SpeechRecognition'
        pip install SpeechRecognition

    - cài đặt thư viện 'gTTS'
        sudo apt-get update
        sudo apt-get install python-rpi.gpio python3-rpi.gpio

* Tiếp theo là cấu hình Raspberry Pi.

    Bước 1: Chỉnh sửa tệp rc.local
        - Bạn có thể sử dụng trình soạn thảo văn bản để mở tệp rc.local bằng lệnh sau:

            sudo nano /etc/rc.local

        - Sau đó, bạn sẽ thấy một tệp văn bản, và bạn có thể thêm lệnh để chạy file code của bạn ngay trước dòng "exit 0". Ví dụ:

            python3 /home/pi/myfile.py &

        Lưu tệp rc.local và đóng nó lại.
    Bước 2: Khởi động lại Raspberry Pi

    - Cuối cùng, bạn cần khởi động lại Raspberry Pi để thay đổi được áp dụng. Bạn có thể sử dụng lệnh sau để khởi động lại:

        sudo reboot
        
        
 * Setup phần cứng:
        -Sơ đồ mạch nguyên lý: https://github.com/thelam2301/Smart_home_chatGPT/blob/097bceef38e2e2bdecf670c6982b3e6d409eb38f/S%C6%A1%20%C4%91%E1%BB%93%20m%E1%BA%A1ch%20nguy%C3%AAn%20l%C3%BD.JPG
    Các thiết bị điện ( bóng đèn, quạt ) được điều khiển bởi Raspberry Pi thông qua relay 5V- 220V với nguyên lý như sau:
    Các chân điều khiển của module relay được kết nối với các chân GPIO của Raspberry Pi. Khi có tín hiệu điều khiển bật/tắt từ Raspberry Pi, các module này hoạt động  như các công tắc điện đóng mở nguồn điện cung cấp chó các thiết bị.

 
 
 

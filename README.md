# Smart_home_chatGPT
Hướng dẫn cài đặt thư viện và setup hệ thống Nhà thông minh sử dụng chatGPT.

Hệ thống sử dụng ngôn ngữ lập trình Python với máy tính nhúng Raspberry Pi.

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

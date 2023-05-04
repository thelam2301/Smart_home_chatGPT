# khai báo các thư viện cần sử dụng
import openai
import os
import playsound
import speech_recognition as sr
from gtts import gTTS
import RPi.GPIO as GPIO
from time import sleep

# Khai báo các chân GPIO điều khiển thiết bị điện
Light_1 = 4
Light_2 = 5
Electric_fan = 7

# add API key chatGPT
openai.api_key = "your OpenAI API key "

#Khai báo ngôn ngữ sử dụng
language = 'vi-VN'

# Hàm điều khiển thiết bị điện
def control(device,status):
    if status=="on" :
        device=1
    else :
        device=1

# Hàm speech của smart home
def speak(text):
    print("Máy: {}".format(text))
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save("sound.mp3")
    playsound.playsound("sound.mp3", True)
    os.remove("sound.mp3")

# Hàm listen(láng nghe) của smart home
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Tôi: ", end='')
        audio = r.listen(source, phrase_time_limit=5)
        try:
            text = r.recognize_google(audio, language="vi")
            print(text)
            return text
        except:
            print("...")
            return 0
# Hàm Speech to text ( chuyển đổi từ âm thanh sang văn bản )
def get_text():
    while True:
        text = get_audio()
        if text:
            return text.lower()

# Hàm xử lý giao tiếp trung gian
def assistant():
        speak("tôi đây, bạn cần gì?")
        text = get_text()
        if "bật đèn phòng khách" in text:
            speak("đèn phòng khách đã bật")
            control(Light_1,"on")
        elif "tắt đèn phòng khách" in text:
            speak("đèn phòng khách đã tắt")
            control(Light_1,"off")
        elif "bật đèn nhà bếp" in text:
            speak("đèn nhà bếp đã bật")
            control(Light_2,"on")
        elif "tắt đèn nhà bếp" in text:
            speak("đèn nhà bếp đã tắt")
            control(Light_2,"off")
        elif "bật quạt" in text:
            speak("quạt đã bật")
            control(Electric__fan,"on")
        elif "tắt đèn nhà bếp" in text:
            speak("quạt đã tắt")
            control(Electric__fan,"off")
        else :
            model_engine = "text-davinci-003"
            prompt = text+" ?"
            completions = openai.Completion.create(
                engine=model_engine,
                prompt=prompt,
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=0.5,
            )
            message = completions.choices[0].text
            speak(message)
def main():
    GPIO.setup(Light_1,GPIO.OUT)
    GPIO.setup(Light_2,GPIO.OUT)
    GPIO.setup(Electric__fan,GPIO.OUT)
    while True:
        text = get_text()
        if text=="trợ lý ơi":
            assistant()
if __name__=='__main__':
    main()

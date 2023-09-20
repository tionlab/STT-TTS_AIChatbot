from tts import Say
from stt import Listen
from welcome import Welcome
from answer import Answer
import time

Welcome()
Say("안녕하세요ㅛ!")
print("안녕ㅎㅏ세요ㅛ!")

while True:
    listen = Listen()
    if listen.text:
        if listen.text == "종료해 줘" and "종료해줘":
            print("ㅇㅔ이ㅇㅏ이: ㅂㅏ이 ㅂㅏ이")
            Say("바잉바잉")
            time.sleep(5)
            break
        Answer(listen.text)
    time.sleep(2)
from tts import Say
from stt import Listen
from welcome import Welcome
from answer import Answer
import time

Welcome()

Say("hello!")
print("hellooo!")

while True:
    listen = Listen()
    if listen.text:
        if listen.text == "Shut down" and "Shutdown":
            print("Temmie : Goooood byee!")
            Say("gooood bye!")
            time.sleep(5)
            break
        Answer(listen.text)
    time.sleep(2)

import speech_recognition as sr

class Listen:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.audio = None
        self.text = None
        try:
            with sr.Microphone() as source:
                print("듣는 중 이ㅇㅔㅔㅔ요!")
                self.recognizer.adjust_for_ambient_noise(source)
                self.audio = self.recognizer.listen(source, timeout=None, phrase_time_limit=3)
            self.text = self.recognizer.recognize_google(self.audio, language="ko-KR")
            print("ㄴㅏ : " +  self.text)
        except sr.UnknownValueError:
            print("머ㅓㅝ라ㅏ고요?")
        except sr.RequestError as e:
            print("갑ㅈㅏ기 ㅇㅏㄴ들리는 ㄱㅓㅅ 같아ㅏㅇ...;; {0}".format(e))


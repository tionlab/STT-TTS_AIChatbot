import speech_recognition as sr

class Listen:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.audio = None
        self.text = None
        
        try:
            with sr.Microphone() as source:
                print("Listeningggg!")
                self.recognizer.adjust_for_ambient_noise(source)
                self.audio = self.recognizer.listen(source, timeout=None, phrase_time_limit=3)
            self.text = self.recognizer.recognize_google(self.audio, language="ko-KR")
            print("You : " +  self.text)
        except sr.UnknownValueError:
            print("Pardon?")
        except sr.RequestError as e:
            print("Suddenly I can't hear you... {0}".format(e))


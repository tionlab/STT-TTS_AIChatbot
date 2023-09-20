import pygame
import tempfile
from gtts import gTTS


class Say:
    def __init__(self, text):
        tts = gTTS(text=text, lang='ko')

        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_file:
            temp_file_name = temp_file.name
            tts.save(temp_file_name)

        pygame.mixer.init()
        pygame.mixer.music.load(temp_file_name)
        pygame.mixer.music.play()

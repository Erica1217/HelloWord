from gtts import gTTS
import pygame
import os.path

class WordSpeaker:

    @staticmethod
    def speak(word):
        # os.path.isfile(fname)

        path = "../resource/mp3/"

        tts = gTTS(word, 'en')
        tts.save(path + tts.text + ".mp3")

        pygame.mixer.init()
        pygame.mixer.music.load(path + tts.text + ".mp3")
        pygame.mixer.music.play()
        clock = pygame.time.Clock()

        while pygame.mixer.music.get_busy():
            clock.tick(30)
        pygame.mixer.quit()

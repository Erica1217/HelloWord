from gtts import gTTS
import pygame
import os.path

class WordSpeaker:

    @staticmethod
    def speak(word):
        path = "../resource/mp3/" + word + ".mp3"

        if not os.path.isfile(path):
            tts = gTTS(word, 'en')
            tts.save(path)

        pygame.mixer.init()
        pygame.mixer.music.load(path)
        pygame.mixer.music.play()
        clock = pygame.time.Clock()

        while pygame.mixer.music.get_busy():
            clock.tick(30)
        pygame.mixer.quit()

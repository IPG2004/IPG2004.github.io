PYGAME_HIDE_SUPPORT_PROMPT = 1
import pygame
# import time as t

def sound(time):
    pygame.init()
    pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=4096)
    # pygame.mixer.init()
    pygame.mixer.music.load('beep.wav')
    pygame.time.delay(1000)
    pygame.mixer.music.play()
    pygame.time.delay(1000)
    pygame.mixer.music.stop()

if __name__ == '__main__':
    sec = 2      # Duración en segundos

    sound(sec)
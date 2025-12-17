import pygame

pygame.mixer.init()

def tocar_tema():
    pygame.mixer.music.load("sounds/theme.ogg")
    pygame.mixer.music.set_volume(0.2)  # 0.0 a 1.0
    pygame.mixer.music.play(-1)  # -1 = loop infinito


def parar_tema():
    pygame.mixer.music.stop()

def tocar_tiro():
    tiro_sound = pygame.mixer.Sound("sounds/shot.ogg")
    tiro_sound.set_volume(0.5)
    tiro_sound.play()

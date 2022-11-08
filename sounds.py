"""Class SoundManager du jeu Redem mode PVE en python."""

import pygame

#Classe pour le son du jeu
class SoundManager:
    def __init__(self):
        # Dictionnaire pour les sons
        self.sounds = {
            'arc': pygame.mixer.Sound("Assets/Sound/arc3.mp3"),
            'music': pygame.mixer.Sound("Assets/Sound/music.mp3")
        }

    # Définition de jouer le son
    def play(self, name):
        self.sounds[name].play()

    # Définition de jouer le son en boucle
    def boucle(self, name):
        self.sounds[name].play(500, 0, 5000)

    # Définition de régler le volume du jeu
    def volume(self, name):
        self.sounds[name].set_volume(0.1)
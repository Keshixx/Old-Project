"""Class Menu du jeu Redem mode PVE en python."""

import pygame
import animation

#class du menu
class Menu(animation.AnimateSprite):
    def __init__(self, game):
        super().__init__("ls-")
        self.game = game

    def update_animation_menu(self):
        self.animate_menu()
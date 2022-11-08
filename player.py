"""Class Player du jeu Redem mode PVE en python."""

import pygame
from projectile import Projectile
import animation
from sounds import SoundManager

#Classe du personnage que l'on incarne dans le jeu
class Player(animation.AnimateSprite):

    def __init__(self, game):
        super().__init__('Ggdqc3-', (150, 111))
        self.game = game
        self.sound_manager = SoundManager()
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 5
        self.all_projectiles = pygame.sprite.Group()
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 428

    #Définition pour faire animer le personnage
    def update_animation(self):
        self.animate(0.4)

    #Définition pour afficher sa barre de vie
    def update_health_bar(self, surface):
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 30, self.rect.y + 10, self.max_health, 7])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 30, self.rect.y + 10, self.health, 7])

    #Définition pour que le joueur prenne des dégâts et si sa vie tombe à 0 alors game over
    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount
        else:
            self.game.game_over()

    #Définition pour lancer des projectiles
    def launch_projectile(self):
        self.start_animation()
        self.sound_manager.play('arc')
        self.all_projectiles.add(Projectile(self))

    #Définition pour que le personnage se déplace à droite
    def move_right(self):

        if not self.game.check_collision(self, self.game.all_mob):
            self.rect.x += self.velocity

    #Définition pour que le personnage se déplace à gauche
    def move_left(self):
        self.rect.x -= self.velocity

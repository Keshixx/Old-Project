"""Class Projectile du jeu Redem mode PVE en python."""

import pygame

#classe projectile qui permet au personnage de lancer des flèches
class Projectile(pygame.sprite.Sprite):

    def __init__(self, player):
        super().__init__()
        self.velocity = 15
        self.player = player
        self.image = pygame.image.load('Assets/Character/Adventurer/Arc/arrow.png')
        #self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x
        self.rect.y = player.rect.y
        self.origin_image = self.image
        self.angle = 0

    #Défintion pour faire tourner l'image en rond
    def rotate(self):
        self.angle += 12
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center = self.rect.center)

    #Définition pour supprimer la flèche
    def remove(self):
        self.player.all_projectiles.remove(self)

    #Définition pour que la flèche bouge avec ces conditions
    def move(self):
        self.rect.x += self.velocity
        #self.rotate()
        for slime in self.player.game.check_collision(self, self.player.game.all_mob):
            slime.damage(self.player.attack)
            self.remove()

        if self.rect.x > 1296:
            self.remove()

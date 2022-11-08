"""Class Slime du jeu Redem mode PVE en python."""

import pygame
import random
import animation

#classe des mobs
class Mob(animation.AnimateSprite):

    def __init__(self, game, name, anim, offset = 0, posx = 0, posy = 0, largeur = 5, size = (200, 200)):
        super().__init__(name, size)
        self.game = game
        self.health = 30
        self.max_health = 30
        self.attack = 0.3
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 210 + offset
        self.posx = posx
        self.posy = posy
        self.anim = anim
        self.largeur = largeur
        self.loot_amount = 10
        self.start_animation()

    #Définition pour définir la vitesse du mob
    def set_speed(self,speed):
        self.default_speed = speed
        self.velocity = random.randint(1, speed)


    #Définition pour les dégâts que le mob prend
    def set_loot_amount(self, amount):
        self.loot_amount = amount

    #Définition pour activer l'animation
    def update_animation(self):
        self.animate(speed = self.anim, loop = True)

    #Définition pour mettre à jour la barre de vie
    def update_health_bar(self, surface):
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + self.posx, self.rect.y + self.posy, self.max_health, self.largeur])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + self.posx, self.rect.y + self.posy, self.health, self.largeur])

    #Définition pour infliger des dégâts au mob et le faire respawn si sa vie atteint 0
    def damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.rect.x = 1000 + random.randint(0, 300)
            self.velocity = random.randint(1, self.default_speed)
            self.health = self.max_health
            self.game.add_score(self.loot_amount)

    #Défintion pour que le mob se déplace
    def forward(self):
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        else:
            self.game.player.damage(self.attack)

#Classe du slime qui prend les mêmes caractéristique que la classe mob
class Slime(Mob):
    def __init__(self, game):
        super().__init__(game, "iOOF6t-", 0.3, 130, 95, 130, 5, (230, 230))
        self.set_speed(2)

#Classe du boss qui prend les mêmes caractéristique que la classe mob
class Mini(Mob):
    def __init__(self, game):
        super().__init__(game, "BOSS-BLEU-EP22-", 0.5, 160, 30, 30, 7)
        self.health = 150
        self.max_health = 150
        self.attack = 0.8
        self.set_speed(1)
        self.set_loot_amount(50)
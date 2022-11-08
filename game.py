"""Class Game du jeu Redem mode PVE en python."""
import animation
from player import Player
from slime import Slime, Mini
from menu import Menu
import pygame
import animation
from sounds import SoundManager

#Classe du jeu qui est le coeur principal du programme
class Game:

    #Rappeler toutes les fonctions qu'on a besoin pour le jeu
    def __init__(self):
        self.is_playing = False
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        self.all_mob = pygame.sprite.Group()
        self.all_menu = pygame.sprite.Group()
        self.sound_manager = SoundManager()
        self.font = pygame.font.SysFont("monospace", 16)
        self.score = 0
        self.pressed = {}

    #Définition pour valider le commencement du jeu et faire spawn un slime et un boss
    def start(self):
        self.is_playing = True
        self.spawn_mob(Slime)
        self.spawn_mob(Mini)

    #Définition pour l'ajout d'un score
    def add_score(self, points = 10):
        self.score += points

    #Définition pour le game over donc recommencer le jeu
    def game_over(self):
        self.all_mob = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False
        self.score = 0

    #Définition pour faire apparaître le menu
    def update_menu(self, screen):
        for menu in self.all_menu:
            menu.update_animation_menu()
        self.all_menu.draw(screen)

    #Définition qui met à jour le jeu tout le temps
    def update(self, screen):
        #font = pygame.font.Font("Assets/   .ttf", 25)
        #Afficher le score
        score_text = self.font.render(f"Score : {self.score}", 1, (0, 0, 0))
        screen.blit(score_text, (20, 20))
        screen.blit(self.player.image, self.player.rect)
        #Afficher la barre de vie
        self.player.update_health_bar(screen)
        self.player.update_animation()
        #Pour supprimer un projectile
        for projectile in self.player.all_projectiles:
            projectile.move()

        #Pour ajouter toutes les fonctions du slime et du boss
        for slime in self.all_mob:
            slime.forward()
            slime.update_health_bar(screen)
            slime.update_animation()

        self.player.all_projectiles.draw(screen)
        self.all_mob.draw(screen)

        #Commande pour faire bouger le joueur vers la droite
        if self.pressed.get(pygame.K_d) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()

        #Commande pour faire bouger le joueur vers la gauche
        elif self.pressed.get(pygame.K_q) and self.player.rect.x > -30:
            self.player.move_left()

    #Définition pour vérifier si il y a une collision
    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    #Définition pour faire spawn les mobs
    def spawn_mob(self, mob_class_name):
        self.all_mob.add(mob_class_name.__call__(self))

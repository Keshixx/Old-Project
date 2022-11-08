"""
Mode de jeu PVE de Redem en poo avec Pygame créé par Kevin Espiguinha et Thibaut Bise en 2021.
Jeu de survie, il ne faut pas mourir par les mobs !
Jeu dans lequel où l'on incarne le personnage Redem qui affronte des créatures.
N'oubliez pas d'installer pygame (pip install pygame).
Mettre la commande entre parenthèses dans le terminal pour faire fonctionner le jeu.
Script Python
Fichiers : main.py, game.py, player.py, animations.py, projectile.py, sounds.py, slime.py, menu.py
"""

import pygame
from game import Game

pygame.init()

#Gestion de fps
clock = pygame.time.Clock()
FPS = 60

#Définition pour l'affichage
pygame.display.set_caption("Adventurer")
screen = pygame.display.set_mode((580, 326))
icon = pygame.image.load("Assets/Icon/Icon2.png").convert_alpha()
pygame.display.set_icon(icon)
background = pygame.image.load('Assets/Background/Background3.png')
banner = pygame.image.load('Assets/Start/ls-44.png')
play_button = pygame.image.load('Assets/Start/bouton.png')
play_button_rect = play_button.get_rect()

game = Game()
running = True

#Lancement du jeu avec un menu (class menu) et la class game
while running:
    if game.is_playing:
        screen = pygame.display.set_mode((1296, 598))
        screen.blit(background, (0, 0))
        game.update(screen)
    else:
        screen = pygame.display.set_mode((580, 326))
        #game.spawn_menu()
        #game.update_menu(screen)
        screen.blit(banner, (0, 0))
        screen.blit(play_button, (0, 0))
        pygame.mixer.pause()

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")

        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            #Si le joueur appuie sur espace alors le personnage lancera un projectile ici une flèche
            if event.key == pygame.K_SPACE:
                if game.is_playing:
                    game.player.launch_projectile()
                #Quand le jeu se lancera alors une musique se lancera aussi
                else:
                    game.start()
                    game.sound_manager.boucle('music')
                    game.sound_manager.volume('music')

        #Commande pour que le joueur clique sur le bouton qu'il l'envoie directement sur le jeu en lançant la musique
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_button_rect.collidepoint(event.pos):
                game.start()
                game.sound_manager.boucle('music')

    #commande pour mettre 60 images par seconde
    clock.tick(FPS)


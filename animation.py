"""Class AnimateSprite du jeu Redem mode PVE en python."""

import pygame

#Classe pour faire animer les personnages
class AnimateSprite(pygame.sprite.Sprite):

    def __init__(self, sprite_name, size = (200, 200)):
        super().__init__()
        self.size = size
        self.image = pygame.image.load(f'Assets/{sprite_name}.png')
        self.image = pygame.transform.scale(self.image, size)
        self.current_image = 0
        self.images = animations.get(sprite_name)
        self.animation = False

    # Définition pour commencer l'animation
    def start_animation(self):
        self.animation = True

    # Définition de l'enchainement d'image
    def animate(self, speed, loop=False):
        if self.animation:
            self.current_image += speed
            if self.current_image >= len(self.images):
                self.current_image = 0
                if loop is False:
                    self.animation = False
            self.image = self.images[int(self.current_image)]
            self.image = pygame.transform.scale(self.image, self.size)

    # Définition d'un menu
    def animate_menu(self):
        self.current_image += 1
        self.image = self.images[self.current_image]

#Définition du chargement des images
def load_animation_images(sprite_name):
    images = []
    path = f"Assets/{sprite_name}/{sprite_name}"

    for num in range(0, 3):
        image_path = path + str(num) + '.png'
        images.append(pygame.image.load(image_path))

    return images

def load_animation_8(sprite_name):
    images = []
    path = f"Assets/{sprite_name}/{sprite_name}"

    for num in range(0, 8):
        image_path = path + str(num) + '.png'
        images.append(pygame.image.load(image_path))

    return images

def load_animation_14(sprite_name):
    images = []
    path = f"Assets/{sprite_name}/{sprite_name}"

    for num in range(0, 14):
        image_path = path + str(num) + '.png'
        images.append(pygame.image.load(image_path))

    return images

def load_animation_31(sprite_name):
    images = []
    path = f"Assets/{sprite_name}/{sprite_name}"

    for num in range(0, 31):
        image_path = path + str(num) + '.png'
        images.append(pygame.image.load(image_path))

    return images

def load_animation_menu(sprite_name):
    images = []
    path = f"Assets/{sprite_name}/{sprite_name}"

    for num in range(0, 50):
        image_path = path + str(num) + '.png'
        images.append(pygame.image.load(image_path))

    return images

#Dictionnaire pour les images
animations = {
    'FKh0pz': load_animation_images('FKh0pz'),
    'ls-': load_animation_menu('ls-'),
    'Ggdqc3-': load_animation_8('Ggdqc3-'),
    'BOSS-BLEU-EP22-': load_animation_31('BOSS-BLEU-EP22-'),
    'iOOF6t-': load_animation_images('iOOF6t-')
}
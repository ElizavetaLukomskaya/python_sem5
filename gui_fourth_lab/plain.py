import random
import pygame
from os import path
import datetime

img_dir = path.join(path.dirname(__file__), 'img')
snd_dir = path.join(path.dirname(__file__), 'snd')

WIDTH = 1400
HEIGHT = 780
FPS = 60
POWERUP_TIME = 3500

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

clock = pygame.time.Clock()



def position(x, y, z, plain):
    start = (plain.rect.left + 30, plain.rect.top +30)

    x1 = start[0] + 60*x
    y1 = start[1] + 60*y

    if z == 0:
        x1 -= 15
        y1 -= 15
    elif z==1:
        x1+=15
        y1-=15
    elif z==2:
        x1-=15
        y1+=15
    elif z==3:
        x1+=15
        y1+=15

    return [x1,y1]


class Plain(pygame.sprite.Sprite):
    def __init__(self, x, y):
        # x_max = 19, y_max = 12
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("transparant.png")
        self.image = pygame.transform.scale(self.image, (60*x, 60*y))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2-100, HEIGHT/2)

    def update(self):
        pass

class Animal(pygame.sprite.Sprite):
    def __init__(self, x, y, z, type, plain, sex='Male'):
        self.is_animating = False
        self.sprites = []
        self.current_sprite = 0
        self.image = pygame.image.load("plant.png")


        if type == 'p':
            pygame.sprite.Sprite.__init__(self)
            self.sprites.append(self.image)
            self.image = pygame.transform.scale(self.image, (30, 30))
            self.rect = self.image.get_rect()



        if type == 'r':
            pygame.sprite.Sprite.__init__(self)
            self.rabbit = []
            if sex == 'Male':
                for i in range(116):
                    self.rabbit.append(pygame.image.load(f'r/male/Слой {i+1}.png'))
                self.image = pygame.transform.scale(self.image, (30, 30))
                self.rect = self.image.get_rect()

                self.sprites = self.rabbit
                self.image = self.sprites[self.current_sprite]


            if sex == 'Female':
                for i in range(117):
                    self.rabbit.append(pygame.image.load(f'r/female/Слой {i+1}.png'))
                self.image = pygame.transform.scale(self.image, (30, 30))
                self.rect = self.image.get_rect()

                self.sprites = self.rabbit
                self.image = self.sprites[self.current_sprite]


        if type == 's':
            pygame.sprite.Sprite.__init__(self)
            self.squirrel = []
            if sex == 'Male':
                for i in range(107):
                    self.squirrel.append(pygame.image.load(f's/male/Слой {i + 1}.png'))
                self.image = pygame.transform.scale(self.image, (30, 30))
                self.rect = self.image.get_rect()

                self.sprites = self.squirrel
                self.image = self.sprites[self.current_sprite]

            if sex == 'Female':
                for i in range(99):
                    self.squirrel.append(pygame.image.load(f's/female/Слой {i + 1}.png'))
                self.image = pygame.transform.scale(self.image, (30, 30))
                self.rect = self.image.get_rect()

                self.sprites = self.squirrel
                self.image = self.sprites[self.current_sprite]

        if type == 'w':
            pygame.sprite.Sprite.__init__(self)
            self.wolf = []
            if sex == 'Male':
                for i in range(35):
                    self.wolf.append(pygame.image.load(f'w/male/Слой {i + 1}.png'))
                self.image = pygame.transform.scale(self.image, (30, 30))
                self.rect = self.image.get_rect()

                self.sprites = self.wolf
                self.image = self.sprites[self.current_sprite]

            if sex == 'Female':
                for i in range(65):
                    self.wolf.append(pygame.image.load(f'w/female/Слой {i + 1}.png'))
                self.image = pygame.transform.scale(self.image, (30, 30))
                self.rect = self.image.get_rect()

                self.sprites = self.wolf
                self.image = self.sprites[self.current_sprite]

        if type == 'd':
            pygame.sprite.Sprite.__init__(self)
            self.deer = []
            if sex == 'Male':
                for i in range(60):
                    self.deer.append(pygame.image.load(f'd/male/Слой {i + 1}.png'))
                self.image = pygame.transform.scale(self.image, (30, 30))
                self.rect = self.image.get_rect()

                self.sprites = self.deer
                self.image = self.sprites[self.current_sprite]

            if sex == 'Female':
                for i in range(76):
                    self.deer.append(pygame.image.load(f'd/female/Слой {i + 1}.png'))
                self.image = pygame.transform.scale(self.image, (30, 30))
                self.rect = self.image.get_rect()

                self.sprites = self.deer
                self.image = self.sprites[self.current_sprite]

        if type == 'b':
            pygame.sprite.Sprite.__init__(self)
            self.bear = []
            if sex == 'Male':
                for i in range(123):
                    self.bear.append(pygame.image.load(f'b/male/Слой {i + 1}.png'))
                self.image = pygame.transform.scale(self.image, (30, 30))
                self.rect = self.image.get_rect()

                self.sprites = self.bear
                self.image = self.sprites[self.current_sprite]

            if sex == 'Female':
                for i in range(122):
                    self.bear.append(pygame.image.load(f'b/female/Слой {i + 1}.png'))
                self.image = pygame.transform.scale(self.image, (30, 30))
                self.rect = self.image.get_rect()

                self.sprites = self.bear
                self.image = self.sprites[self.current_sprite]

        self.x, self.y = position(x,y,z,plain)
        self.rect.center = (self.x, self.y)

    def animate(self):
        self.is_animating = True

    def update(self):
        if self.is_animating:
            clock.tick(200)
            self.current_sprite += 1

            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False

            self.image = self.sprites[self.current_sprite]
            self.image = pygame.transform.scale(self.image, (30, 30))




import pygame
import math
import toolbox
from score_manager import ScoreManager, Background
import image_util
import random, power


class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, target):
        super().__init__(self.containers)
        self.screen = screen
        self.target = target
        self.x = x
        self.y = y

        self.normalImage = pygame.image.load(image_util.getImage("Walker.png")).convert_alpha()
        self.hurtImage = pygame.image.load(image_util.getImage("Walker_hurt.png")).convert_alpha()
        self.image = self.normalImage
        self.rect = self.image.get_rect()
        self.rect.center = [self.x, self.y]

        self.angle = 180
        self.speed = 5
        self.max_health = 50
        self.health = self.max_health
        self.damage = 10
        self.hurtTimer = 0

        self.reset_offset = 0
        self.offset_x = random.randrange(-350, 350)
        self.offset_y = random.randrange(-350, 350)

    def update(self, projectiles, powers):
        self.angle = toolbox.angleBetweenPoints(self.x, self.y, self.target.x, self.target.y)
        angle_rads = math.radians(self.angle)
        
        self.x_move = (math.cos(angle_rads) / 5) * self.speed
        self.y_move = -(math.sin(angle_rads) / 5) * self.speed
        # self.x += self.x_move
        # self.y += self.y_moves
        self.rect.center = [self.x - Background.display_scroll[0], self.y - Background.display_scroll[1]]
        self.image = self.normalImage


        if self.reset_offset == 0:
            self.offset_x = random.randrange(-350, 350)
            self.offset_y = random.randrange(-350, 350)
            self.reset_offset = random.randrange(130, 150)
        else:
            self.reset_offset -= 1

        if self.target.x + self.offset_x > self.x - Background.display_scroll[0]:
            self.x += 1
        elif self.target.x + self.offset_x < self.x - Background.display_scroll[0]:
            self.x -= 1

        if self.target.y + self.offset_y > self.y - Background.display_scroll[1]:
            self.y += 1
        elif self.target.y + self.offset_y < self.y - Background.display_scroll[1]:
            self.y -= 1

        for projectile in projectiles:
            if self.rect.colliderect(projectile.rect):
                self.getHit(projectile.damage)
                projectile.explode()

        if self.hurtTimer <= 0:
            imageToRotate = self.image
        else:
            imageToRotate = self.hurtImage
            self.hurtTimer -= 1

        image_to_draw, image_rect = toolbox.getRotatedImage(imageToRotate, self.rect, self.angle)
        self.screen.blit(image_to_draw, image_rect)

    def getHit(self, damage):
        if damage:
            toolbox.playSound('hit.wav')
            self.hurtTimer = 5
        self.x -= self.x_move * 10
        self.y -= self.y_move * 10
        self.health -= damage
        if self.health <= 0:
            self.kill()

            if random.random() > .75:
                power.PowerUp(self.screen, [self.x, self.y])

            toolbox.playSound('point.wav')
            ScoreManager.score += int(self.max_health/5)


class Brute(Enemy):
    def __init__(self, screen, x, y, target):
        super().__init__(screen, x, y, target)
        self.normalImage = pygame.image.load(image_util.getImage("Brute.png")).convert_alpha()
        self.hurtImage = pygame.image.load(image_util.getImage("Brute_hurt.png")).convert_alpha()
        self.image = self.normalImage
        self.speed = 2
        self.max_health = 100
        self.health = self.max_health


class Crawler(Enemy):
    def __init__(self, screen, x, y, target):
        super().__init__(screen, x, y, target)
        self.hurtImage = pygame.image.load(image_util.getImage("Crawler_hurt.png")).convert_alpha()
        self.normalImage = self.normalImage
        self.normalImage = pygame.image.load(image_util.getImage("Crawler.png")).convert_alpha()
        self.speed = 1.5
        self.max_health = 75
        self.health = self.max_health
        self.angle = 90


class Helicopter(Enemy):
    def __init__(self, screen, x, y, target):
        super().__init__(screen, x, y, target)
        self.hurtImage = pygame.image.load(image_util.getImage("helicopter_hurt.png")).convert_alpha()
        self.normalImage = pygame.image.load(image_util.getImage("helicopter.png")).convert_alpha()
        self.normalImage = pygame.transform.scale(self.normalImage, (40, 40))
        self.normalImage = self.normalImage
        self.speed = 3
        self.max_health = 80
        self.health = self.max_health


class Spider(Enemy):
    def __init__(self, screen, x, y, target):
        super().__init__(screen, x, y, target)
        self.hurtImage = pygame.image.load(image_util.getImage("Spider_hurt.png")).convert_alpha()
        self.image = pygame.image.load(image_util.getImage("Spider.png")).convert_alpha()
        self.speed = 10
        self.max_health = 45
        self.health = self.max_health


class Runner(Enemy):
    def __init__(self, screen, x, y, target):
        super().__init__(screen, x, y, target)
        self.hurtImage = pygame.image.load(image_util.getImage("Runner_hurt.png"))
        self.image = pygame.image.load(image_util.getImage("Runner.png"))
        self.speed = 100
        self.max_health = 15
        self.health = self.max_health


class Motorcycle(Enemy):
    def __init__(self, screen, x, y, target):
        super().__init__(screen, x, y, target)
        self.hurtImage = pygame.image.load(image_util.getImage("Motorcycle_hurt.png"))
        self.image = pygame.image.load(image_util.getImage("Motorcycle.png"))
        self.speed = 15
        self.max_health = 45
        self.health = self.max_health

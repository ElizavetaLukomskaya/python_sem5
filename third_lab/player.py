import pygame, pygame.gfxdraw
import toolbox
import projectile
import image_util

class Player(pygame.sprite.Sprite):
    def __init__(self, screen, x, y):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.screen = screen
        self.x = x
        self.y = y

        self.image = pygame.image.load(image_util.getImage("Main_Character.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

        self.start_speed = 3
        self.speed = self.start_speed

        self.angle = 0
        self.shoot_cooldown = 0
        self.shoot_cooldown_max = 30
        self.start_shoot_cd = self.shoot_cooldown_max

        self.hurtTimer = 0
        self.alive = True

        self.health_max = 200
        self.health = self.health_max


    def update(self, enemies, powers):
        self.rect.center = (self.x, self.y)


        for enemy in enemies:
            if self.rect.colliderect(enemy.rect):
                enemy.getHit(0)
                self.getHit(enemy.damage)

        for power in powers:
            if self.rect.colliderect(power.rect):
                power.hide()

                if power.type == 'health_point':
                    power.regen_hp(self)
                if power.type == 'reload':
                    power.up_reload(self, False)
                    power.r_flag = True
                if power.type == 'speed':
                    power.up_speed(self, True)
                    power.s_flag = True


        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1

        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.angle = toolbox.angleBetweenPoints(self.x, self.y, mouse_x, mouse_y)

        image_to_draw, image_rect = toolbox.getRotatedImage(self.image, self.rect, self.angle)
        self.screen.blit(image_to_draw, image_rect)


        pygame.gfxdraw.arc(self.screen, int(self.x), int(self.y), 26, 0, 359, (255, 255, 255, 150))
        pygame.gfxdraw.arc(self.screen, int(self.x), int(self.y), 25, 0, 359, (255, 255, 255, 150))
        pygame.gfxdraw.arc(self.screen, int(self.x), int(self.y), 24, 0, 359, (255, 255, 255, 150))
        pygame.gfxdraw.arc(self.screen, int(self.x), int(self.y), 23, 0, 359, (255, 255, 255, 150))

        health_percentage = int(self.health / self.health_max * 359)

        pygame.gfxdraw.arc(self.screen, int(self.x), int(self.y), 26, 0, health_percentage, (0, 0, 255, 180))
        pygame.gfxdraw.arc(self.screen, int(self.x), int(self.y), 25, 0, health_percentage, (0, 0, 255, 180))
        pygame.gfxdraw.arc(self.screen, int(self.x), int(self.y), 24, 0, health_percentage, (0, 0, 255, 180))
        pygame.gfxdraw.arc(self.screen, int(self.x), int(self.y), 23, 0, health_percentage, (0, 0, 255, 180))


    def move (self, x_movement, y_movement):
        self.x += self.speed * x_movement
        self.y += self.speed * y_movement

    def shoot(self):
        if self.shoot_cooldown <= 0:
            self.shoot_cooldown = self.shoot_cooldown_max
            projectile.Bullet(self.screen, self.x, self.y, self.angle)

    def getHit(self, damage):
        self.hurtTimer = 5
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            self.alive = False

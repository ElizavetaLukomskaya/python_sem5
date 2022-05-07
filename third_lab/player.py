import pygame
import pygame.gfxdraw
import toolbox
import image_util
import weapon


class Player(pygame.sprite.Sprite):
    def __init__(self, screen, x, y):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.screen = screen
        self.x = x
        self.y = y

        self.start_speed = 4
        self.speed = self.start_speed

        self.angle = 0

        self.hurtTimer = 0
        self.alive = True

        self.health_max = 200
        self.health = self.health_max

        self.weapons = [weapon.Weapon('gun', 25, 1, 1, 17, 7, 'Main_Character.png', 'gun_shot.mp3'), weapon.Weapon('shotgun', 40, 5, 250, 6, 6, 'Main_Rocket.png', 'shotgun_shot.mp3'), weapon.Weapon('machine', 6, 60, 300, 3, 9, 'Main_AR.png', 'machine_shot.mp3'), weapon.Weapon('snipe', 70, 15, 375, 50, 12, 'Main_HeavySniper.png', 'snipe_shot.mp3')]

        self.player_weapon = self.weapons[0]

        self.image = pygame.image.load(image_util.getImage(self.player_weapon.image)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def update(self, enemies, powers):
        self.rect.center = (self.x, self.y)

        for enemy in enemies:
            if self.rect.colliderect(enemy.rect):
                if enemy.alive:
                    enemy.get_hit(0)
                    self.get_hit(enemy.damage)

        for power in powers:
            if self.rect.colliderect(power.rect):
                power.hide()

                if power.type == 'health_point':
                    power.regen_hp(self)
                if power.type == 'shoot':
                    power.up_shoot(self, False)
                    power.sh_flag = True
                if power.type == 'speed':
                    power.up_speed(self, True)
                    power.s_flag = True
                if power.type == 'reload':
                    power.up_reload(self, False)
                    power.r_flag = True


        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.angle = toolbox.angleBetweenPoints(self.x, self.y, mouse_x, mouse_y)

        if self.player_weapon.shoot_cooldown > 0:
            self.player_weapon.shoot_cooldown -= 1

        # self.reload_weapon(mouse_x, mouse_y)

        self.player_weapon.draw_ammo(mouse_x, mouse_y)

        image_to_draw, image_rect = toolbox.getRotatedImage(self.image, self.rect, self.angle)
        self.screen.blit(image_to_draw, image_rect)

        if self.x <= 25:
            self.x = 25
        if self.y <= 25:
            self.y = 25
        if self.y >= 575:
            self.y = 575
        if self.x >= 775:
            self.x = 775

        self.draw_hp()

    def draw_hp(self):
        pygame.gfxdraw.arc(self.screen, int(self.x), int(self.y), 26, -90, 269, (255, 255, 255, 75))
        pygame.gfxdraw.arc(self.screen, int(self.x), int(self.y), 25, -90, 269, (255, 255, 255, 75))
        pygame.gfxdraw.arc(self.screen, int(self.x), int(self.y), 24, -90, 269, (255, 255, 255, 75))
        pygame.gfxdraw.arc(self.screen, int(self.x), int(self.y), 23, -90, 269, (255, 255, 255, 75))

        health_percentage = int(self.health / self.health_max * 359)

        pygame.gfxdraw.arc(self.screen, int(self.x), int(self.y), 26, -90, health_percentage - 90, (255, 250, 0, 200))
        pygame.gfxdraw.arc(self.screen, int(self.x), int(self.y), 25, -90, health_percentage - 90, (255, 250, 0, 200))
        pygame.gfxdraw.arc(self.screen, int(self.x), int(self.y), 24, -90, health_percentage - 90, (255, 250, 0, 200))
        pygame.gfxdraw.arc(self.screen, int(self.x), int(self.y), 23, -90, health_percentage - 90, (255, 250, 0, 200))


    def move(self, x_movement, y_movement):
        self.x += self.speed * x_movement
        self.y += self.speed * y_movement



    def shoot(self):
        if self.player_weapon.shoot_cooldown <= 0:
            self.player_weapon.shoot_cooldown = self.player_weapon.shoot_cooldown_max
            self.player_weapon.shoot(self)

    def change_weapon(self, key):
        self.image = pygame.image.load(image_util.getImage(self.player_weapon.image)).convert_alpha()

        self.player_weapon = self.weapons[key]
        if self.weapons[key].ammo_count == 0 and self.weapons[key].reload_cooldown > 0:
            self.weapons[key].reload_cooldown = 0

    def reload_weapon(self, mouse_x, mouse_y):
       # if self.player_weapon.ammo_count == 0:
        if self.player_weapon.type != 'gun':
            self.player_weapon.reload_cooldown += 1
            self.player_weapon.draw_reload(self.screen, mouse_x, mouse_y)

            if self.player_weapon.reload_cooldown == self.player_weapon.reload_cooldown_max:
                self.player_weapon.reload()
                self.player_weapon.reload_cooldown = 0

            if self.player_weapon.reload_cooldown % 60 == 0:
                toolbox.playSound(self.player_weapon.reload_sound)


    def get_hit(self, damage):
        self.hurtTimer = 5
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            self.alive = False

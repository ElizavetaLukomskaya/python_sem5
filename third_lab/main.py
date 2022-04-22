import pygame.gfxdraw

import enemy
import image_util
from player import Player
from power import PowerUp
from projectile import Bullet
from score_manager import ScoreManager, Background
from wave_controller import WaveController

WIDTH = 1000
HEIGHT = 600
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Crimsoland")
clock = pygame.time.Clock()

background_image = pygame.image.load(image_util.getImage("landscape.png")).convert()

playerGroup = pygame.sprite.Group()
projectilesGroup = pygame.sprite.Group()
enemiesGroup = pygame.sprite.Group()
powerGroup = pygame.sprite.Group()

Player.containers = playerGroup
Bullet.containers = projectilesGroup
enemy.Enemy.containers = enemiesGroup
PowerUp.containers = powerGroup


mr_player = Player(screen, WIDTH/2, HEIGHT/2)
wave_controller = WaveController(screen, WIDTH, HEIGHT, enemiesGroup)

pygame.mixer.music.load(image_util.getImage('Main_Theme.wav'))
pygame.mixer.music.play(-1)

font = pygame.font.SysFont('Bodoni 72 Book', 60)
running = True

while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and keys[pygame.K_a]:
        Background.display_scroll[0] -= mr_player.speed / 1.4
        Background.display_scroll[1] -= mr_player.speed / 1.4
        for projectile in projectilesGroup:
            projectile.x += mr_player.speed / 1.4
            projectile.y += mr_player.speed / 1.4

    elif keys[pygame.K_w] and keys[pygame.K_d]:
        Background.display_scroll[0] += mr_player.speed / 1.4
        Background.display_scroll[1] -= mr_player.speed / 1.4
        for projectile in projectilesGroup:
            projectile.x -= mr_player.speed / 1.4
            projectile.y += mr_player.speed / 1.4

    elif keys[pygame.K_s] and keys[pygame.K_a]:
        Background.display_scroll[0] -= mr_player.speed / 1.4
        Background.display_scroll[1] += mr_player.speed / 1.4
        for projectile in projectilesGroup:
            projectile.x += mr_player.speed / 1.4
            projectile.y -= mr_player.speed / 1.4

    elif keys[pygame.K_s] and keys[pygame.K_d]:
        Background.display_scroll[0] += mr_player.speed / 1.4
        Background.display_scroll[1] += mr_player.speed / 1.4
        for projectile in projectilesGroup:
            projectile.x -= mr_player.speed / 1.4
            projectile.y -=mr_player.speed / 1.4

    elif keys[pygame.K_d]:
        Background.display_scroll[0] += mr_player.speed
        for projectile in projectilesGroup:
            projectile.x -= mr_player.speed
        # for power in powerGroup:
        #     power.rect.center[0] -= mr_player.speed

    elif keys[pygame.K_a]:
        Background.display_scroll[0] -= mr_player.speed
        for projectile in projectilesGroup:
            projectile.x += mr_player.speed
        # for power in powerGroup:
        #     power.rect.center[0] += mr_player.speed

    elif keys[pygame.K_w]:
        Background.display_scroll[1] -= mr_player.speed
        for projectile in projectilesGroup:
            projectile.y += mr_player.speed
        # for power in powerGroup:
        #     power.rect.center[1] += mr_player.speed

    elif keys[pygame.K_s]:
        Background.display_scroll[1] += mr_player.speed
        for projectile in projectilesGroup:
            projectile.y -= mr_player.speed
        # for power in powerGroup:
        #     power.rect.center[1] -= mr_player.speed


    if pygame.mouse.get_pressed()[0]:
        mr_player.shoot()

    if keys[pygame.K_SPACE]:
        if not waveComing:
            waveComing = True
            wave_controller.new_wave(mr_player)

    screen.blit(background_image, (0 - Background.display_scroll[0], 0 - Background.display_scroll[1]))

    mr_player.update(enemiesGroup, powerGroup)
    for projectile in projectilesGroup:
        projectile.update()

    for enemy in enemiesGroup:
        enemy.update(projectilesGroup, powerGroup)
    if not enemiesGroup.sprites():
        waveComing = False

    for power in powerGroup:
        power.update(mr_player)

    if  not mr_player.alive:
        running = False

    score_text = font.render("Score: " + str(ScoreManager.score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    wave_text = font.render("Wave: " + str(wave_controller.wave_number), True, (255, 255, 255))
    screen.blit(wave_text, (800, 10))

    pygame.display.flip()


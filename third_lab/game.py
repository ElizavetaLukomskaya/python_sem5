import pygame.gfxdraw
import enemy
import image_util
from player import Player
from power import PowerUp
from projectile import Bullet
from wave_controller import WaveController

WIDTH = 800
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

background_image = pygame.image.load(image_util.getImage("land.png")).convert()

playerGroup = pygame.sprite.Group()
projectilesGroup = pygame.sprite.Group()
enemiesGroup = pygame.sprite.Group()
powerGroup = pygame.sprite.Group()

Player.containers = playerGroup
Bullet.containers = projectilesGroup
enemy.Enemy.containers = enemiesGroup
PowerUp.containers = powerGroup

mr_player = Player(screen, WIDTH / 2, HEIGHT / 2)
wave_controller = WaveController(screen, WIDTH, HEIGHT, enemiesGroup)


font = pygame.font.SysFont('Bodoni 72 Book', 60)





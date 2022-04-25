import pygame.gfxdraw
from play_loop import play_loop
import enemy
import image_util
from player import Player
from power import PowerUp
from projectile import Bullet
from manager import ScoreManager, Background
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

mr_player = Player(screen, WIDTH / 2, HEIGHT / 2)
wave_controller = WaveController(screen, WIDTH, HEIGHT, enemiesGroup)

# pygame.mixer.music.load(image_util.getImage('Main_Theme.wav'))
# pygame.mixer.music.play(-1)

font = pygame.font.SysFont('Bodoni 72 Book', 60)

class Game:
    def start_game(self):
        play_loop(screen, clock, FPS, mr_player, projectilesGroup, enemiesGroup, powerGroup, wave_controller, font, background_image)





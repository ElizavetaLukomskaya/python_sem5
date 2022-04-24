import pygame.gfxdraw
import toolbox
import enemy
import image_util
from player import Player
from power import PowerUp
from projectile import Bullet
from score_manager import ScoreManager, Background
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


class Button:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.inact_clr = (15, 15, 15)

    def draw(self, x, y, message, action=None, font_size=30):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        print_text(message=message, x=x + 5, y=y + 5, font_clr=(255, 255, 255), font_size=font_size)
        if x < mouse[0] < x + self.width:
            if y < mouse[1] < y + self.height:
                pygame.draw.rect(screen, self.inact_clr, (x, y, self.width, self.height))
                print_text(message=message, x=x + 5, y=y + 5, font_clr=(123, 22, 12), font_size=font_size)
                if click[0] == 1:
                    toolbox.playSound('button.wav')
                    pygame.time.delay(300)
                    if action is not None:
                        if action == quit():
                            pygame.quit()
                            quit()
                        else:
                            action()

        else:
            pygame.draw.rect(screen, self.inact_clr, (x, y, self.width, self.height))
            print_text(message=message, x=x + 5, y=y + 5, font_clr=(255,255,255), font_size=font_size)



def print_text(message, x, y, font_clr = (0,0,0), font_type = 'RequestPersonalUse.otf', font_size = 30):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_clr)
    screen.blit(text, (x,y))

def pause():
    paused = True
    pause_bg = pygame.image.load(image_util.getImage('land.jpg'))
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.blit(pause_bg, (0,0))
        print_text('Paused! press ENTER to continue', 110, 280, font_clr=(WHITE), font_size=20)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            paused = False

        pygame.display.update()
        clock.tick(15)

def show_menu():
    menu_bg = pygame.image.load(image_util.getImage('crimsonland_menu.jpg'))

    menu = True

    menu_btn = Button(125, 25)

    pygame.mouse.set_visible(False)
    cursor_img = pygame.image.load(image_util.getImage('cursor.png'))
    cursor_rect = cursor_img.get_rect()

    pygame.mixer.music.load(image_util.getImage('menu.mp3'))
    pygame.mixer.music.play(-1)

    need_input = False
    input_text = ''

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if need_input and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    need_input = False
                    input_text = ''
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    if len(input_text) < 15:
                        input_text += event.unicode


        cursor_rect.topleft = pygame.mouse.get_pos()
        screen.blit(menu_bg, (0,0))
        menu_btn.draw(220, 213, 'Start game', None, 10)
        menu_btn.draw(203, 274, 'Rating', None, 10)
        menu_btn.draw(182, 333, 'About game', None, 10)
        menu_btn.draw(161, 394, 'Options', None, 10)
        menu_btn.draw(140, 453, 'Quit', quit, 10)
        screen.blit(cursor_img, cursor_rect)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_TAB]:
            need_input = True

        print_text(input_text, 100, 100)

        pygame.display.update()
        clock.tick(60)




background_image = pygame.image.load(image_util.getImage("land.jpg")).convert()

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


font = pygame.font.SysFont('Bodoni 72 Book', 60)
running = True

button = Button(100, 100)

show_menu()

pygame.mixer.music.load(image_util.getImage('Main_Theme.wav'))
pygame.mixer.music.play(-1)

while running:
    clock.tick(FPS)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
        #     running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        pause()

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
    screen.blit(wave_text, (600, 10))

    pygame.display.flip()


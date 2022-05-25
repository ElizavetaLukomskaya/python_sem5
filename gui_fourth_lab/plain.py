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

x_p = 0
y_p = 0
move_count = 0

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("LAB4")

start_bg = pygame.image.load("start.png")
start_bg = pygame.transform.scale(start_bg, (1400, 780))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

clock = pygame.time.Clock()

sound_library = {}

def playSound(name):
    global sound_library
    sound = sound_library.get(name)
    if sound == None:
        sound = pygame.mixer.Sound(name)
        sound_library[name] = sound
    sound.play()

def print_text(message, x, y, font_clr = (0,0,0), font_type = 'Fifaks10Dev1.ttf', font_size = 30):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_clr)
    screen.blit(text, (x,y))

class Button:
    def __init__(self, width, height, inact_clr=(0, 0, 0)):
        self.width = width
        self.height = height
        self.inact_clr = inact_clr

    def draw_menu(self, x, y, message, action=None, start='', font_size=30, b_font_clr=(255,255,255)):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        print_text(message=message, x=x + 5, y=y + 5, font_clr=b_font_clr, font_size=font_size)
        if x < mouse[0] < x + self.width:
            if y < mouse[1] < y + self.height:
                pygame.draw.rect(screen, self.inact_clr, (x, y, self.width, self.height))
                print_text(message=message, x=x + 5, y=y + 5, font_clr=(75, 80, 100), font_size=font_size)
                if click[0] == 1:
                    playSound('button.wav')
                    pygame.time.delay(300)
                    if start == 'start':
                        gaming()

                    if action is not None:
                        if action == quit():
                            pygame.quit()
                            quit()
                        else:
                            action()

        else:
            pygame.draw.rect(screen, self.inact_clr, (x, y, self.width, self.height))
            print_text(message=message, x=x + 5, y=y + 5, font_clr=b_font_clr, font_size=font_size)

    def draw_game(self, x, y, message, action=None, start='', font_size=30, b_font_clr=(255,255,255)):
        global move_count
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        pygame.draw.rect(screen, self.inact_clr, (x, y, self.width, self.height))
        print_text(message=message, x=x + 18, y=y + 45, font_clr=b_font_clr, font_size=font_size)
        if x < mouse[0] < x + self.width:
            if y < mouse[1] < y + self.height:
                pygame.draw.rect(screen, self.inact_clr, (x, y, self.width, self.height))
                print_text(message=message, x=x + 18, y=y + 45, font_clr=(164, 224, 194), font_size=font_size)
                if click[0] == 1:
                    playSound('button.wav')
                    pygame.time.delay(300)
                    if start == 'move':
                        move_count += 1

                    if start == 'quit':
                        pygame.quit()
                        quit()

                    if action is not None:
                        if action == quit():
                            pygame.quit()
                            quit()
                        else:
                            action()

        else:
            pygame.draw.rect(screen, self.inact_clr, (x, y, self.width, self.height))
            print_text(message=message, x=x + 18, y=y + 45, font_clr=b_font_clr, font_size=font_size)


need_input = False
input_text = '|'
input_tick = 50


def get_input(x, y):
    global need_input, input_text, input_tick

    input_rect = pygame.Rect(x, y, 255, 50)

    mouse = pygame.mouse.get_pos()

    pygame.draw.rect(screen, (255, 255, 255), input_rect)

    click = pygame.mouse.get_pressed()

    if input_rect.collidepoint(mouse[0], mouse[1]) and click[0]:
        need_input = True

    if need_input:
        for event in pygame.event.get():
            if need_input and event.type == pygame.KEYDOWN:
                input_text = input_text.replace('|', '')
                input_tick = 50

                if event.key == pygame.K_RETURN:
                    need_input = False
                    message = input_text
                    input_text = ''
                    return message
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    if len(input_text) < 3:
                        input_text += event.unicode

                input_text += '|'
    if len(input_text):
        print_text(message=input_text, x=input_rect.x + 2, y=input_rect.y + 2, font_size=55)
    input_tick -= 1

    if input_tick == 0:
        input_text = input_text[:-1]
    if input_tick == -50:
        input_text += '|'
        input_tick =50

    return None

def error():
    paused = True
    cong_bg = pygame.image.load('error.jpg')
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.blit(cong_bg, (0, 0))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            paused = False

        pygame.display.update()

def show_menu():
    global x_p, y_p
    menu = True

    start_btn = Button(400, 80)

    pygame.mouse.set_visible(False)
    cursor_img = pygame.image.load('cursor.png')
    cursor_rect = cursor_img.get_rect()

    pygame.mixer.music.load('menu.mp3')
    pygame.mixer.music.play(-1)

    got_name_x = False
    got_name_y = False

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        cursor_rect.topleft = pygame.mouse.get_pos()
        screen.blit(start_bg, (0,0))
        if not got_name_x:
            print_text('WIDTH: ', 510, 200, font_clr=(255,255,255), font_size=60)
            name = get_input(510, 255)
            if name:
                got_name_x = True
                x_p = int(name)
                if int(name) < 1 or int(name) > 19:
                    error()
                    got_name_x = False

        else:
            print_text(f'WIDTH: {x_p}', 510, 200, font_clr=(255, 255, 255), font_size=80)
            if not got_name_y:
                print_text('HEIGHT: ', 510, 300, font_clr=(255, 255, 255), font_size=60)
                name_y = get_input(510, 355)
                if name_y:
                    got_name_y = True
                    y_p = int(name_y)
                    if int(name_y) < 1 or int(name_y) > 12:
                        error()
                        got_name_y = False

            else:
                print_text(f'HEIGHT: {y_p}', 510, 300, font_clr=(255, 255, 255), font_size=80)
            



        start_btn.draw_menu(510, 530, 'START GAME', start='start', font_size=75)
        screen.blit(cursor_img, cursor_rect)

        pygame.display.update()
        # clock.tick(60)



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


class Fence(pygame.sprite.Sprite):
    def __init__(self, x, y, image: str):
        # x_max = 19, y_max = 12
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


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
            clock.tick(1000)
            self.current_sprite += 1

            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False

            self.image = self.sprites[self.current_sprite]
            self.image = pygame.transform.scale(self.image, (30, 30))


def gaming():
    global x_p, y_p, move_count
    bg = pygame.image.load("grass.png")
    bg = pygame.transform.scale(bg, (1700, 1200))

    move_btn = Button(150, 150, inact_clr=(70,175,137))
    save_btn = Button(150, 150, inact_clr=(70,175,137))
    exit_btn = Button(150, 150, inact_clr=(70,175,137))

    # clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()

    # max_x_for_plain = 19
    # max_y_dor_plain = 12

    pl = Plain(x_p, y_p)
    all_sprites.add(pl)

    x_left_curr = pl.rect.left - 15
    y_top_curr = pl.rect.top - 15
    y_bot_curr = pl.rect.bottom + 15

    for i in range(2 * (x_p + 2) - 2):
        f = Fence(x_left_curr, y_top_curr, 'fence.png')
        f1 = Fence(x_left_curr, y_bot_curr, 'fence.png')
        x_left_curr += 30
        all_sprites.add(f)
        all_sprites.add(f1)

    x_left_curr = pl.rect.left - 15
    x_right_curr = pl.rect.right + 15
    y_top_curr = pl.rect.top - 30

    for i in range(2 * (y_p + 2) - 2):
        f = Fence(x_left_curr, y_top_curr + 15, 'fence1.png')
        f1 = Fence(x_right_curr, y_top_curr + 15, 'fence1.png')
        y_top_curr += 30
        all_sprites.add(f)
        all_sprites.add(f1)

    an = []

    # max_x_for_animals = max_x_for_plain - 1
    # max_y_dor_animals = max_y_for_plain - 1

    an.append(Animal(0, 0, 0, 'p', pl))
    an.append(Animal(0, 1, 0, 'p', pl))
    an.append(Animal(0, 2, 0, 'p', pl))
    an.append(Animal(0, 3, 0, 'p', pl))
    an.append(Animal(0, 4, 0, 'p', pl))
    an.append(Animal(0, 5, 0, 'p', pl))

    an.append(Animal(0, 6, 0, 'p', pl))
    an.append(Animal(0, 7, 0, 'p', pl))
    an.append(Animal(0, 8, 0, 'p', pl))
    an.append(Animal(0, 9, 0, 'p', pl))
    an.append(Animal(0, 10, 0, 'p', pl))
    an.append(Animal(0, 11, 0, 'p', pl))

    an.append(Animal(2, 6, 3, 'r', pl))
    an.append(Animal(3, 7, 3, 'r', pl, sex='Female'))
    an.append(Animal(4, 6, 2, 's', pl))
    an.append(Animal(3, 10, 2, 's', pl, sex='Male'))
    an.append(Animal(5, 6, 2, 'w', pl))
    an.append(Animal(6, 10, 2, 'w', pl, sex='Female'))
    an.append(Animal(7, 6, 2, 'd', pl))
    an.append(Animal(8, 11, 2, 'd', pl, sex='Female'))
    an.append(Animal(9, 6, 2, 'b', pl))
    an.append(Animal(18, 11, 0, 'b', pl, sex='Female'))

    an.append(Animal(18, 0, 1, 'b', pl, sex='Female'))
    all_sprites.add(an)

    pygame.mouse.set_visible(False)
    cursor_img = pygame.image.load('cursor.png')
    cursor_rect = cursor_img.get_rect()

    running = True

    while running:
        clock.tick(60)
        screen.blit(bg, (0, 0))
        print_text("MOVE:", 1220, 15, font_clr=(255, 255, 255), font_size=75)
        print_text(str(move_count), 1220, 90, font_clr=(255, 255, 255), font_size=75)
        move_btn.draw_game(1220, 200, 'MOVE', start='move', font_size=60)
        save_btn.draw_game(1220, 400, 'SAVE', start='save', font_size=60)
        exit_btn.draw_game(1220, 600, 'EXIT', action='quit', font_size=60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        for i in range(len(an)):
            an[i].animate()

        all_sprites.update()

        all_sprites.draw(screen)


        cursor_rect.center = pygame.mouse.get_pos()
        screen.blit(cursor_img, cursor_rect)
        pygame.display.flip()


    pygame.quit()
    quit()




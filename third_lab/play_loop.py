import pygame.gfxdraw
import pygame, math
from manager import ScoreManager, Background
from menu import print_text, pause
import toolbox
from game import *


class Button:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.inact_clr = (15, 15, 15)

    def draw(self, x, y, message, action=None, start='', font_size=30):
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
                    if start == 'start':
                        play_loop(screen, clock, FPS, mr_player, projectilesGroup, enemiesGroup, powerGroup,
                                  wave_controller, font, background_image, True)
                    if action is not None:
                        if action == quit():
                            pygame.quit()
                            quit()
                        else:
                            action()

        else:
            pygame.draw.rect(screen, self.inact_clr, (x, y, self.width, self.height))
            print_text(message=message, x=x + 5, y=y + 5, font_clr=(255, 255, 255), font_size=font_size)


def show_menu():
    menu_bg = pygame.image.load(image_util.getImage('crimsonland_menu.jpg'))

    menu = True

    start_btn = Button(125, 25)
    rating_btn = Button(125, 25)
    info_btn = Button(125, 25)
    opt_btn = Button(125, 25)
    quit_btn = Button(125, 25)

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
        screen.blit(menu_bg, (0, 0))
        start_btn.draw(220, 213, 'Start game', start='start', font_size=10)
        rating_btn.draw(203, 274, 'Rating', action=None, font_size=10)
        info_btn.draw(182, 333, 'About game', action=None, font_size=10)
        opt_btn.draw(161, 394, 'Options', action=None, font_size=10)
        quit_btn.draw(140, 453, 'Quit', action=quit, font_size=10)
        screen.blit(cursor_img, cursor_rect)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_TAB]:
            need_input = True

        print_text(input_text, 100, 100)

        pygame.display.update()
        clock.tick(60)


def play_loop(screen, clock, FPS, mr_player, projectilesGroup, enemiesGroup, powerGroup, wave_controller, font,
              background_image, flag):
    pygame.mixer.music.load(image_util.getImage('Main_Theme.wav'))
    pygame.mixer.music.play(-1)

    pygame.mouse.set_visible(False)
    cursor_img = pygame.image.load(image_util.getImage('curs_white.png'))
    cursor_rect = cursor_img.get_rect()

    rw_flag = False

    running = flag
    while running:

        print(mr_player.x, mr_player.y, sep=' ')
        print(Background.display_scroll)
        clock.tick(FPS)

        screen.blit(background_image, (0 - Background.display_scroll[0], 0 - Background.display_scroll[1]))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause()


        keys = pygame.key.get_pressed()
        cursor_rect.center = pygame.mouse.get_pos()

        if 250 > Background.display_scroll[0] > - 250:

            if keys[pygame.K_d]:
                Background.display_scroll[0] += mr_player.speed
                for projectile in projectilesGroup:
                    projectile.x -= mr_player.speed

            elif keys[pygame.K_a]:
                Background.display_scroll[0] -= mr_player.speed
                for projectile in projectilesGroup:
                    projectile.x += mr_player.speed


        elif Background.display_scroll[0] >= 250:
            if keys[pygame.K_d]:
                mr_player.move(1,0)

            elif keys[pygame.K_a]:
                mr_player.move(-1,0)
                if mr_player.x <= 401 and Background.display_scroll[0] > 250:
                    Background.display_scroll[0] = 249


        elif Background.display_scroll[0] <= -250:
            if keys[pygame.K_d]:
                mr_player.move(1,0)
                if mr_player.x >= 399 and Background.display_scroll[0] < -250:
                    Background.display_scroll[0] = -249

            elif keys[pygame.K_a]:
                mr_player.move(-1,0)

        if 200 > Background.display_scroll[1] > - 200:

            if keys[pygame.K_w]:
                Background.display_scroll[1] -= mr_player.speed
                for projectile in projectilesGroup:
                    projectile.y += mr_player.speed

            elif keys[pygame.K_s]:
                Background.display_scroll[1] += mr_player.speed
                for projectile in projectilesGroup:
                    projectile.y -= mr_player.speed

        elif Background.display_scroll[1] >= 200:

            if keys[pygame.K_w]:
                mr_player.move(0, -1)
                if mr_player.y <= 301 and Background.display_scroll[1] >= 200:
                    Background.display_scroll[1] = 199
            elif keys[pygame.K_s]:
                mr_player.move(0, 1)

        elif Background.display_scroll[1] <= - 200:

            if keys[pygame.K_w]:
                mr_player.move(0, -1)
            elif keys[pygame.K_s]:
                mr_player.move(0, 1)
                if mr_player.y >= 299 and Background.display_scroll[1] <= -200:
                    Background.display_scroll[1] = -199





        # if 250 >= Background.display_scroll[0] >= -250 and 200 >= Background.display_scroll[1] >= -200:
        # # if Background.display_scroll[0] > -250 and Background.display_scroll[1] > -250:
        #     if keys[pygame.K_w] and keys[pygame.K_a]:
        #         Background.display_scroll[0] -= int(mr_player.speed / 1.4)
        #         Background.display_scroll[1] -= int(mr_player.speed / 1.4)
        #         for projectile in projectilesGroup:
        #             projectile.x += int(mr_player.speed / 1.4)
        #             projectile.y += int(mr_player.speed / 1.4)
        #
        #     # if Background.display_scroll[0] < 250 and Background.display_scroll[1] > -250:
        #     elif keys[pygame.K_w] and keys[pygame.K_d]:
        #         Background.display_scroll[0] += int(mr_player.speed / 1.4)
        #         Background.display_scroll[1] -= int(mr_player.speed / 1.4)
        #         for projectile in projectilesGroup:
        #             projectile.x -= int(mr_player.speed / 1.4)
        #             projectile.y += int(mr_player.speed / 1.4)
        #
        #     # if Background.display_scroll[0] > -250 and Background.display_scroll[1] < 250:
        #     elif keys[pygame.K_s] and keys[pygame.K_a]:
        #         Background.display_scroll[0] -= int(mr_player.speed / 1.4)
        #         Background.display_scroll[1] += int(mr_player.speed / 1.4)
        #         for projectile in projectilesGroup:
        #             projectile.x += int(mr_player.speed / 1.4)
        #             projectile.y -= int(mr_player.speed / 1.4)
        #
        #     # if Background.display_scroll[0] < 250 and Background.display_scroll[1] < 250:
        #     elif keys[pygame.K_s] and keys[pygame.K_d]:
        #         Background.display_scroll[0] += int(mr_player.speed / 1.4)
        #         Background.display_scroll[1] += int(mr_player.speed / 1.4)
        #         for projectile in projectilesGroup:
        #             projectile.x -= int(mr_player.speed / 1.4)
        #             projectile.y -= int(mr_player.speed / 1.4)
        #


        if pygame.mouse.get_pressed()[0]:
            mr_player.shoot()

        if keys[pygame.K_1]:
            mr_player.change_weapon(0)
        if keys[pygame.K_2]:
            if wave_controller.wave_number >=5:
                mr_player.change_weapon(1)
        if keys[pygame.K_3]:
            if wave_controller.wave_number >= 10:
                mr_player.change_weapon(2)
        if keys[pygame.K_4]:
            if wave_controller.wave_number >= 15:
                mr_player.change_weapon(3)


        if (keys[pygame.K_r] and mr_player.player_weapon.ammo_count_max > mr_player.player_weapon.ammo_count > 0) or mr_player.player_weapon.ammo_count == 0:
            mr_player.reload_weapon(cursor_rect.centerx, cursor_rect.centery)

        else:
            mr_player.player_weapon.reload_cooldown = 0



        if wave_controller.wave_number == 0:
            if keys[pygame.K_SPACE]:
                wave_controller.new_wave(mr_player)

        elif len(enemiesGroup.sprites()) <= 5:
            print_text(f"New Wave coming in", 280, 50, font_clr=(255, 255, 255), font_type='Qore.otf', font_size=17)
            wave_controller.draw_timer(screen, 400, 110)
            wave_controller.wave_cd += 1

            if keys[pygame.K_SPACE] or wave_controller.wave_cd == wave_controller.wave_cd_max or (
                    wave_controller.wave_cd < wave_controller.wave_cd_max and len(enemiesGroup.sprites()) == 0):
                if wave_controller.wave_cd < wave_controller.wave_cd_max:
                    ScoreManager.score += math.ceil((wave_controller.wave_cd_max - wave_controller.wave_cd)/30)

                wave_controller.new_wave(mr_player)


        mr_player.update(enemiesGroup, powerGroup)
        for projectile in projectilesGroup:
            projectile.update()


        for enemy in enemiesGroup:
            enemy.update(projectilesGroup, powerGroup)

        for power in powerGroup:
            power.update(mr_player)

        if not mr_player.alive:
            running = False

        print_text("Score: " + str(ScoreManager.score), 10, 10, font_clr=(255,255,255), font_type='Qore.otf')

        print_text("Wave: " + str(wave_controller.wave_number), 615, 10, font_clr=(255, 255, 255), font_type='Qore.otf')

        screen.blit(cursor_img, cursor_rect)
        pygame.display.flip()

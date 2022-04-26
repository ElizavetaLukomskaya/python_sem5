import pygame
import image_util
import toolbox
from game import screen, clock




def print_text(message, x, y, font_clr = (0,0,0), font_type = 'RequestPersonalUse.otf', font_size = 30):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_clr)
    screen.blit(text, (x,y))

def pause():
    paused = True
    pause_bg = pygame.image.load(image_util.getImage('land.png'))
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.blit(pause_bg, (0,0))
        print_text('Paused! press ENTER to continue', 110, 280, font_clr=(255, 255, 255), font_size=20)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            paused = False

        pygame.display.update()
        clock.tick(15)


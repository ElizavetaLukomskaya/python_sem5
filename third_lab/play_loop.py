import pygame.gfxdraw
import pygame
from manager import ScoreManager, Background


def play_loop(screen, clock, FPS, mr_player, projectilesGroup, enemiesGroup, powerGroup, wave_controller, font, background_image):
    running = True

    while running:

        print(Background.display_scroll)
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        keys = pygame.key.get_pressed()

        #if Background.display_scroll[0] > -250 and Background.display_scroll[1] > -250:
        if keys[pygame.K_w] and keys[pygame.K_a]:
            Background.display_scroll[0] -= mr_player.speed / 1.4
            Background.display_scroll[1] -= mr_player.speed / 1.4
            for projectile in projectilesGroup:
                projectile.x += mr_player.speed / 1.4
                projectile.y += mr_player.speed / 1.4

        #if Background.display_scroll[0] < 250 and Background.display_scroll[1] > -250:
        elif keys[pygame.K_w] and keys[pygame.K_d]:
            Background.display_scroll[0] += mr_player.speed / 1.4
            Background.display_scroll[1] -= mr_player.speed / 1.4
            for projectile in projectilesGroup:
                projectile.x -= mr_player.speed / 1.4
                projectile.y += mr_player.speed / 1.4

        #if Background.display_scroll[0] > -250 and Background.display_scroll[1] < 250:
        elif keys[pygame.K_s] and keys[pygame.K_a]:
            Background.display_scroll[0] -= mr_player.speed / 1.4
            Background.display_scroll[1] += mr_player.speed / 1.4
            for projectile in projectilesGroup:
                projectile.x += mr_player.speed / 1.4
                projectile.y -= mr_player.speed / 1.4

        #if Background.display_scroll[0] < 250 and Background.display_scroll[1] < 250:
        elif keys[pygame.K_s] and keys[pygame.K_d]:
            Background.display_scroll[0] += mr_player.speed / 1.4
            Background.display_scroll[1] += mr_player.speed / 1.4
            for projectile in projectilesGroup:
                projectile.x -= mr_player.speed / 1.4
                projectile.y -=mr_player.speed / 1.4

        #elif Background.display_scroll[0] < 250:
        elif keys[pygame.K_d]:
            Background.display_scroll[0] += mr_player.speed
            for projectile in projectilesGroup:
                projectile.x -= mr_player.speed


        #elif Background.display_scroll[0] > -250:
        elif keys[pygame.K_a]:
            Background.display_scroll[0] -= mr_player.speed
            for projectile in projectilesGroup:
                projectile.x += mr_player.speed


        #elif Background.display_scroll[1] > -250:
        elif keys[pygame.K_w]:
            Background.display_scroll[1] -= mr_player.speed
            for projectile in projectilesGroup:
                projectile.y += mr_player.speed


        #elif Background.display_scroll[1] < 250:
        elif keys[pygame.K_s]:
            Background.display_scroll[1] += mr_player.speed
            for projectile in projectilesGroup:
                projectile.y -= mr_player.speed

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


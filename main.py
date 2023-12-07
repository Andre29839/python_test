import pygame
from pygame.constants import QUIT 

pygame.init()

FPS = pygame.time.Clock()

HEIGTH = 800
WIDTH = 1200

COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)

main_display = pygame.display.set_mode((WIDTH, HEIGTH))

player_size = (20, 20)

player = pygame.Surface(player_size)
player.fill(COLOR_WHITE)

player_rect = player.get_rect()
player_speed = [1, 1]

playing = True

while playing: 
    FPS.tick(240)

    for e in pygame.event.get():
        if e.type == QUIT:
            playing = False

    main_display.fill(COLOR_BLACK)

    if player_rect.bottom >= HEIGTH or player_rect.top <= -1:
        player_speed[1] = -player_speed[1]

    if player_rect.right >= WIDTH or player_rect.left <= -1:
        player_speed[0] = -player_speed[0]

    main_display.blit(player, player_rect)

    player_rect = player_rect.move(player_speed)

    pygame.display.flip()
import pygame
import sys

# setup
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Base Pygame Template")
clock = pygame.time.Clock()
FPS = 60

# setup player
player_color = (255, 0, 0)
player_size = 50
player_x, player_y = WIDTH // 2, HEIGHT // 2
player_speed = 5

# loop
running = True
while running:
    dt = clock.tick(FPS) / 1000

    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_y -= player_speed
    if keys[pygame.K_s]:
        player_y += player_speed
    if keys[pygame.K_a]:
        player_x -= player_speed
    if keys[pygame.K_d]:
        player_x += player_speed


    # update state
    # TODO

    # rendering
    screen.fill((135, 206, 23))
    pygame.draw.rect(screen, player_color, (player_x, player_y, player_size, player_size))

    pygame.display.flip()

pygame.quit()
sys.exit()
import pygame
import sys

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

player = pygame.Rect((600, 350, 64, 64))

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    # RENDER YOUR GAME HERE
    pygame.draw.rect(screen, (0, 0, 0), player)
    key = pygame.key.get_pressed()
    if key[pygame.K_UP] == True:
        player.move_ip(0, -1)
    if key[pygame.K_DOWN] == True:
        player.move_ip(0, 1)
    if key[pygame.K_LEFT] == True:
        player.move_ip(-1, 0)
    if key[pygame.K_RIGHT] == True:
        player.move_ip(1, 0)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
sys.exit()
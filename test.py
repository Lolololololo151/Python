import pygame

pygame.init()
WIN_WIDTH = 16 * 90
WIN_HEIGHT = 15 * 50
SCREEN = pygame.display.set_mode([WIN_WIDTH, WIN_HEIGHT])
RUNNING = True

while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
    
    SCREEN.fill('brown')
    pygame.display.flip()
import pygame
import os

pygame.init()
WIN_WIDTH = 16 * 90
WIN_HEIGHT = 15 * 50
SCREEN = pygame.display.set_mode([WIN_WIDTH, WIN_HEIGHT])
RUNNING = True
BOARD = pygame.Rect(100, 50, 1250, 650)
BOARD_CELLS = [] 
CELL_HEIGHT = 81
CELL_WIDTH = 156
BLACK_CHECKER = pygame.image.load(os.path.join('black.png'))
WHITE_CHECKER = pygame.image.load(os.path.join('white.png'))

pygame.display.set_caption("Checkers")

for row in range(8):
    for col in range(8):
        x = 100 + col * CELL_WIDTH
        y = 50 + row * CELL_HEIGHT
        BOARD_CELLS.append(pygame.Rect(x, y, CELL_WIDTH, CELL_HEIGHT))

while RUNNING:
    CurrentPressedKey = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
    
    SCREEN.fill("brown")
    pygame.draw.rect(surface=SCREEN, color=(0, 0, 0), rect=BOARD, width=2)

    for i in range(24):
        cell = BOARD_CELLS[i]
        SCREEN.blit(WHITE_CHECKER, (cell.x, cell.y))

    for i in range(40, 64):
        cell = BOARD_CELLS[i]
        SCREEN.blit(BLACK_CHECKER, (cell.x, cell.y))

    for cell in BOARD_CELLS:
        pygame.draw.rect(surface=SCREEN, color=(0, 0, 0), rect=cell, width=2)
    
    pygame.display.flip()

#40
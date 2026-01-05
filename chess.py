import pygame

pygame.init()
WIN_WIDTH = 16 * 90
WIN_HEIGHT = 15 * 50
SCREEN = pygame.display.set_mode([WIN_WIDTH, WIN_HEIGHT])
RUNNING = True
BOARD = pygame.Rect(100, 50, 1250, 650)
BOARD_CELLS = [] 

def PrepareTheBoard():
    pygame.draw.rect(surface=SCREEN, color=(0, 0, 0), rect=BOARD, width=5)
    BOARD_CELLS = []
    CELL_HEIGHT = 81
    CELL_WIDTH = 156
    for row in range(8):
        for col in range(8):
            x = 100 + col * CELL_WIDTH
            y = 50 + row * CELL_HEIGHT
            BOARD_CELLS.append(pygame.Rect(x, y, CELL_WIDTH, CELL_HEIGHT))
    
    for cell in BOARD_CELLS:
        pygame.draw.rect(surface=SCREEN, color=(0, 0, 0), rect=cell, width=2)

while RUNNING:
    CurrentPressedKey = pygame.key.get_pressed()

    if CurrentPressedKey[pygame.K_ESCAPE]:
        RUNNING = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
    
    SCREEN.fill("brown")
    PrepareTheBoard()
    pygame.display.flip()
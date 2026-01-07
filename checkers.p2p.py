import pygame
import os
import random

pygame.init()
WIN_WIDTH = 16 * 90
WIN_HEIGHT = 15 * 50
SCREEN = pygame.display.set_mode([WIN_WIDTH, WIN_HEIGHT])
BOARD = pygame.Rect(100, 50, 1250, 650)
BOARD_CELLS = [] 
CELL_HEIGHT = 81
CELL_WIDTH = 156
BLACK_CHECKER = pygame.image.load(os.path.join('black.png'))
WHITE_CHECKER = pygame.image.load(os.path.join('white.png'))
ARE_YOU_BLACK_OR_WHITE = random.randint(0, 1)

class CheckersP2P:
    def __init__(self):
        self.RUNNING = True
        SCREEN.fill("brown")
        self.team_Chooser()
        self.prepareCells()
        self.drawBoard()
        self.drawCells()
        self.drawCheckers()
        self.gameLoop()

    def team_Chooser(self):
        if ARE_YOU_BLACK_OR_WHITE == 0:
            pygame.display.set_caption("Checkers white team")
        elif ARE_YOU_BLACK_OR_WHITE == 1:
            pygame.display.set_caption("Checkers black team")
        else:
            pygame.display.set_caption("Checkers")

    def prepareCells(self):
        for row in range(8):
            for col in range(8):
                x = 100 + col * CELL_WIDTH
                y = 50 + row * CELL_HEIGHT
                BOARD_CELLS.append(pygame.Rect(x, y, CELL_WIDTH, CELL_HEIGHT))
                #array: Rect(100, 50, 156, 81)

    def drawBoard(self):
        pygame.draw.rect(surface=SCREEN, color=(0, 0, 0), rect=BOARD, width=10)

    def drawCells(self):
        for cell in BOARD_CELLS:
            pygame.draw.rect(surface=SCREEN, color=(0, 0, 0), rect=cell, width=5)

    def drawCheckers(self):
        for i in range(24):
            cell = BOARD_CELLS[i]
            SCREEN.blit(WHITE_CHECKER, (cell.x, cell.y))
            self.BLACK_CELLS = []
            self.BLACK_CELLS.append(i)

        for i in range(40, 64):
            cell = BOARD_CELLS[i]
            SCREEN.blit(BLACK_CHECKER, (cell.x, cell.y))
            self.WHITE_CELLS = []
            self.WHITE_CELLS.append(i)

    def gameLoop(self):
        while self.RUNNING:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.RUNNING = False
            
            pygame.display.flip()

GAME = CheckersP2P()


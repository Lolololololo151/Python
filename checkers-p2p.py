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
WHITE_CHECKERS_PIC_CELL = []
BLACK_CHECKERS_PIC_CELL = []

class CheckersP2P:
    def __init__(self):
        self.selected_cell = None
        self.WHICH_TURN = 0
        self.RUNNING = True
        self.team_Chooser()
        self.prepareCells()
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
            things_To_Append = [cell.x, cell.y]
            WHITE_CHECKERS_PIC_CELL.append(things_To_Append)
        
        for i in range(40, 64):
            cell = BOARD_CELLS[i]
            SCREEN.blit(BLACK_CHECKER, (cell.x, cell.y))
            things_To_Append = [cell.x, cell.y]
            BLACK_CHECKERS_PIC_CELL.append(things_To_Append)
        
    def checkClick(self, m_pos):
        if pygame.mouse.get_just_pressed()[0]:
            if self.selected_cell != None:
                temporary_selected_cell = None
                for i in range(0, len(BOARD_CELLS)):
                    cell = BOARD_CELLS[i]
                    if cell.collidepoint(m_pos):
                        temporary_selected_cell = cell
                        print("You clicked on cell")
                        print(WHITE_CHECKERS_PIC_CELL[0])
                        print(pygame.mouse.get_pos())
                        print(cell)
                        print(temporary_selected_cell)
                        
                if temporary_selected_cell != None:
                    save_cell = BOARD_CELLS[BOARD_CELLS.index(self.selected_cell)]
                    BOARD_CELLS[BOARD_CELLS.index(self.selected_cell)].x = temporary_selected_cell.x
                    BOARD_CELLS[BOARD_CELLS.index(self.selected_cell)].y = temporary_selected_cell.y
                    if self.WHICH_TURN == 0:
                        for i, cell in enumerate(WHITE_CHECKERS_PIC_CELL):
                            # print("AAAAAA: ", i, cell, len(WHITE_CHECKERS_PIC_CELL))
                            if cell[0] == self.selected_cell.x and cell[1] == self.selected_cell.y:
                                WHITE_CHECKERS_PIC_CELL[i] = [temporary_selected_cell.x, temporary_selected_cell.y]
                                break
                           
                return
            
            temporary_selected_cell = None
            for cell in BOARD_CELLS:
                    if cell.collidepoint(m_pos):
                        temporary_selected_cell = cell
                        print("You clicked on cell")
                        print(WHITE_CHECKERS_PIC_CELL[0])
                        print(pygame.mouse.get_pos())
                        print(cell)
                        print(temporary_selected_cell)
                        break
            is_The_Correct_Cell_was_chosen = False
            if temporary_selected_cell == None:
                self.selected_cell = None
                return
            if self.WHICH_TURN == 0:
                for cell in WHITE_CHECKERS_PIC_CELL:
                    if cell[0] == temporary_selected_cell.x and cell[1] == temporary_selected_cell.y:
                        is_The_Correct_Cell_was_chosen = True
            if self.WHICH_TURN == 1:
                for cell in BLACK_CHECKERS_PIC_CELL:
                    if cell[0] == temporary_selected_cell.x and cell[1] == temporary_selected_cell.y:
                        is_The_Correct_Cell_was_chosen = True
            if is_The_Correct_Cell_was_chosen == True:
                self.selected_cell = temporary_selected_cell
    
    def highlightClickedRect(self):
            if self.selected_cell is not None:
                pygame.draw.rect(SCREEN, (0, 255, 0), self.selected_cell, 4)

    def gameLoop(self):
        while self.RUNNING:
            SCREEN.fill("brown")
            self.drawBoard()
            self.drawCells()
            self.drawCheckers()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.RUNNING = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.checkClick(pygame.mouse.get_pos())

            self.highlightClickedRect()
            pygame.display.flip()

GAME = CheckersP2P()
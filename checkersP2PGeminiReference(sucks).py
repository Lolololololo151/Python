import pygame
import os
import random

# --- Constants ---
pygame.init()
WIN_WIDTH = 16 * 90
WIN_HEIGHT = 15 * 50
SCREEN = pygame.display.set_mode([WIN_WIDTH, WIN_HEIGHT])
BOARD = pygame.Rect(100, 50, 1250, 650)
BOARD_CELLS = [] 
CELL_HEIGHT = 81
CELL_WIDTH = 156

# Note: Make sure these images exist in your folder, otherwise comment them out to run existing code
try:
    BLACK_CHECKER = pygame.image.load(os.path.join('black.png'))
    WHITE_CHECKER = pygame.image.load(os.path.join('white.png'))
except:
    print("Warning: Checker images not found. Using placeholders if needed.")

ARE_YOU_BLACK_OR_WHITE = random.randint(0, 1)

class CheckersP2P:
    def __init__(self):
        self.RUNNING = True
        self.selected_cell = None # NEW: Variable to store which cell is clicked
        
        self.team_Chooser()
        self.prepareCells()
        
        # We removed the draw calls from here. 
        # They must happen in the gameLoop to update the screen!
        
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

    # --- NEW FUNCTION: Checks if mouse clicks a cell ---
    def check_click(self, mouse_pos):
        # We iterate through every cell in our list
        for cell in BOARD_CELLS:
            # .collidepoint checks if the (x,y) of mouse is inside the rect
            if cell.collidepoint(mouse_pos):
                self.selected_cell = cell
                print(f"Cell clicked at: {cell.x}, {cell.y}") # For debug

    # --- NEW FUNCTION: Draws the green highlight ---
    def draw_highlight(self):
        if self.selected_cell is not None:
            # Draw a green rectangle at the selected cell's position
            pygame.draw.rect(SCREEN, (0, 255, 0), self.selected_cell)

    def drawBoard(self):
        pygame.draw.rect(surface=SCREEN, color=(0, 0, 0), rect=BOARD, width=10)

    def drawCells(self):
        for cell in BOARD_CELLS:
            pygame.draw.rect(surface=SCREEN, color=(0, 0, 0), rect=cell, width=5)

    def drawCheckers(self):
        # Fixed logic: Initialize lists OUTSIDE the loop
        self.BLACK_CELLS = [] 
        self.WHITE_CELLS = []

        for i in range(24):
            cell = BOARD_CELLS[i]
            # Check if image loaded, otherwise skip to prevent crash
            if 'WHITE_CHECKER' in globals(): 
                SCREEN.blit(WHITE_CHECKER, (cell.x, cell.y))
            self.BLACK_CELLS.append(i)

        for i in range(40, 64):
            cell = BOARD_CELLS[i]
            if 'BLACK_CHECKER' in globals():
                SCREEN.blit(BLACK_CHECKER, (cell.x, cell.y))
            self.WHITE_CELLS.append(i)

    def gameLoop(self):
        while self.RUNNING:
            # 1. EVENT HANDLING
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.RUNNING = False
                
                # Check for mouse click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Pass the mouse position to our new function
                    self.check_click(pygame.mouse.get_pos())

            # 2. DRAWING (Order matters!)
            SCREEN.fill("brown")       # 1. Clear screen
            self.drawBoard()           # 2. Draw border
            self.draw_highlight()      # 3. Draw Highlight (Under the checkers!)
            self.drawCells()           # 4. Draw Grid lines
            self.drawCheckers()        # 5. Draw Pieces
            
            pygame.display.flip()      # Update the display

GAME = CheckersP2P()
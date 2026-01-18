#!/usr/bin/env -S uv run --script
# /// script
# dependencies = ["pygame"]
# ///

import pygame
# print(help(pygame.Color.lerp))
# exit()

pygame.init()

SCALE = 90
WIN_WIDTH  = 14 * SCALE
WIN_HEIGHT = 12 * SCALE
BG_COLOR = pygame.Color("#181818")
SCREEN = pygame.display.set_mode([WIN_WIDTH, WIN_HEIGHT])

BOARD_PATTERN_COLOR_A = pygame.Color("white")
BOARD_PATTERN_COLOR_B = pygame.Color("#185018")
IMAGES = {
    "black": pygame.image.load('black.png'),
    "white": pygame.image.load('white.png'),
}

# Better to use enums
MY_COLOR    = "white" # white | black
ENEMY_COLOR = "black" # white | black


class Cell:
    def __init__(self, rect: pygame.Rect, piece: str):
        self.rect  = rect
        self.piece = piece # empty | black | white

    def draw(self, surface: pygame.Surface):
        if self.piece == "empty": return
        surface.blit(IMAGES[self.piece], self.rect) # width and hight are ignored


class Board:
    def __init__(self):
        self.cells: list[Cell] = []
        self.size = 8
        self.piece_rows = 3
        self.selected_cell_idx: int | None = None
        self.init_board()


    # make init_board as separete function to call it on game restart
    def init_board(self):
        # min is needed to have square cells that fit inside winow
        cell_size = min(
            SCREEN.get_width() / self.size,
            SCREEN.get_height() / self.size
        )

        # rescale image to fit in cell
        for name in IMAGES:
            IMAGES[name] = pygame.transform.scale(IMAGES[name], (cell_size, cell_size))

        # calculate padding to have board always in center
        padding_x = (SCREEN.get_width() - cell_size * self.size) / 2
        padding_y = (SCREEN.get_height() - cell_size * self.size) / 2

        for row in range(self.size):
            for col in range(self.size):
                x = col * cell_size
                y = row * cell_size
                piece = None
                # Add eneymy pieces
                # Enemy pieces should always be on top
                # It is not compfortable to have your pieces on top
                if row < self.piece_rows:
                     # checker pattern
                    if (row + col) % 2 == 1: piece = ENEMY_COLOR
                    else: piece = "empty"
                # add rows in the middle (without) pieces
                elif row >= self.piece_rows and row < self.size - self.piece_rows:
                    piece = "empty"
                # add MY_COLOR pieces to board
                # for every player his pieces should always be at bottom.
                elif row >= self.size - self.piece_rows:
                     # checker pattern
                    if (row + col) % 2 == 1: piece = MY_COLOR
                    else: piece = "empty"
                # every piece should be not None. Crash the program if not.
                # help to find out if something went wrong
                assert(piece != None)
                cell = Cell(
                    pygame.rect.Rect(x + padding_x, y + padding_y, cell_size, cell_size),
                    piece
                )
                self.cells.append(cell)

    # get coordinate from screen e.g mouse position and transte to index of cell on board
    # or return None if no cell in that place on screen
    # TODO: maybe I don't need this function and can move impementaion to `self.select_cell`
    def screen_to_board(self, p: pygame.Vector2) -> int | None:
        for i, cell in enumerate(self.cells):
            if cell.rect.collidepoint(p):
                return i
        return None

    # select cell using screen coordinated e.g. mouse coordinates
    # selected cell will be stored in `self.selected_cell_idx` and will be higlihted on draw
    def select_cell(self, p: pygame.Vector2):
        # if try to select, but don't there is no cell in coordinate deselect
        # so `None` is okay
        self.selected_cell_idx = self.screen_to_board(p)

    def draw(self, surface: pygame.Surface):
        for i, cell in enumerate(self.cells):
            col = i % self.size
            row = i // self.size
            # draw grid
            bg_color = None
            if (row + col) % 2 == 0:
                bg_color = BOARD_PATTERN_COLOR_A
            else:
                bg_color = BOARD_PATTERN_COLOR_B
            if self.selected_cell_idx != None and i == self.selected_cell_idx:
                # higlight. Get value 0.6 from gradient `bg_color`->green
                bg_color = bg_color.lerp("green", 0.6)
            pygame.draw.rect(surface, bg_color, cell)

            # draw piece
            cell.draw(surface)

class Game:
    def __init__(self):
        self.running = True
        self.board = Board()
        self.turn = "white" # white | black
        self.was_mouse_pressed = False

    # helper funcion analog of `just_pressed` in community version
    def is_left_mouse_clicked(self) -> bool:
        if not pygame.mouse.get_pressed()[0] and self.was_mouse_pressed:
            self.was_mouse_pressed = False
            return True
        if pygame.mouse.get_pressed()[0]:
            self.was_mouse_pressed = True
        return False

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    # TODO: piece can move only one squere diagonal
    # TODO: add rules of the game e.g. should take if can (maybe as new function)
    # TODO: implement taking other piece (one or many)  (maybe inside `self.make_move`)
    def is_move_legal(self, from_cell_idx: int, to_cell_idx: int) -> bool:
        # check if preivously selected cell is valid and new selected is valid
        if from_cell_idx == None or to_cell_idx == None:
            return False
        # first selection must a have piece (can't move nothing)
        if self.board.cells[from_cell_idx].piece == "empty":
            return False
        # can't move my piece on top of another even if I take I do it over piece
        if self.board.cells[to_cell_idx].piece != "empty":
            return False
        # can't move pieces of my oponnent
        if self.board.cells[from_cell_idx].piece != self.turn:
            print(f"Can't move {self.board.cells[from_cell_idx].piece} pieces on turn {self.turn}")
            return False
        return True

    def make_move(self, from_cell_idx: int, to_cell_idx: int):
        from_piece = self.board.cells[from_cell_idx].piece
        self.board.cells[to_cell_idx].piece = from_piece
        self.board.cells[from_cell_idx].piece = "empty"
        self.board.selected_cell_idx = None
        # python analog of C++ '? :'
        self.turn = "white" if self.turn == "black" else "black"

    def loop(self):
        while self.running:
            self.handle_events()

            if self.is_left_mouse_clicked():
                m_pos = pygame.mouse.get_pos()
                prev_selected_idx = self.board.selected_cell_idx
                self.board.select_cell(m_pos)
                if self.is_move_legal(prev_selected_idx, self.board.selected_cell_idx):
                    print("Making a move ...")
                    self.make_move(prev_selected_idx, self.board.selected_cell_idx)

            SCREEN.fill(BG_COLOR)
            self.board.draw(SCREEN)
            pygame.display.flip()


game = Game()
game.loop()

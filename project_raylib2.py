import pyray as pr

CELL_WIDTH = 40
CELL_HEIGHT = 30
WIN_WIDTH = 16 * 100
WIN_HEIGHT = 9 * 100

pr.init_window(WIN_WIDTH, WIN_HEIGHT, "Grid")

while not pr.window_should_close():
    pr.begin_drawing()
    pr.clear_background([25, 23, 36, 255])
    for X in range(CELL_WIDTH, WIN_WIDTH, CELL_WIDTH):
        pr.draw_line(X, 0, X, WIN_HEIGHT, pr.RED)
    for Y in range(CELL_HEIGHT, WIN_HEIGHT, CELL_HEIGHT):
        pr.draw_line(0, Y, WIN_WIDTH, Y, pr.RED)

    pr.draw_rectangle(pr.get_mouse_x() // CELL_WIDTH * CELL_WIDTH,
                      pr.get_mouse_y() // CELL_HEIGHT * CELL_HEIGHT,
                      CELL_WIDTH, CELL_HEIGHT, pr.GREEN)
    #pr.get_mouse_x()
    #pr.get_mouse_y()
    pr.end_drawing()


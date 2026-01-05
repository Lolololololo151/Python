import pyray as rl
import random

rl.init_window(600, 800, "Tree")
toys = []

def draw_tree():
    rl.draw_triangle((200, 150), (400, 150), (300, 0), rl.GREEN)
    rl.draw_triangle((150, 300), (450, 300), (300, 100), rl.GREEN)
    rl.draw_triangle((100, 500), (500, 500), (300, 150), rl.GREEN)
    rl.draw_rectangle(250, 500, 100, 100, rl.BROWN)

while not rl.window_should_close():
    rl.begin_drawing()
    rl.clear_background(rl.SKYBLUE)
    rl.draw_text("Happy", 30, 30, 40, rl.RED)
    rl.draw_text("New", 400, 20, 52, rl.RED)
    rl.draw_text("Year", 450, 80, 52, rl.RED)
    draw_tree()
    for toy in toys:
        rl.draw_circle_v(toy[0], toy[1], toy[2])
    m_pos = rl.get_mouse_position()

    if rl.is_mouse_button_pressed(rl.MouseButton.MOUSE_BUTTON_LEFT):
        rand_color = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
            255
        )
        toys.append([m_pos, random.randint(2, 10), rand_color])
        print("Drawing Circle")

    rl.end_drawing()
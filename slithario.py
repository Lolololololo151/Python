import socket

import pyray as rl

class Button:
    def __init__(self, rect: rl.Rectangle, texture: rl.Texture2D):
        self.rect = rect
        self.texture = texture
    def draw(self):
        rl.drawTexture_Pro(
            self.texture, 
            rl.Rectangle(0, 0, self.texture.width, self.texture.height), 
            self.dest_rec, 
            [0, 0], 
            0,
            rl.WHITE
        )


BG_COLOR = rl.Color(50, 50, 50, 255)


rl.init_window(600, 600, "Slitherio")

IMAGES = {
    "host": rl.load_texture("knopka2.png"),
    "connect": rl.load_texture("knopka.png")
}

BTN_HOST = Button(rl.Rectangle(0, 0, 200, 200), IMAGES["host"])
BTN_CONNECT = Button(rl.Rectangle(100, 0, 100, 100), IMAGES["connect"])

while not rl.window_should_close():
    rl.begin_drawing()
    rl.draw_texture(IMAGES["host"], 0, 0, rl.WHITE)
    rl.clear_background(BG_COLOR)
    rl.end_drawing()

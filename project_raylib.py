import pyray as pr
import random

pr.init_window(1800, 900, "Raylib")

japan_random_color = int(random.randint(0, 255))
japan_random_color_1 = int(random.randint(0, 255))
japan_random_color_2 = int(random.randint(0, 255))

X_Circle = int(1800 / 2)
Y_Circle = int(900 / 2)
pr.set_target_fps(60)

# history = []

# Circle

while not pr.window_should_close():
    dt = pr.get_frame_time()
    Circle_Speed = 500 * dt
    pr.begin_drawing()
    pr.clear_background(pr.WHITE)
    pr.draw_circle(
        int(X_Circle), int(Y_Circle),
        200,
        [
            japan_random_color,
            japan_random_color_1,
            japan_random_color_2,
            255
        ]
    )

    # a = [ [1, 2], [3, 4]]
    # for i in a[1:]:
    #     print(i[0])
    # history.append([X_Circle, Y_Circle])
    # for c in history:
    #     c[0] c[1]
    if pr.is_key_down(pr.KEY_RIGHT):
        print("Right")
        X_Circle += Circle_Speed
    if pr.is_key_down(pr.KEY_UP):
        print("Up")
        Y_Circle -= Circle_Speed
    if pr.is_key_down(pr.KEY_DOWN):
        print("Down")
        Y_Circle += Circle_Speed
    if pr.is_key_down(pr.KEY_LEFT):
        print("Left")
        X_Circle -= Circle_Speed
    pr.end_drawing()
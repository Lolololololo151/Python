# name = input("Enter your full name: ")
# print(f"Your name is {name}")
# surname = input("Enter your surname: ")
# print(f"Your surname is: {surname}")

# def name_Check(theName):
#     usersName = input("What's your name?: ")
#     if usersName == theName:
#         print("Thats my name!!! Give it back!")
#     else:
#         print(f"Hello {usersName}")

# name_Check("Roma")

# def say_my_name():
#     print("Hello, Alex")
#     print("Hello, Katya")
#     print("Hello, Kotenok")

# say_my_name()

import pyray as pr

WIN_WIDTH = 16 * 100
WIN_HEIGHT = 9 * 100

X_Circle = int(WIN_WIDTH / 2)
Y_Circle = int(WIN_HEIGHT / 2)
pr.set_target_fps(60)

pr.init_window(WIN_WIDTH, WIN_HEIGHT, "DVD")
Circle_Speed = 500
while not pr.window_should_close():
    dt = pr.get_frame_time()
   
    pr.begin_drawing()
    pr.clear_background([25, 23, 36, 255])
    pr.draw_circle(
        int(X_Circle),
        int(Y_Circle),
        100,
        [
            255,
            255,
            255,
            255
        ]
    )
    X_Circle += Circle_Speed * dt
    if X_Circle > WIN_WIDTH:
        Circle_Speed = Circle_Speed * -1
    if X_Circle < 0:
        Circle_Speed = Circle_Speed * -1
    pr.end_drawing()
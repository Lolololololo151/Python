import pygame

pygame.init()
WIN_WIDTH = 16 * 90
WIN_HEIGHT = 15 * 50
SCREEN = pygame.display.set_mode([WIN_WIDTH, WIN_HEIGHT])
print(type(SCREEN))
CLOCK = pygame.time.Clock()
RUNNING = True


class Circle:
    def __init__(self, color, position):
        self.color = color
        self.position = position

    def draw(self, surface):
        pygame.draw.circle(
        surface,
        self.color,
        self.position, 
        50
        )

    def place(self, position):
        self.position = position


CIRCLE = Circle("red", [50, 50])
while RUNNING:
    currentPressedKey = pygame.key.get_pressed()

    if currentPressedKey[pygame.K_SPACE]:
        RUNNING = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = True

    SCREEN.fill("black")
    CIRCLE.draw(SCREEN)
    CIRCLE.place([400, 100])
    pygame.display.flip()
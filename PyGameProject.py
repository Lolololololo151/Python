import pygame
import animation
import math

pygame.init()
WIN_WIDTH = 16 * 90
WIN_HEIGHT = 15 * 50
screen = pygame.display.set_mode([WIN_WIDTH, WIN_HEIGHT])
print(type(screen))

clock = pygame.time.Clock()

class Player:
    def __init__(self):
        self.pos = pygame.math.Vector2(0, 0)
        self.speed = 1


    def move(self):
        m_pos = pygame.mouse.get_pos()
        if self.pos.distance_to(m_pos) > 5:
            dir = m_pos - self.pos
            dir = dir.normalize()
            self.pos += dir * self.speed

#player = Player()

player = animation.Animal("robocode", 0.5, (79, 227, 134))

running = True

while running:
    CurrentPressedKey = pygame.key.get_pressed()

    if CurrentPressedKey[pygame.K_SPACE]:
        running = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = True

    screen.fill("black")
    player.move_animal(pygame.mouse.get_pos(), 100)
    player.draw_animal(screen)
    #pygame.draw.circle(screen, "red", player.pos, 50)
    pygame.display.flip()
    print(clock.get_fps())
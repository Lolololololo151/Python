import pygame

class Main():
    def __init__(self, backgroundColor, WIN_WIDTH, WIN_HEIGHT):
        self.backgroundColor=backgroundColor
        self.WIN_WIDTH=WIN_WIDTH
        self.WIN_HEIGHT=WIN_HEIGHT
        self.SCREEN=pygame.display.set_mode([self.WIN_WIDTH, self.WIN_HEIGHT])
        self.RUNNING=True
        print("Initial Variables Initialized.")
        self.initPyGameScreen()
    
    def initPyGameScreen(self):
        while self.RUNNING:
            self.currentPressedKey = pygame.key.get_pressed()

            if self.currentPressedKey[pygame.K_SPACE]:
                self.RUNNING = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.RUNNING = True
            
            self.SCREEN.fill(self.backgroundColor)
            self.drawCircle(circleColor="red", position=[500, 500], radius=60)
            pygame.display.flip()
    
    def drawCircle(self, circleColor, position, radius):
        pygame.draw.circle(
            self.SCREEN,
            circleColor,
            position,
            radius
        )

Main = Main(backgroundColor="blue", WIN_WIDTH=16 * 90, WIN_HEIGHT=15 * 50)
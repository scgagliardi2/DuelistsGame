# gain access to the pygame library
import pygame

# size of game screen
ScreenWidth = 700
ScreenHeight = 700
ScreenTitle = 'Duelists Game'

class Map:

    def __init__(self):
        self.title = ScreenTitle
        self.height = ScreenHeight
        self.width = ScreenWidth
        self.CameraX = -250
        self.CameraY = -350
        # set window title
        pygame.display.set_caption(self.title)
        # create game display window
        self.GameScreen = pygame.display.set_mode((self.width, self.height))
        # set background
        BackgroundImage = pygame.image.load('Images/Grass Map 1.jpg')
        self.image = pygame.transform.scale(BackgroundImage, (self.width*3, self.height*2))

    def draw(self):
        self.GameScreen.blit(self.image, (self.CameraX, self.CameraY))

    def update_camera(self, direction):
        if direction == 'right':
            self.CameraX -= 5
        elif direction == 'left':
            self.CameraX += 5
        elif direction == 'down':
            self.CameraY -= 5
        elif direction == 'up':
            self.CameraY += 5

# gain access to the pygame library
import pygame
import TerrainObject

# size of game screen
ScreenWidth = 900
ScreenHeight = 900
ScreenTitle = 'Duelists Game'

class Map:

    def __init__(self):
        self.title = ScreenTitle
        self.height = ScreenHeight
        self.width = ScreenWidth
        # set window title
        pygame.display.set_caption(self.title)
        # create game display window
        self.GameScreen = pygame.display.set_mode((self.width, self.height))
        # set background
        BackgroundImage = pygame.image.load('Images/Grass Map 2.jpg')
        self.image = pygame.transform.scale(BackgroundImage, (self.width, self.height))

    def draw(self):
        self.GameScreen.blit(self.image, (0, 0))
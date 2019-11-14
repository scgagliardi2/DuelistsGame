# gain access to the pygame library
import pygame

# size of game screen
ScreenWidth = 900
ScreenHeight = 900
ScreenTitle = 'Duelists Game'

# RGB Color codes
WhiteColor = (255, 255, 255)
BlackColor = (0, 0, 0)
RedColor = (255, 0, 0)
BlueColor = (0, 0, 255)
GreenColor = (0, 255, 0)


class Map:

    def __init__(self):
        self.title = ScreenTitle
        self.height = ScreenHeight
        self.width = ScreenWidth
        self.occupiedSpaces = [[]]
        # set window title
        pygame.display.set_caption(self.title)
        # create game display window
        self.GameScreen = pygame.display.set_mode((self.width, self.height))
        # set background
        BackgroundImage = pygame.image.load('Images/Grass Map 2.jpg')
        self.image = pygame.transform.scale(BackgroundImage, (self.width, self.height))

    def draw(self):
        self.GameScreen.blit(self.image, (0, 0))
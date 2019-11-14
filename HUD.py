import pygame

pygame.init()

class HUD:

    def __init__(self, ImagePath, x, y, width, heigth):
        # create player image
        ObjectImage = pygame.image.load(ImagePath)
        # scale image
        self.image = pygame.transform.scale(ObjectImage, (100, 100))

        self.xPos = x
        self.yPos = y

        self.width = width
        self.height = heigth

    def draw(self, background):
        background.blit(self.image, (self.xPos, self.yPos))

import pygame

pygame.init()


class TerrainObject:

    def __init__(self, ImagePath, x, y, width, heigth):
        self.width = width
        self.height = heigth

        # create terrian image
        ObjectImage = pygame.image.load(ImagePath)
        # scale image
        self.image = pygame.transform.scale(
            ObjectImage, (self.width, self.height))

        self.xPos = x
        self.yPos = y

    def draw(self, background):
        background.blit(self.image, (self.xPos, self.yPos))

    def update_camera(self, direction):
        if direction == 'right':
            self.xPos -= 5
        elif direction == 'left':
            self.xPos += 5
        elif direction == 'down':
            self.yPos -= 5
        elif direction == 'up':
            self.yPos += 5

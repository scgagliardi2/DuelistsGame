import pygame


class Player:

    Speed = 5

    def __init__(self, ImagePath, x, y, width, heigth):
        self.width = width
        self.height = heigth

        # create player image
        ObjectImage = pygame.image.load(ImagePath)
        # scale image
        self.image = pygame.transform.scale(
            ObjectImage, (self.width, self.height))

        self.xPos = x
        self.yPos = y

    def draw(self, background):
        background.blit(self.image, (self.xPos, self.yPos))

    def move(self, direction):
        if direction == "up":
            if self.yPos <= -20:
                pass
            else:
                self.yPos -= self.Speed
        elif direction == "down":
            if self.yPos >= 880:
                pass
            else:
                self.yPos += self.Speed
        elif direction == "left":
            if self.xPos <= -20:
                pass
            else:
                self.xPos -= self.Speed
        elif direction == "right":
            if self.xPos >= 880:
                pass
            else:
                self.xPos += self.Speed

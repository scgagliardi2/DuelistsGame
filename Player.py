import pygame
import GameObject


class PlayerCharacter(GameObject):

    Speed = 5

    def __init__(self, ImagePath, x, y, width, heigth):
        super().__init__(ImagePath, x, y, width, heigth)

    def draw(self, background):
        background.blit(self.image, (self.xPos, self.yPos))

    def move(self, direction):
        if direction == "up":
            if self.yPos <= -30:
                pass
            else:
                self.yPos -= self.Speed
        elif direction == "down":
            if self.yPos >= 710:
                pass
            else:
                self.yPos += self.Speed
        elif direction == "left":
            if self.xPos <= -30:
                pass
            else:
                self.xPos -= self.Speed
        elif direction == "right":
            if self.xPos >= 750:
                pass
            else:
                self.xPos += self.Speed

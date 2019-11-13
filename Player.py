import pygame
import Map
import Spellbook
import Spell


class Player:

    # base player speed
    Speed = 5

    def __init__(self, ImagePath, x, y, width, heigth):
        self.Width = width
        self.Height = heigth
        # create player image
        ObjectImage = pygame.image.load(ImagePath)
        # scale image
        self.image = pygame.transform.scale(
            ObjectImage, (self.Width, self.Height))
        self.XPosition = x
        self.YPosition = y
        self.BoundingBox = [self.XPosition, self.YPosition,
                            self.Width, self.Height]
        # Spellbook that player has access to
        CreateSpellBook = Spellbook.Spellbook()
        self.SpellBook = CreateSpellBook.spellbook
        self.Spell1 = self.SpellBook['Blast']
        self.Spell1.KeyBinding = "1"
        self.Spell2 = self.SpellBook['Barrier']
        self.Spell2.KeyBinding = "2"
        self.Spell3 = self.SpellBook['Water Prison']
        self.Spell3.KeyBinding = "3"
        self.Spell4 = self.SpellBook['Lightfoot']
        self.Spell4.KeyBinding = "4"

    def draw(self, background, map):
        background.blit(self.image, (self.XPosition, self.YPosition))

    def move(self, direction):
        if direction == "up":
            if self.YPosition <= -20:
                pass
            else:
                self.YPosition -= self.Speed
        elif direction == "down":
            if self.YPosition >= 880:
                pass
            else:
                self.YPosition += self.Speed
        elif direction == "left":
            if self.XPosition <= -20:
                pass
            else:
                self.XPosition -= self.Speed
        elif direction == "right":
            if self.XPosition >= 880:
                pass
            else:
                self.XPosition += self.Speed
        self.BoundingBox = [self.XPosition, self.YPosition,
                            self.Width, self.Height]

    def get_bounds(self, map):
        pass

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
        self.Facing = "up"
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

    def move(self, x, y):
        XTravel = x - self.XPosition
        YTravel = y - self.YPosition
        
        #face the character a new direction
        if abs(XTravel) > abs(YTravel):
            if x > self.XPosition:
                ObjectImage = pygame.image.load('Images/Wizard Sprite/Wizard Right Face.png')
                self.image = pygame.transform.scale(ObjectImage, (self.Width, self.Height))
                self.Facing = 'right'
            else:
                ObjectImage = pygame.image.load('Images/Wizard Sprite/Wizard Left Face.png')
                self.image = pygame.transform.scale(ObjectImage, (self.Width, self.Height))
                self.Facing = 'left'
        else:
            if y < self.YPosition:
                ObjectImage = pygame.image.load('Images/Wizard Sprite/Wizard Back Face.png')
                self.image = pygame.transform.scale(ObjectImage, (self.Width, self.Height))
                self.Facing = 'up'
            else:
                ObjectImage = pygame.image.load('Images/Wizard Sprite/Wizard Front Face.png')
                self.image = pygame.transform.scale(ObjectImage, (self.Width, self.Height))
                self.Facing = 'down'

        self.XPosition = x
        self.YPosition = y       

    def get_bounds(self, map):
        pass

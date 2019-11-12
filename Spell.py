from enum import Enum
import pygame


class SpellClass(Enum):
    ATTACK = 'ATTACK',
    SPECIAL_ATTACK = 'SPECIAL ATTACK',
    STAT = 'STAT',
    STATUS = 'STATUS',


class SpellType(Enum):
    FIRE = 'FIRE',
    ELECTRIC = 'ELECTRIC',
    WATER = 'WATER',
    EARTH = 'EARTH',
    WIND = 'WIND',


class Status(Enum):
    HEALTHY = 'HEALTHY',
    PARALYZED = 'PARALYZED',
    SLOWED = 'SLOWED',
    POISONED = 'POISONED',
    BURNED = 'BURNED',
    FROZEN = 'FROZEN',
    ASLEEP = 'ASLEEP',
    BLIND = 'BLIND',
    ROOTED = 'ROOTED',
    SHEILDED = 'SHEILDED',
    NA = 'NA'


class Stat(Enum):
    ATTACK = 'ATTACK',
    DEFENSE = 'DEFENSE',
    SHEILD = 'SHEILD',
    SPEED = 'SPEED',
    HIT_CHANCE = 'HIT_CHANCE',
    EVASIVNESS = 'EVASIVNESS',
    NONE = 'NONE'


class Spell:

    def __init__(self, ImagePath, x, y, width, heigth):
        # create spell image
        ObjectImage = pygame.image.load(ImagePath)
        # scale image
        self.image = pygame.transform.scale(ObjectImage, (100, 100))

        self.xPos = x
        self.yPos = y

        self.width = width
        self.height = heigth

        #self.name = name
        #self.SpellClass = SpellClass
        #self.damage = damage
        #self.travelspeed = travelspeed
        #self.SpellType = SpellType
        #self.StatusEffect = Status
        #self.StatEffect = Stat

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

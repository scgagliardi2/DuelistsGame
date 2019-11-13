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

    def __init__(self, KeyBinding, ImagePath, width, heigth, name, SpellClass, damage, travelspeed, SpellType, Status, Stat):
        self.KeyBinding = KeyBinding
        self.width = width
        self.height = heigth
        self.ImagePath = ImagePath
        self.name = name
        self.SpellClass = SpellClass
        self.damage = damage
        self.travelspeed = travelspeed
        self.SpellType = SpellType
        self.StatusEffect = Status
        self.StatEffect = Stat
        self.x = 0
        self.y = 0

    def draw(self, background, x, y):
        # create spell image
        ObjectImage = pygame.image.load(self.ImagePath)
        # scale image
        self.image = pygame.transform.scale(
            ObjectImage, (self.width, self.height))
        self.x = x
        self.y = y
        background.blit(self.image, (self.x, self.y))

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

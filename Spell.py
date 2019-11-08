from enum import Enum


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

    def __init__(self, name, SpellClass, damage, travelspeed, SpellType, Status, Stat):
        self.name = name
        self.SpellClass = SpellClass
        self.damage = damage
        self.travelspeed = travelspeed
        self.SpellType = SpellType
        self.StatusEffect = Status
        self.StatEffect = Stat

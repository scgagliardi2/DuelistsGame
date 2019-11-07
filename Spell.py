from enum import Enum


class SpellClass(Enum):
    ATTACK = 'ATTACK',
    SPECIAL ATTACK = 'SPECIAL ATTACK',
    STAT = 'STAT',
    STATUS = 'STATUS',


class SpellType(Enum):
    FIRE,
    ELECTRIC,
    WATER,
    EARTH,
    WIND,


class Status(Enum):
    HEALTHY,
    PARALYZED,
    SLOWED,
    POISONED,
    BURNED,
    FROZEN,
    ASLEEP,
    BLIND,
    ROOTED,
    SHEILDED,
    NA


class Stat(Enum):
    ATTACK,
    DEFENSE,
    SHEILD,
    SPEED,
    HIT_CHANCE,
    EVASIVNESS,
    NONE


class Spell:

    def __init__(self, name, SpellClass, damage, travelspeed, SpellType, Status, Stat):
        self.name = name
        self.SpellClass = SpellClass
        self.damage = damage
        self.travelspeed = travelspeed
        self.SpellType = SpellType
        self.StatusEffect = Status
        self.StatEffect = Stat

import Spell


class Player:

    def __init__(self):
        self.speed = 20
        self.attack = 40
        self.defense = 20
        self.health = 1000
        self.sheild = 0
        self.moveOne = Spell.Spell("Empty1", Spell.SpellClass.ATTACK, 0,
                                   0, Spell.SpellType.WATER, Spell.Status.NA, Spell.Stat.NONE)

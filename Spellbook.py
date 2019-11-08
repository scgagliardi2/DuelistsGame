import Spell


class Spellbook():

    def __init__(self):
        self.spellbook = {"Blast": Spell.Spell("Blast", Spell.SpellClass.ATTACK, 50, 20, Spell.SpellType.FIRE, Spell.Status.NA, Spell.Stat.NONE),
                          "Earthquake": Spell.Spell("Earthquake", Spell.SpellClass.ATTACK, 50, 15, Spell.SpellType.EARTH, Spell.Status.NA, Spell.Stat.NONE),
                          "Barrier": Spell.Spell("Barrier", Spell.SpellClass.STAT, 50, 0, Spell.SpellType.ELECTRIC, Spell.Status.NA, Spell.Stat.SHEILD),
                          "Water Prison": Spell.Spell("Water Prison", Spell.SpellClass.STATUS, 50, 0, Spell.SpellType.WATER, Spell.Status.ROOTED, Spell.Stat.SPEED)}

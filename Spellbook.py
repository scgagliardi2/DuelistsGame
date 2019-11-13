import Spell


class Spellbook():

    def __init__(self):
        self.spellbook = {"Blast": Spell.Spell('1', 'Images/Spells/Blast.png', 30, 30, "Blast", Spell.SpellClass.ATTACK, 50, 20, Spell.SpellType.FIRE, Spell.Status.NA, Spell.Stat.NONE),
                          "Barrier": Spell.Spell('1', 'Images/Spells/Barrier.png', 35, 35, "Barrier", Spell.SpellClass.STAT, 50, 0, Spell.SpellType.ELECTRIC, Spell.Status.NA, Spell.Stat.SHEILD),
                          "Water Prison": Spell.Spell('1', 'Images/Spells/Water Prison.jpg', 30, 30, "Water Prison", Spell.SpellClass.STATUS, 50, 0, Spell.SpellType.WATER, Spell.Status.ROOTED, Spell.Stat.SPEED),
                          "Lightfoot": Spell.Spell('1', 'Images/Spells/Lightfoot.jpeg', 30, 30, "Lightfoot", Spell.SpellClass.STAT, 30, 0, Spell.SpellType.WIND, Spell.Status.NA, Spell.Stat.SPEED)}

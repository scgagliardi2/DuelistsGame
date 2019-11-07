import Spell

class Spellbook():

    def __init__(self):
        self.spellbook = {"Blast": Spell("Blast", SpellClass.ATTACK, 50, 20, SpellType.FIRE, Status.NA, Stat.NONE),
                          "Earthquake": Spell("Earthquake", SpellClass.ATTACK, 50, 15, SpellType.EARTH, Status.NA, Stat.NONE)}


sp = Spellbook()

print(sp.spellbook)

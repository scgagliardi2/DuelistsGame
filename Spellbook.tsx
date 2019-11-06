import Spell, { SpellClass, SpellType, Status, Stat } from './Spell';

export default class Spellbook {

    static list: Map<String, Spell> = new Map<String, Spell>();

    build() {
        Spellbook.list.set("Blast", new Spell("Blast", SpellClass.ATTACK, 50, 20, SpellType.FIRE, Status.NA, Stat.NONE));
        Spellbook.list.set("Earthquake", new Spell("Earthquake", SpellClass.ATTACK, 50, 15, SpellType.EARTH, Status.NA, Stat.NONE));
    }

} 
export enum SpellClass {
    ATTACK,
    SPECIAL_ATTACK,
    STAT,
    STATUS,
}

export enum SpellType {
    FIRE,
    ELECTRIC,
    WATER,
    EARTH,
    WIND,
}

export enum Status {
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
}

export enum Stat {
    ATTACK,
    DEFENSE,
    SHEILD,
    SPEED,
    HIT_CHANCE,
    EVASIVNESS,
    NONE
}

export default class Spell {
    Name: string
    Classifiaction: SpellClass;
    Damage: number;
    TravelSpeed: number;
    Type: SpellType;
    StatusEffect: Status;
    StatEffect: Stat;

    constructor(Name: string, spellclass: SpellClass, damage: number, travelspeed: number, type: SpellType, status: Status, stat: Stat) {
        this.Name = Name;
        this.Classifiaction = spellclass;
        this.Damage = damage;
        this.TravelSpeed = travelspeed;
        this.Type = type;
        this.StatusEffect = status;
        this.StatEffect = stat;
    }
}
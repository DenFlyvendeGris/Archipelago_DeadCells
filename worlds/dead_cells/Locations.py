"""
Dead Cells APWorld — locations.py

Defines every location that can hold a multiworld item.

ID base: 45_100_000
  Boss kills:          45_100_001 – 45_100_049
  Timed door chests:   45_100_050 – 45_100_099
  Blueprint pickups:   45_100_100 – 45_100_199
  DLC locations:       45_100_200 – 45_100_299
  Elite kills:         45_100_300 – 45_100_399  (only when the elite_checks option is on)
"""

from typing import Dict, NamedTuple, Optional


class DeadCellsLocationData(NamedTuple):
    code: Optional[int]   # None = event location
    region: str           # which Region this location belongs to
    dlc: Optional[str]    # None = base game; otherwise the DLC option name
    option: Optional[str] = None  # extra toggle that must also be on (e.g. "elite_checks")


# ── Boss kill locations ───────────────────────────────────────────────────────

BOSS_LOCATIONS: Dict[str, DeadCellsLocationData] = {
    "Defeat Concierge":           DeadCellsLocationData(45_100_001, "Black Bridge",        None),
    "Defeat Conjunctivius":       DeadCellsLocationData(45_100_002, "Insufferable Crypt",  None),
    "Defeat Timekeeper":          DeadCellsLocationData(45_100_003, "Clock Room",           None),
    "Defeat Hand of the King":    DeadCellsLocationData(45_100_004, "Throne Room",          None),
    # DLC bosses
    "Defeat Mama Tick":           DeadCellsLocationData(45_100_010, "Nest",                 "dlc_the_bad_seed"),
    "Defeat Scarecrow":           DeadCellsLocationData(45_100_011, "Mausoleum",            "dlc_fatal_falls"),
    "Defeat The Giant":           DeadCellsLocationData(45_100_012, "Guardian's Haven",    "dlc_rise_of_the_giant"),
    "Defeat Servants and Queen":  DeadCellsLocationData(45_100_013, "Lighthouse",           "dlc_queen_and_the_sea"),
    "Defeat The Collector":       DeadCellsLocationData(None,       "Astrolab",             "dlc_rise_of_the_giant"),  # event
}

# ── Timed door chest locations ────────────────────────────────────────────────

TIMED_DOOR_LOCATIONS: Dict[str, DeadCellsLocationData] = {
    # Prisoners' Quarters
    "Prisoners' Quarters - Bronze Door":        DeadCellsLocationData(45_100_050, "Prisoners' Quarters", None),
    # Promenade of the Condemned
    "Promenade - Bronze Door":                  DeadCellsLocationData(45_100_051, "Promenade",           None),
    "Promenade - Silver Door":                  DeadCellsLocationData(45_100_052, "Promenade",           None),
    "Promenade - Gold Door":                    DeadCellsLocationData(45_100_053, "Promenade",           None),
    # Toxic Sewers
    "Toxic Sewers - Bronze Door":               DeadCellsLocationData(45_100_054, "Toxic Sewers",        None),
    "Toxic Sewers - Silver Door":               DeadCellsLocationData(45_100_055, "Toxic Sewers",        None),
    # Ramparts
    "Ramparts - Bronze Door":                   DeadCellsLocationData(45_100_056, "Ramparts",            None),
    "Ramparts - Silver Door":                   DeadCellsLocationData(45_100_057, "Ramparts",            None),
    "Ramparts - Gold Door":                     DeadCellsLocationData(45_100_058, "Ramparts",            None),
    # Ossuary
    "Ossuary - Bronze Door":                    DeadCellsLocationData(45_100_059, "Ossuary",             None),
    "Ossuary - Silver Door":                    DeadCellsLocationData(45_100_060, "Ossuary",             None),
    # Ancient Sewers
    "Ancient Sewers - Bronze Door":             DeadCellsLocationData(45_100_061, "Ancient Sewers",      None),
    "Ancient Sewers - Silver Door":             DeadCellsLocationData(45_100_062, "Ancient Sewers",      None),
    # Stilt Village
    "Stilt Village - Bronze Door":              DeadCellsLocationData(45_100_063, "Stilt Village",       None),
    "Stilt Village - Silver Door":              DeadCellsLocationData(45_100_064, "Stilt Village",       None),
    "Stilt Village - Gold Door":                DeadCellsLocationData(45_100_065, "Stilt Village",       None),
    # Slumbering Sanctuary
    "Slumbering Sanctuary - Bronze Door":       DeadCellsLocationData(45_100_066, "Slumbering Sanctuary", None),
    "Slumbering Sanctuary - Silver Door":       DeadCellsLocationData(45_100_067, "Slumbering Sanctuary", None),
    # Graveyard
    "Graveyard - Bronze Door":                  DeadCellsLocationData(45_100_068, "Graveyard",           None),
    "Graveyard - Silver Door":                  DeadCellsLocationData(45_100_069, "Graveyard",           None),
    # Clock Tower
    "Clock Tower - Bronze Door":                DeadCellsLocationData(45_100_070, "Clock Tower",         None),
    "Clock Tower - Silver Door":                DeadCellsLocationData(45_100_071, "Clock Tower",         None),
    "Clock Tower - Gold Door":                  DeadCellsLocationData(45_100_072, "Clock Tower",         None),
    # Forgotten Sepulcher
    "Forgotten Sepulcher - Bronze Door":        DeadCellsLocationData(45_100_073, "Forgotten Sepulcher", None),
    "Forgotten Sepulcher - Silver Door":        DeadCellsLocationData(45_100_074, "Forgotten Sepulcher", None),
    # High Peak Castle
    "High Peak Castle - Bronze Door":           DeadCellsLocationData(45_100_075, "High Peak Castle",    None),
    "High Peak Castle - Silver Door":           DeadCellsLocationData(45_100_076, "High Peak Castle",    None),
    "High Peak Castle - Gold Door":             DeadCellsLocationData(45_100_077, "High Peak Castle",    None),
    # Derelict Distillery
    "Derelict Distillery - Bronze Door":        DeadCellsLocationData(45_100_078, "Derelict Distillery", None),
    "Derelict Distillery - Silver Door":        DeadCellsLocationData(45_100_079, "Derelict Distillery", None),
}

# ── Fixed blueprint pickup locations ─────────────────────────────────────────
# These are the 42 blueprints found in secret areas, puzzles, and locked rooms
# rather than random enemy drops. Each has a fixed, known location.

BLUEPRINT_LOCATIONS: Dict[str, DeadCellsLocationData] = {
    # Prisoners' Quarters
    "Prisoners' Quarters - Broadsword Blueprint":        DeadCellsLocationData(45_100_100, "Prisoners' Quarters", None),
    "Prisoners' Quarters - Disengagement Blueprint":     DeadCellsLocationData(45_100_101, "Prisoners' Quarters", None),
    # Promenade of the Condemned
    "Promenade - Assassin's Dagger Blueprint":           DeadCellsLocationData(45_100_102, "Promenade",           None),
    "Promenade - Explosive Crossbow Blueprint":          DeadCellsLocationData(45_100_103, "Promenade",           None),
    "Promenade - Vine Rune Pedestal":                    DeadCellsLocationData(45_100_104, "Promenade",           None),
    # Toxic Sewers
    "Toxic Sewers - Teleportation Rune Pedestal":        DeadCellsLocationData(45_100_105, "Toxic Sewers",        None),
    # Ramparts
    "Ramparts - Stun Grenade Blueprint":                 DeadCellsLocationData(45_100_106, "Ramparts",            None),
    "Ramparts - Nerves of Steel Blueprint":              DeadCellsLocationData(45_100_107, "Ramparts",            None),
    "Ramparts - Challenger Rune Pedestal":               DeadCellsLocationData(45_100_108, "Ramparts",            None),
    # Ossuary
    "Ossuary - Ram Rune Pedestal":                       DeadCellsLocationData(45_100_109, "Ossuary",             None),
    # Ancient Sewers
    "Ancient Sewers - Aura of Laceration Blueprint":     DeadCellsLocationData(45_100_110, "Ancient Sewers",      None),
    # Insufferable Crypt
    "Insufferable Crypt - Tonic Blueprint":              DeadCellsLocationData(45_100_111, "Insufferable Crypt",  None),
    # Slumbering Sanctuary
    "Slumbering Sanctuary - Spider Rune Pedestal":       DeadCellsLocationData(45_100_112, "Slumbering Sanctuary", None),
    "Slumbering Sanctuary - Crow's Wings Blueprint":     DeadCellsLocationData(45_100_113, "Slumbering Sanctuary", None),
    # Graveyard
    "Graveyard - Punishment Blueprint":                  DeadCellsLocationData(45_100_114, "Graveyard",           None),
    # Prison Depths
    "Prison Depths - Hayabusa Boots Blueprint":          DeadCellsLocationData(45_100_115, "Prison Depths",       None),
    # Fog Fjord / Forgotten Sepulcher
    "Forgotten Sepulcher - Explorer Rune Pedestal":      DeadCellsLocationData(45_100_116, "Forgotten Sepulcher", None),
    "Forgotten Sepulcher - Death Orb Blueprint":         DeadCellsLocationData(45_100_117, "Forgotten Sepulcher", None),
    # Clock Tower
    "Clock Tower - Heavy Grenade Blueprint":             DeadCellsLocationData(45_100_118, "Clock Tower",         None),
    # High Peak Castle
    "High Peak Castle - Homunculus Rune Pedestal":       DeadCellsLocationData(45_100_119, "High Peak Castle",    None),
    # Throne Room passage (after first HotK kill)
    "Throne Room Passage - Ivy Grenade Blueprint":       DeadCellsLocationData(45_100_120, "Throne Room",         None),
}

# ── DLC locations ─────────────────────────────────────────────────────────────

DLC_LOCATIONS: Dict[str, DeadCellsLocationData] = {
    # The Bad Seed
    "Dilapidated Arboretum - Bronze Door":      DeadCellsLocationData(45_100_200, "Dilapidated Arboretum", "dlc_the_bad_seed"),
    "Morass of the Banished - Bronze Door":     DeadCellsLocationData(45_100_201, "Morass",                "dlc_the_bad_seed"),
    "Morass of the Banished - Silver Door":     DeadCellsLocationData(45_100_202, "Morass",                "dlc_the_bad_seed"),
    # Fatal Falls
    "Fractured Shrines - Bronze Door":          DeadCellsLocationData(45_100_210, "Fractured Shrines",     "dlc_fatal_falls"),
    "Fractured Shrines - Silver Door":          DeadCellsLocationData(45_100_211, "Fractured Shrines",     "dlc_fatal_falls"),
    "Undying Shores - Bronze Door":             DeadCellsLocationData(45_100_212, "Undying Shores",        "dlc_fatal_falls"),
    "Undying Shores - Silver Door":             DeadCellsLocationData(45_100_213, "Undying Shores",        "dlc_fatal_falls"),
    # Rise of the Giant
    "Cavern - Bronze Door":                     DeadCellsLocationData(45_100_220, "Cavern",                "dlc_rise_of_the_giant"),
    "Cavern - Silver Door":                     DeadCellsLocationData(45_100_221, "Cavern",                "dlc_rise_of_the_giant"),
    "Astrolab - Bronze Door":                   DeadCellsLocationData(45_100_222, "Astrolab",              "dlc_rise_of_the_giant"),
    "Astrolab - Silver Door":                   DeadCellsLocationData(45_100_223, "Astrolab",              "dlc_rise_of_the_giant"),
    # The Queen and the Sea
    "Infested Shipwreck - Bronze Door":         DeadCellsLocationData(45_100_230, "Infested Shipwreck",    "dlc_queen_and_the_sea"),
    "Infested Shipwreck - Silver Door":         DeadCellsLocationData(45_100_231, "Infested Shipwreck",    "dlc_queen_and_the_sea"),
    "Lighthouse - Bronze Door":                 DeadCellsLocationData(45_100_232, "Lighthouse",            "dlc_queen_and_the_sea"),
}

# ── Elite kill locations ──────────────────────────────────────────────────────
# One location per enemy type that can spawn as an elite (source: the Dead Cells
# wiki "Enemies" page, "Elite?" = Yes). Killing ANY elite of that type counts.
#
# Region = the region of the enemy's biomes that needs the fewest runes to reach
# (base-game biomes are preferred; DLC-only enemies sit in their DLC region and
# also require that DLC option). Left out on purpose: Return to Castlevania
# enemies, The Bank / Cursed-biome enemies, spoilered Astrolab enemies and
# Rampager (no fixed biome) - none of those have a region in this APWorld.
#
# Gated behind the `elite_checks` option. IDs must stay in sync with the mod's
# EliteLocationIds table (GameHooks/CheckSender.cs).

ELITE_LOCATIONS: Dict[str, DeadCellsLocationData] = {
    "Defeat Elite Zombie": DeadCellsLocationData(45_100_300, "Prisoners' Quarters", None, "elite_checks"),
    "Defeat Elite Undead Archer": DeadCellsLocationData(45_100_301, "Prisoners' Quarters", None, "elite_checks"),
    "Defeat Elite Shieldbearer": DeadCellsLocationData(45_100_302, "Prisoners' Quarters", None, "elite_checks"),
    "Defeat Elite Grenadier": DeadCellsLocationData(45_100_303, "Prisoners' Quarters", None, "elite_checks"),
    "Defeat Elite Bombardier": DeadCellsLocationData(45_100_304, "Promenade", None, "elite_checks"),
    "Defeat Elite Runner": DeadCellsLocationData(45_100_305, "Promenade", None, "elite_checks"),
    "Defeat Elite Inquisitor": DeadCellsLocationData(45_100_306, "Prisoners' Quarters", None, "elite_checks"),
    "Defeat Elite Hammer": DeadCellsLocationData(45_100_307, "Derelict Distillery", None, "elite_checks"),
    "Defeat Elite Sweeper": DeadCellsLocationData(45_100_308, "Ramparts", None, "elite_checks"),
    "Defeat Elite Festering Zombie": DeadCellsLocationData(45_100_309, "Stilt Village", None, "elite_checks"),
    "Defeat Elite Swarm Zombie": DeadCellsLocationData(45_100_310, "Graveyard", None, "elite_checks"),
    "Defeat Elite Disgusting Worm": DeadCellsLocationData(45_100_311, "Toxic Sewers", None, "elite_checks"),
    "Defeat Elite Scorpion": DeadCellsLocationData(45_100_312, "Toxic Sewers", None, "elite_checks"),
    "Defeat Elite Catcher": DeadCellsLocationData(45_100_313, "Graveyard", None, "elite_checks"),
    "Defeat Elite Cleaver": DeadCellsLocationData(45_100_314, "Forgotten Sepulcher", None, "elite_checks"),
    "Defeat Elite Pirate Captain": DeadCellsLocationData(45_100_315, "Stilt Village", None, "elite_checks"),
    "Defeat Elite Knife Thrower": DeadCellsLocationData(45_100_316, "Prisoners' Quarters", None, "elite_checks"),
    "Defeat Elite Slasher": DeadCellsLocationData(45_100_317, "Ramparts", None, "elite_checks"),
    "Defeat Elite Lacerator": DeadCellsLocationData(45_100_318, "Derelict Distillery", None, "elite_checks"),
    "Defeat Elite Thorny": DeadCellsLocationData(45_100_319, "High Peak Castle", None, "elite_checks"),
    "Defeat Elite Caster": DeadCellsLocationData(45_100_320, "Slumbering Sanctuary", None, "elite_checks"),
    "Defeat Elite Golem": DeadCellsLocationData(45_100_321, "Slumbering Sanctuary", None, "elite_checks"),
    "Defeat Elite Dark Tracker": DeadCellsLocationData(45_100_322, "Promenade", None, "elite_checks"),
    "Defeat Elite Cannibal": DeadCellsLocationData(45_100_323, "Clock Tower", None, "elite_checks"),
    "Defeat Elite Lancer": DeadCellsLocationData(45_100_324, "High Peak Castle", None, "elite_checks"),
    "Defeat Elite Royal Guard": DeadCellsLocationData(45_100_325, "High Peak Castle", None, "elite_checks"),
    "Defeat Elite Bomber": DeadCellsLocationData(45_100_326, "Ossuary", None, "elite_checks"),
    "Defeat Elite Slammer": DeadCellsLocationData(45_100_327, "Corrupted Prison", None, "elite_checks"),
    "Defeat Elite Demon": DeadCellsLocationData(45_100_328, "High Peak Castle", None, "elite_checks"),
    "Defeat Elite Failed Experiment": DeadCellsLocationData(45_100_329, "Prisoners' Quarters", None, "elite_checks"),
    "Defeat Elite Oven Knight": DeadCellsLocationData(45_100_330, "Prisoners' Quarters", None, "elite_checks"),
    "Defeat Elite Toxic Miasma": DeadCellsLocationData(45_100_331, "Corrupted Prison", None, "elite_checks"),
    "Defeat Elite Weirded Warrior": DeadCellsLocationData(45_100_332, "Stilt Village", None, "elite_checks"),
    "Defeat Elite Corpulent Zombie": DeadCellsLocationData(45_100_333, "Forgotten Sepulcher", None, "elite_checks"),
    "Defeat Elite Dancer": DeadCellsLocationData(45_100_334, "Slumbering Sanctuary", None, "elite_checks"),
    "Defeat Elite Infected Worker": DeadCellsLocationData(45_100_335, "Derelict Distillery", None, "elite_checks"),
    "Defeat Elite Living Barrel": DeadCellsLocationData(45_100_336, "Derelict Distillery", None, "elite_checks"),
    "Defeat Elite Demolisher": DeadCellsLocationData(45_100_337, "Prisoners' Quarters", None, "elite_checks"),
    "Defeat Elite Arbiter": DeadCellsLocationData(45_100_338, "Cavern", "dlc_rise_of_the_giant", "elite_checks"),
    "Defeat Elite Ground Shaker": DeadCellsLocationData(45_100_339, "Cavern", "dlc_rise_of_the_giant", "elite_checks"),
    "Defeat Elite Yeeter": DeadCellsLocationData(45_100_340, "Dilapidated Arboretum", "dlc_the_bad_seed", "elite_checks"),
    "Defeat Elite Giant Tick": DeadCellsLocationData(45_100_341, "Morass", "dlc_the_bad_seed", "elite_checks"),
    "Defeat Elite Stone Warden": DeadCellsLocationData(45_100_342, "Fractured Shrines", "dlc_fatal_falls", "elite_checks"),
    "Defeat Elite Cold Blooded Guardian": DeadCellsLocationData(45_100_343, "Fractured Shrines", "dlc_fatal_falls", "elite_checks"),
    "Defeat Elite Mutineer": DeadCellsLocationData(45_100_344, "Infested Shipwreck", "dlc_queen_and_the_sea", "elite_checks"),
    "Defeat Elite Armored Shrimp": DeadCellsLocationData(45_100_345, "Infested Shipwreck", "dlc_queen_and_the_sea", "elite_checks"),
}

# ── Master lookup ─────────────────────────────────────────────────────────────

ALL_LOCATIONS: Dict[str, DeadCellsLocationData] = {
    **BOSS_LOCATIONS,
    **TIMED_DOOR_LOCATIONS,
    **BLUEPRINT_LOCATIONS,
    **DLC_LOCATIONS,
    **ELITE_LOCATIONS,
}

# ID → name reverse lookup (used by the client)
LOCATION_ID_TO_NAME: Dict[int, str] = {
    data.code: name
    for name, data in ALL_LOCATIONS.items()
    if data.code is not None
}
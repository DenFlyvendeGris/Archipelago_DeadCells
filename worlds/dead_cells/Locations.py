"""
Dead Cells APWorld — locations.py

Defines every location that can hold a multiworld item.

ID base: 45_100_000
  Boss kills:          45_100_001 – 45_100_049
  Timed door chests:   45_100_050 – 45_100_099
  Blueprint pickups:   45_100_100 – 45_100_199
  DLC locations:       45_100_200 – 45_100_299
"""

from typing import Dict, NamedTuple, Optional


class DeadCellsLocationData(NamedTuple):
    code: Optional[int]   # None = event location
    region: str           # which Region this location belongs to
    dlc: Optional[str]    # None = base game; otherwise the DLC option name


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

# ── Master lookup ─────────────────────────────────────────────────────────────

ALL_LOCATIONS: Dict[str, DeadCellsLocationData] = {
    **BOSS_LOCATIONS,
    **TIMED_DOOR_LOCATIONS,
    **BLUEPRINT_LOCATIONS,
    **DLC_LOCATIONS,
}

# ID → name reverse lookup (used by the client)
LOCATION_ID_TO_NAME: Dict[int, str] = {
    data.code: name
    for name, data in ALL_LOCATIONS.items()
    if data.code is not None
}
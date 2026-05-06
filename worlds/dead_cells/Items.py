"""
Dead Cells APWorld — items.py

Defines every item that can exist in the multiworld pool, along with its
unique ID and ItemClassification.

ID base: 45_000_000
  Runes:          45_000_001 – 45_000_008
  BSC upgrades:   45_000_010 – 45_000_014
  Scrolls:        45_000_020 – 45_000_022
  Blueprints:     45_000_100 – 45_000_399  (base) / 45_000_400 – 45_000_499 (DLC)
  Filler:         45_000_900 – 45_000_909
  Traps:          45_000_950 – 45_000_959
"""

from typing import Dict, NamedTuple, Optional
from BaseClasses import ItemClassification


class DeadCellsItemData(NamedTuple):
    code: Optional[int]                  # None = event item
    classification: ItemClassification


# Convenience aliases
prog   = ItemClassification.progression
useful = ItemClassification.useful
filler = ItemClassification.filler
trap   = ItemClassification.trap


# ── Runes ─────────────────────────────────────────────────────────────────────
# All runes are progression — they gate regions.

RUNE_ITEMS: Dict[str, DeadCellsItemData] = {
    "Vine Rune":          DeadCellsItemData(45_000_001, prog),
    "Teleportation Rune": DeadCellsItemData(45_000_002, prog),
    "Ram Rune":           DeadCellsItemData(45_000_003, prog),
    "Spider Rune":        DeadCellsItemData(45_000_004, prog),
    "Challenger Rune":    DeadCellsItemData(45_000_005, useful),  # unlocks daily challenges
    "Homunculus Rune":    DeadCellsItemData(45_000_006, prog),
    "Explorer Rune":      DeadCellsItemData(45_000_007, useful),  # map reveal only
    "Custom Mode Rune":   DeadCellsItemData(45_000_008, useful),  # unlocks custom mode
}

# ── Boss Stem Cells ───────────────────────────────────────────────────────────
# Progression — they gate difficulty tiers and some biome entrances.

BSC_ITEMS: Dict[str, DeadCellsItemData] = {
    "Boss Stem Cell 1":   DeadCellsItemData(45_000_010, prog),
    "Boss Stem Cell 2":   DeadCellsItemData(45_000_011, prog),
    "Boss Stem Cell 3":   DeadCellsItemData(45_000_012, prog),
    "Boss Stem Cell 4":   DeadCellsItemData(45_000_013, prog),
    "Boss Stem Cell 5":   DeadCellsItemData(45_000_014, prog),
}

# ── Scrolls ───────────────────────────────────────────────────────────────────
# Useful — they're meaningful power boosts but don't gate any region.

SCROLL_ITEMS: Dict[str, DeadCellsItemData] = {
    "Power Scroll":       DeadCellsItemData(45_000_020, useful),
    "Dual Scroll":        DeadCellsItemData(45_000_021, useful),
    "Cursed Scroll":      DeadCellsItemData(45_000_022, useful),
}

# ── Base-game blueprints ──────────────────────────────────────────────────────
# All blueprints are useful — they expand the player's weapon/skill options.
# Names match exactly what the DCCM in-game mod will report.

BLUEPRINT_ITEMS: Dict[str, DeadCellsItemData] = {
    # Melee weapons — IDs 45_000_100–45_000_129
    "Blueprint: Broadsword":             DeadCellsItemData(45_000_100, useful),
    "Blueprint: Assassin's Dagger":      DeadCellsItemData(45_000_101, useful),
    "Blueprint: Blood Sword":            DeadCellsItemData(45_000_102, useful),
    "Blueprint: Cursed Sword":           DeadCellsItemData(45_000_103, useful),
    "Blueprint: Frantic Sword":          DeadCellsItemData(45_000_104, useful),
    "Blueprint: Meat Skewer":            DeadCellsItemData(45_000_105, useful),
    "Blueprint: Dagger of the Sadist":   DeadCellsItemData(45_000_106, useful),
    "Blueprint: Hayabusa Boots":         DeadCellsItemData(45_000_107, useful),
    "Blueprint: Rapier":                 DeadCellsItemData(45_000_108, useful),
    "Blueprint: Valmont's Whip":         DeadCellsItemData(45_000_109, useful),
    "Blueprint: Spite Sword":            DeadCellsItemData(45_000_110, useful),
    "Blueprint: Frostbite":              DeadCellsItemData(45_000_111, useful),
    "Blueprint: Oven Axe":              DeadCellsItemData(45_000_112, useful),
    "Blueprint: Spartan Sandals":        DeadCellsItemData(45_000_113, useful),
    "Blueprint: Great Owl of War":       DeadCellsItemData(45_000_114, useful),
    "Blueprint: Crowbar":                DeadCellsItemData(45_000_115, useful),
    "Blueprint: Lightning Bolt":         DeadCellsItemData(45_000_116, useful),

    # Ranged weapons — IDs 45_000_130–45_000_149
    "Blueprint: Quick Bow":              DeadCellsItemData(45_000_130, useful),
    "Blueprint: Infantry Bow":           DeadCellsItemData(45_000_131, useful),
    "Blueprint: Ice Bow":                DeadCellsItemData(45_000_132, useful),
    "Blueprint: Hokuto's Bow":           DeadCellsItemData(45_000_133, useful),
    "Blueprint: Nerves of Steel":        DeadCellsItemData(45_000_134, useful),
    "Blueprint: Explosive Crossbow":     DeadCellsItemData(45_000_135, useful),
    "Blueprint: Double Crossb-o-matic":  DeadCellsItemData(45_000_136, useful),
    "Blueprint: Bow and Endless Quiver": DeadCellsItemData(45_000_137, useful),

    # Shields — IDs 45_000_150–45_000_159
    "Blueprint: Blood Shield":           DeadCellsItemData(45_000_150, useful),
    "Blueprint: Force Shield":           DeadCellsItemData(45_000_151, useful),
    "Blueprint: Front Line Shield":      DeadCellsItemData(45_000_152, useful),
    "Blueprint: Spiked Shield":          DeadCellsItemData(45_000_153, useful),
    "Blueprint: Rampart":                DeadCellsItemData(45_000_154, useful),
    "Blueprint: Punishment":             DeadCellsItemData(45_000_155, useful),
    "Blueprint: Shove Shield":           DeadCellsItemData(45_000_156, useful),
    "Blueprint: Counter Shield":         DeadCellsItemData(45_000_157, useful),

    # Grenades — IDs 45_000_160–45_000_174
    "Blueprint: Fire Grenade":           DeadCellsItemData(45_000_160, useful),
    "Blueprint: Magnetic Grenade":       DeadCellsItemData(45_000_161, useful),
    "Blueprint: Oil Grenade":            DeadCellsItemData(45_000_162, useful),
    "Blueprint: Ivy Grenade":            DeadCellsItemData(45_000_163, useful),
    "Blueprint: Heavy Grenade":          DeadCellsItemData(45_000_164, useful),
    "Blueprint: Stun Grenade":           DeadCellsItemData(45_000_165, useful),
    "Blueprint: Cluster Grenade":        DeadCellsItemData(45_000_166, useful),

    # Skills / powers — IDs 45_000_175–45_000_199
    "Blueprint: Toxic Cloud":            DeadCellsItemData(45_000_175, useful),
    "Blueprint: Vampirism":              DeadCellsItemData(45_000_176, useful),
    "Blueprint: Grappling Hook":         DeadCellsItemData(45_000_177, useful),
    "Blueprint: Knife Storm":            DeadCellsItemData(45_000_178, useful),
    "Blueprint: Phaser":                 DeadCellsItemData(45_000_179, useful),
    "Blueprint: Tonic":                  DeadCellsItemData(45_000_180, useful),
    "Blueprint: Crow's Wings":           DeadCellsItemData(45_000_181, useful),
    "Blueprint: Death Orb":              DeadCellsItemData(45_000_182, useful),
    "Blueprint: Corrupted Power":        DeadCellsItemData(45_000_183, useful),
    "Blueprint: Aura of Laceration":     DeadCellsItemData(45_000_184, useful),
    "Blueprint: Denial Wave":            DeadCellsItemData(45_000_185, useful),

    # Turrets / traps — IDs 45_000_200–45_000_214
    "Blueprint: Flamethrower Turret":    DeadCellsItemData(45_000_200, useful),
    "Blueprint: Ceiling Turret":         DeadCellsItemData(45_000_201, useful),
    "Blueprint: Heavy Turret":           DeadCellsItemData(45_000_202, useful),
    "Blueprint: Crusher":                DeadCellsItemData(45_000_203, useful),
    "Blueprint: Explosive Lure":         DeadCellsItemData(45_000_204, useful),

    # Key mutations (Brutality) — IDs 45_000_215–45_000_229
    "Blueprint: Predator":               DeadCellsItemData(45_000_215, useful),
    "Blueprint: Vengeance":              DeadCellsItemData(45_000_216, useful),
    "Blueprint: Berserker":              DeadCellsItemData(45_000_217, useful),
    "Blueprint: Adrenaline":             DeadCellsItemData(45_000_218, useful),
    "Blueprint: Soldier's Resistance":   DeadCellsItemData(45_000_219, useful),

    # Key mutations (Tactics) — IDs 45_000_230–45_000_244
    "Blueprint: Swarm":                  DeadCellsItemData(45_000_230, useful),
    "Blueprint: Scheme":                 DeadCellsItemData(45_000_231, useful),
    "Blueprint: Porcupack":              DeadCellsItemData(45_000_232, useful),
    "Blueprint: Predator":               DeadCellsItemData(45_000_233, useful),

    # Key mutations (Survival) — IDs 45_000_245–45_000_259
    "Blueprint: What Doesn't Kill Me":   DeadCellsItemData(45_000_245, useful),
    "Blueprint: Soldier's Resistance":   DeadCellsItemData(45_000_246, useful),
    "Blueprint: Kill Rhythm":            DeadCellsItemData(45_000_247, useful),
    "Blueprint: No Mercy":               DeadCellsItemData(45_000_248, useful),
    "Blueprint: Disengagement":          DeadCellsItemData(45_000_249, useful),
}

# ── DLC blueprints ────────────────────────────────────────────────────────────
# Only injected into the pool when the relevant DLC toggle is enabled.
# IDs 45_000_300–45_000_499

DLC_BLUEPRINT_ITEMS: Dict[str, DeadCellsItemData] = {
    # Rise of the Giant — 45_000_300–45_000_319
    "Blueprint: Giant Killer":           DeadCellsItemData(45_000_300, useful),
    "Blueprint: Hemorrhage":             DeadCellsItemData(45_000_301, useful),

    # The Bad Seed — 45_000_320–45_000_339
    "Blueprint: Cocoon":                 DeadCellsItemData(45_000_320, useful),
    "Blueprint: Scythe Claws":           DeadCellsItemData(45_000_321, useful),

    # Fatal Falls — 45_000_340–45_000_359
    "Blueprint: Serenade":               DeadCellsItemData(45_000_340, useful),
    "Blueprint: Castlevania":            DeadCellsItemData(45_000_341, useful),

    # The Queen and the Sea — 45_000_360–45_000_379
    "Blueprint: Pirate Captain's Sword": DeadCellsItemData(45_000_360, useful),
    "Blueprint: Wrecking Ball":          DeadCellsItemData(45_000_361, useful),
}

# ── Filler items ──────────────────────────────────────────────────────────────

FILLER_ITEMS: Dict[str, DeadCellsItemData] = {
    "Small Gold Pouch":   DeadCellsItemData(45_000_900, filler),
    "Large Gold Pouch":   DeadCellsItemData(45_000_901, filler),
}

# ── Trap items ────────────────────────────────────────────────────────────────

TRAP_ITEMS: Dict[str, DeadCellsItemData] = {
    "Curse Trap":   DeadCellsItemData(45_000_950, trap),
    "Malaise Trap": DeadCellsItemData(45_000_951, trap),
}

# ── Master lookup ─────────────────────────────────────────────────────────────
# Combines all item dicts for easy access from __init__.py.

ALL_ITEMS: Dict[str, DeadCellsItemData] = {
    **RUNE_ITEMS,
    **BSC_ITEMS,
    **SCROLL_ITEMS,
    **BLUEPRINT_ITEMS,
    **DLC_BLUEPRINT_ITEMS,
    **FILLER_ITEMS,
    **TRAP_ITEMS,
}

# ID → name reverse lookup (used by the client)
ITEM_ID_TO_NAME: Dict[int, str] = {
    data.code: name
    for name, data in ALL_ITEMS.items()
    if data.code is not None
}
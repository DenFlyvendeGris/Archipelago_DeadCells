"""
Dead Cells APWorld — rules.py

All region and location access rules.

Rules are plain functions that take (state, player) and return bool.
They are composed bottom-up: early-game helpers feed into mid-game
helpers, which feed into late-game helpers. This avoids copy-paste
and makes logic changes easy to propagate.

Usage from __init__.py:
    from .rules import set_rules
    set_rules(self.multiworld, self.player, self.options)
"""

from worlds.AutoWorld import World
from BaseClasses import MultiWorld, CollectionState
from .DeadCellsOptions import DeadCellsOptions, Goal


# ── Rune helpers ──────────────────────────────────────────────────────────────

def _has_vine(state: CollectionState, player: int) -> bool:
    return state.has("Vine Rune", player)

def _has_teleport(state: CollectionState, player: int) -> bool:
    return state.has("Teleportation Rune", player)

def _has_ram(state: CollectionState, player: int) -> bool:
    return state.has("Ram Rune", player)

def _has_spider(state: CollectionState, player: int) -> bool:
    return state.has("Spider Rune", player)

def _has_homunculus(state: CollectionState, player: int) -> bool:
    return state.has("Homunculus Rune", player)


# ── BSC helpers ───────────────────────────────────────────────────────────────

def _has_bsc(state: CollectionState, player: int, count: int) -> bool:
    """True if the player has received at least `count` BSC items."""
    return (
        state.has("Boss Stem Cell 1", player) +
        state.has("Boss Stem Cell 2", player) +
        state.has("Boss Stem Cell 3", player) +
        state.has("Boss Stem Cell 4", player) +
        state.has("Boss Stem Cell 5", player)
    ) >= count


# ── Stage 2 region rules ──────────────────────────────────────────────────────

def _can_reach_promenade(state: CollectionState, player: int) -> bool:
    return True  # Always accessible from Prisoners' Quarters


def _can_reach_toxic_sewers(state: CollectionState, player: int) -> bool:
    return _has_vine(state, player)


def _can_reach_arboretum(state: CollectionState, player: int) -> bool:
    # DLC: The Bad Seed — requires Teleportation Rune from PQ
    return _has_teleport(state, player)


# ── Stage 3 region rules ──────────────────────────────────────────────────────

def _can_reach_ramparts(state: CollectionState, player: int) -> bool:
    # Free from Promenade (no rune) or from Toxic Sewers (no extra rune)
    return (
        _can_reach_promenade(state, player) or
        _can_reach_toxic_sewers(state, player)
    )


def _can_reach_ossuary(state: CollectionState, player: int) -> bool:
    # Promenade → Ossuary requires Teleportation Rune
    return _can_reach_promenade(state, player) and _has_teleport(state, player)


def _can_reach_ancient_sewers(state: CollectionState, player: int) -> bool:
    # Toxic Sewers → Ancient Sewers requires Ram Rune
    return _can_reach_toxic_sewers(state, player) and _has_ram(state, player)


def _can_reach_morass(state: CollectionState, player: int) -> bool:
    # DLC: The Bad Seed — from Arboretum
    return _can_reach_arboretum(state, player)


# ── Boss 1 arena rules ────────────────────────────────────────────────────────

def _can_reach_black_bridge(state: CollectionState, player: int) -> bool:
    return _can_reach_ramparts(state, player)


def _can_reach_insufferable_crypt(state: CollectionState, player: int) -> bool:
    # Accessible via Ossuary OR Ancient Sewers
    return (
        _can_reach_ossuary(state, player) or
        _can_reach_ancient_sewers(state, player)
    )


def _can_reach_nest(state: CollectionState, player: int) -> bool:
    # DLC: The Bad Seed
    return _can_reach_morass(state, player)


# ── Stage 4 region rules ──────────────────────────────────────────────────────

def _can_reach_stilt_village(state: CollectionState, player: int) -> bool:
    return _can_reach_black_bridge(state, player)


def _can_reach_slumbering_sanctuary(state: CollectionState, player: int) -> bool:
    # Insufferable Crypt → Slumbering Sanctuary requires Spider Rune
    return _can_reach_insufferable_crypt(state, player) and _has_spider(state, player)


def _can_reach_graveyard(state: CollectionState, player: int) -> bool:
    # Stilt Village → Graveyard requires Spider Rune
    return _can_reach_stilt_village(state, player) and _has_spider(state, player)


def _can_reach_fractured_shrines(state: CollectionState, player: int) -> bool:
    # DLC: Fatal Falls — unlocked after Black Bridge
    return _can_reach_black_bridge(state, player)


# ── Stage 5 region rules ──────────────────────────────────────────────────────

def _can_reach_clock_tower(state: CollectionState, player: int) -> bool:
    # Multiple stage-4 paths lead here
    return (
        _can_reach_stilt_village(state, player) or
        _can_reach_slumbering_sanctuary(state, player) or
        _can_reach_graveyard(state, player)
    )


def _can_reach_forgotten_sepulcher(state: CollectionState, player: int) -> bool:
    # Requires Teleportation Rune to enter
    return _can_reach_clock_tower(state, player) and _has_teleport(state, player)


def _can_reach_cavern(state: CollectionState, player: int) -> bool:
    # DLC: Rise of the Giant — requires Homunculus Rune
    return _has_homunculus(state, player)


def _can_reach_undying_shores(state: CollectionState, player: int) -> bool:
    # DLC: The Queen and the Sea — unlocked after Black Bridge
    return _can_reach_black_bridge(state, player)


# ── Boss 2 arena rules ────────────────────────────────────────────────────────

def _can_reach_clock_room(state: CollectionState, player: int) -> bool:
    return _can_reach_clock_tower(state, player)


def _can_reach_guardians_haven(state: CollectionState, player: int) -> bool:
    # DLC: Rise of the Giant — via Cavern
    return _can_reach_cavern(state, player)


def _can_reach_mausoleum(state: CollectionState, player: int) -> bool:
    # DLC: Fatal Falls — via Fractured Shrines
    return _can_reach_fractured_shrines(state, player)


# ── Stage 6 region rules ──────────────────────────────────────────────────────

def _can_reach_high_peak_castle(state: CollectionState, player: int) -> bool:
    return _can_reach_clock_room(state, player)


def _can_reach_distillery(state: CollectionState, player: int) -> bool:
    return _can_reach_clock_room(state, player)


def _can_reach_infested_shipwreck(state: CollectionState, player: int) -> bool:
    # DLC: The Queen and the Sea — via Undying Shores
    return _can_reach_undying_shores(state, player)


# ── Endgame region rules ──────────────────────────────────────────────────────

def _can_reach_throne_room(state: CollectionState, player: int) -> bool:
    return (
        _can_reach_high_peak_castle(state, player) or
        _can_reach_distillery(state, player)
    )


def _can_reach_lighthouse(state: CollectionState, player: int) -> bool:
    # DLC: The Queen and the Sea
    return _can_reach_infested_shipwreck(state, player)


def _can_reach_astrolab(state: CollectionState, player: int) -> bool:
    # True ending path: must have beaten HotK once (reached Throne Room)
    # AND have Homunculus Rune AND have beaten the Giant
    return (
        _can_reach_throne_room(state, player) and
        _can_reach_guardians_haven(state, player) and
        _has_homunculus(state, player)
    )


# ── Goal completion checks ────────────────────────────────────────────────────

def _goal_hand_of_the_king(state: CollectionState, player: int) -> bool:
    return _can_reach_throne_room(state, player)


def _goal_the_collector(state: CollectionState, player: int) -> bool:
    return _can_reach_astrolab(state, player)


def _goal_target_bsc(state: CollectionState, player: int, target: int) -> bool:
    return _has_bsc(state, player, target)


# ── Main entry point ──────────────────────────────────────────────────────────

def set_rules(multiworld: MultiWorld, player: int, options: DeadCellsOptions) -> None:
    """
    Attach access rules to all entrances and locations for this player.
    Called from DeadCellsWorld.set_rules() in __init__.py.
    """

    # Helper: shorthand for setting an entrance rule
    def entrance(source: str, target: str, rule):
        ent = multiworld.get_entrance(f"{source} -> {target}", player)
        ent.access_rule = rule

    # ── Base game entrance rules ───────────────────────────────────────────────
    entrance("Menu", "Prisoners' Quarters", lambda s: True)
    entrance("Prisoners' Quarters", "Promenade", lambda s: True)
    entrance("Prisoners' Quarters", "Toxic Sewers", lambda s: _has_vine(s, player))
    entrance("Promenade", "Ramparts", lambda s: True)
    entrance("Promenade", "Ossuary", lambda s: _has_teleport(s, player))
    entrance("Promenade", "Prison Depths", lambda s: _has_spider(s, player))
    entrance("Toxic Sewers", "Ramparts", lambda s: True)
    entrance("Toxic Sewers", "Ancient Sewers", lambda s: _has_ram(s, player))
    entrance("Toxic Sewers", "Corrupted Prison", lambda s: _has_spider(s, player))
    entrance("Ramparts", "Black Bridge", lambda s: True)
    entrance("Ossuary", "Insufferable Crypt", lambda s: True)
    entrance("Ancient Sewers", "Insufferable Crypt", lambda s: True)
    entrance("Black Bridge", "Stilt Village", lambda s: True)
    entrance("Insufferable Crypt", "Slumbering Sanctuary", lambda s: _has_spider(s, player))
    entrance("Stilt Village", "Graveyard", lambda s: _has_spider(s, player))
    entrance("Stilt Village", "Clock Tower", lambda s: True)
    entrance("Slumbering Sanctuary", "Clock Tower", lambda s: True)
    entrance("Graveyard", "Clock Tower", lambda s: True)
    entrance("Clock Tower", "Forgotten Sepulcher", lambda s: _has_teleport(s, player))
    entrance("Clock Tower", "Clock Room", lambda s: True)
    entrance("Forgotten Sepulcher", "Clock Room", lambda s: True)
    entrance("Clock Room", "High Peak Castle", lambda s: True)
    entrance("Clock Room", "Derelict Distillery", lambda s: True)
    entrance("High Peak Castle", "Throne Room", lambda s: True)
    entrance("Derelict Distillery", "Throne Room", lambda s: True)

    # ── DLC entrance rules — only set if DLC is enabled ───────────────────────
    if options.dlc_the_bad_seed:
        entrance("Prisoners' Quarters", "Dilapidated Arboretum", lambda s: _has_teleport(s, player))
        entrance("Dilapidated Arboretum", "Morass", lambda s: True)
        entrance("Morass", "Nest", lambda s: True)
        entrance("Nest", "Stilt Village", lambda s: True)

    if options.dlc_fatal_falls:
        entrance("Black Bridge", "Fractured Shrines", lambda s: True)
        entrance("Fractured Shrines", "Undying Shores", lambda s: True)
        entrance("Undying Shores", "Mausoleum", lambda s: True)
        entrance("Mausoleum", "Clock Tower", lambda s: True)

    if options.dlc_rise_of_the_giant:
        entrance("Prisoners' Quarters", "Cavern", lambda s: _has_homunculus(s, player))
        entrance("Cavern", "Guardian's Haven", lambda s: True)
        entrance("Guardian's Haven", "Astrolab",
                 lambda s: _can_reach_throne_room(s, player) and _has_homunculus(s, player))
        entrance("Astrolab", "Collector's Lair", lambda s: True)

    if options.dlc_queen_and_the_sea:
        entrance("Black Bridge", "Undying Shores", lambda s: True)
        entrance("Undying Shores", "Infested Shipwreck", lambda s: True)
        entrance("Infested Shipwreck", "Lighthouse", lambda s: True)

    # ── Victory condition ─────────────────────────────────────────────────────

    goal = options.goal.value

    if goal == Goal.option_hand_of_the_king:
        multiworld.completion_condition[player] = (
            lambda s: s.has("Victory", player)
        )

    elif goal == Goal.option_the_collector:
        multiworld.completion_condition[player] = (
            lambda s: s.has("Victory", player)
        )

    elif goal == Goal.option_target_bsc:
        target = options.target_bsc_level.value
        multiworld.completion_condition[player] = (
            lambda s, t=target: _has_bsc(s, player, t)
        )
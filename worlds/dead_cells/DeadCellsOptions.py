"""
Dead Cells APWorld — DeadCellsOptions.py

Named DeadCellsOptions.py (NOT Options.py) to avoid clashing
with Archipelago's own top-level Options.py file.
"""

from dataclasses import dataclass
from Options import Choice, DefaultOnToggle, Range, Toggle, PerGameCommonOptions


class Goal(Choice):
    """Determines the victory condition for this randomizer run.

    - **hand_of_the_king**: Defeat the Hand of the King. No DLC required. Default.
    - **the_collector**: Defeat the Collector. Requires Rise of the Giant DLC.
    - **target_bsc**: Collect a target number of Boss Stem Cells.
    """
    display_name = "Goal"
    rich_text_doc = True
    option_hand_of_the_king = 0
    option_the_collector = 1
    option_target_bsc = 2
    default = 0


class TargetBSCLevel(Range):
    """Number of Boss Stem Cells required to win. Only used when goal is target_bsc."""
    display_name = "Target BSC Level"
    range_start = 1
    range_end = 5
    default = 3


class DLCRiseOfTheGiant(Toggle):
    """Include Rise of the Giant DLC content. Required for the_collector goal."""
    display_name = "DLC: Rise of the Giant"


class DLCTheBadSeed(Toggle):
    """Include The Bad Seed DLC content."""
    display_name = "DLC: The Bad Seed"


class DLCFatalFalls(Toggle):
    """Include Fatal Falls DLC content."""
    display_name = "DLC: Fatal Falls"


class DLCQueenAndTheSea(Toggle):
    """Include The Queen and the Sea DLC content."""
    display_name = "DLC: The Queen and the Sea"


class ScrollShuffle(DefaultOnToggle):
    """Shuffle Power, Dual, and Cursed Scrolls into the multiworld item pool."""
    display_name = "Scroll Shuffle"


class BSCShuffle(DefaultOnToggle):
    """Shuffle all five Boss Stem Cell upgrades into the multiworld item pool."""
    display_name = "BSC Shuffle"


class TrapPercentage(Range):
    """Percentage of filler slots replaced with trap items. 0 disables traps."""
    display_name = "Trap Percentage"
    range_start = 0
    range_end = 50
    default = 10


class StartingWeapon(Choice):
    """The weapon the player starts each run with.

    - **any**: Chosen from received blueprints.
    - **rusty_sword**: Always the base Rusty Sword.
    """
    display_name = "Starting Weapon"
    rich_text_doc = True
    option_any = 0
    option_rusty_sword = 1
    default = 0


class BlueprintCount(Choice):
    """How many blueprints enter the pool.

    - **all**: Every blueprint subject to DLC toggles.
    - **subset**: Curated subset, no outfit blueprints.
    """
    display_name = "Blueprint Count"
    rich_text_doc = True
    option_all = 0
    option_subset = 1
    default = 1


@dataclass
class DeadCellsOptions(PerGameCommonOptions):
    goal:                   Goal
    target_bsc_level:       TargetBSCLevel
    dlc_rise_of_the_giant:  DLCRiseOfTheGiant
    dlc_the_bad_seed:       DLCTheBadSeed
    dlc_fatal_falls:        DLCFatalFalls
    dlc_queen_and_the_sea:  DLCQueenAndTheSea
    scroll_shuffle:         ScrollShuffle
    bsc_shuffle:            BSCShuffle
    trap_percentage:        TrapPercentage
    starting_weapon:        StartingWeapon
    blueprint_count:        BlueprintCount
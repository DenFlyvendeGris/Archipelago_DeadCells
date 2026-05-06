"""
Dead Cells APWorld — __init__.py
"""

from typing import Dict, Any, List

from BaseClasses import Item, ItemClassification, Region, Location, Tutorial
from worlds.AutoWorld import World, WebWorld
from Options import OptionError

from .DeadCellsOptions import DeadCellsOptions, Goal
from .Items import (
    ALL_ITEMS, RUNE_ITEMS, BSC_ITEMS, SCROLL_ITEMS,
    BLUEPRINT_ITEMS, DLC_BLUEPRINT_ITEMS, FILLER_ITEMS, TRAP_ITEMS,
    DeadCellsItemData,
)
from .Locations import ALL_LOCATIONS, DeadCellsLocationData
from .Rules import set_rules


class DeadCellsItem(Item):
    game = "Dead Cells"


class DeadCellsWebWorld(WebWorld):
    theme = "dirt"
    tutorials = [
        Tutorial(
            tutorial_name="Setup Guide",
            description="A guide to setting up Dead Cells Archipelago.",
            language="English",
            file_name="setup_en.md",
            link="setup/en",
            authors=["DenFlyvendeGris"],
        )
    ]


class DeadCellsWorld(World):
    """Dead Cells is a roguelite metroidvania by Motion Twin and Evil Empire.
    Fight through procedurally generated biomes, collect runes to unlock new
    paths, and defeat the Hand of the King — or beyond."""

    game = "Dead Cells"
    options_dataclass = DeadCellsOptions
    options: DeadCellsOptions
    web = DeadCellsWebWorld()

    item_name_to_id = {
        name: data.code
        for name, data in ALL_ITEMS.items()
        if data.code is not None
    }
    location_name_to_id = {
        name: data.code
        for name, data in ALL_LOCATIONS.items()
        if data.code is not None
    }

    def generate_early(self) -> None:
        # Validate: The Collector goal requires Rise of the Giant DLC
        if (self.options.goal == Goal.option_the_collector
                and not self.options.dlc_rise_of_the_giant):
            raise OptionError(
                f"[Dead Cells] Player {self.player_name}: goal 'the_collector' "
                f"requires 'dlc_rise_of_the_giant' to be enabled."
            )
        # Nudge Vine Rune into early sphere so the player isn't immediately locked
        self.multiworld.local_early_items[self.player]["Vine Rune"] = 1

    def create_item(self, name: str) -> DeadCellsItem:
        data = ALL_ITEMS[name]
        return DeadCellsItem(name, data.classification, data.code, self.player)

    def create_regions(self) -> None:
        # Build the list of region names based on enabled DLC
        region_names = [
            "Menu",
            "Prisoners' Quarters",
            "Promenade",
            "Toxic Sewers",
            "Prison Depths",
            "Corrupted Prison",
            "Ramparts",
            "Ossuary",
            "Ancient Sewers",
            "Black Bridge",
            "Insufferable Crypt",
            "Stilt Village",
            "Slumbering Sanctuary",
            "Graveyard",
            "Clock Tower",
            "Forgotten Sepulcher",
            "Clock Room",
            "High Peak Castle",
            "Derelict Distillery",
            "Throne Room",
        ]

        if self.options.dlc_the_bad_seed:
            region_names += ["Dilapidated Arboretum", "Morass", "Nest"]
        if self.options.dlc_fatal_falls:
            region_names += ["Fractured Shrines", "Undying Shores", "Mausoleum"]
        if self.options.dlc_rise_of_the_giant:
            region_names += ["Cavern", "Guardian's Haven", "Astrolab", "Collector's Lair"]
        if self.options.dlc_queen_and_the_sea:
            if "Undying Shores" not in region_names:
                region_names += ["Undying Shores"]
            region_names += ["Infested Shipwreck", "Lighthouse"]

        # Create all Region objects
        regions: Dict[str, Region] = {}
        for name in region_names:
            region = Region(name, self.player, self.multiworld)
            regions[name] = region
            self.multiworld.regions.append(region)

        # Helper to connect two regions
        def connect(source: str, target: str) -> None:
            if source in regions and target in regions:
                regions[source].connect(regions[target], f"{source} -> {target}")

        # Base game connections
        connect("Menu",                 "Prisoners' Quarters")
        connect("Prisoners' Quarters",  "Promenade")
        connect("Prisoners' Quarters",  "Toxic Sewers")
        connect("Promenade",            "Ramparts")
        connect("Promenade",            "Ossuary")
        connect("Promenade",            "Prison Depths")
        connect("Toxic Sewers",         "Ramparts")
        connect("Toxic Sewers",         "Ancient Sewers")
        connect("Toxic Sewers",         "Corrupted Prison")
        connect("Ramparts",             "Black Bridge")
        connect("Ossuary",              "Insufferable Crypt")
        connect("Ancient Sewers",       "Insufferable Crypt")
        connect("Black Bridge",         "Stilt Village")
        connect("Insufferable Crypt",   "Slumbering Sanctuary")
        connect("Stilt Village",        "Graveyard")
        connect("Stilt Village",        "Clock Tower")
        connect("Slumbering Sanctuary", "Clock Tower")
        connect("Graveyard",            "Clock Tower")
        connect("Clock Tower",          "Forgotten Sepulcher")
        connect("Clock Tower",          "Clock Room")
        connect("Forgotten Sepulcher",  "Clock Room")
        connect("Clock Room",           "High Peak Castle")
        connect("Clock Room",           "Derelict Distillery")
        connect("High Peak Castle",     "Throne Room")
        connect("Derelict Distillery",  "Throne Room")

        # DLC connections
        if self.options.dlc_the_bad_seed:
            connect("Prisoners' Quarters",  "Dilapidated Arboretum")
            connect("Dilapidated Arboretum","Morass")
            connect("Morass",               "Nest")
            connect("Nest",                 "Stilt Village")
        if self.options.dlc_fatal_falls:
            connect("Black Bridge",         "Fractured Shrines")
            connect("Fractured Shrines",    "Undying Shores")
            connect("Undying Shores",       "Mausoleum")
            connect("Mausoleum",            "Clock Tower")
        if self.options.dlc_rise_of_the_giant:
            connect("Prisoners' Quarters",  "Cavern")
            connect("Cavern",               "Guardian's Haven")
            connect("Guardian's Haven",     "Astrolab")
            connect("Astrolab",             "Collector's Lair")
        if self.options.dlc_queen_and_the_sea:
            connect("Black Bridge",         "Undying Shores")
            connect("Undying Shores",       "Infested Shipwreck")
            connect("Infested Shipwreck",   "Lighthouse")

        # Populate regions with locations
        for loc_name, loc_data in ALL_LOCATIONS.items():
            if loc_data.code is None:
                continue
            if loc_data.dlc and not getattr(self.options, loc_data.dlc):
                continue
            if loc_data.region not in regions:
                continue
            location = Location(self.player, loc_name, loc_data.code, regions[loc_data.region])
            regions[loc_data.region].locations.append(location)

        # Victory event
        goal = self.options.goal.value
        if goal == Goal.option_hand_of_the_king:
            victory_region = regions["Throne Room"]
            victory_name = "Hand of the King Victory"
        elif goal == Goal.option_the_collector:
            victory_region = regions.get("Collector's Lair", regions["Throne Room"])
            victory_name = "The Collector Victory"
        else:
            return  # target_bsc is item-based, no event needed

        victory_loc = Location(self.player, victory_name, None, victory_region)
        victory_loc.place_locked_item(
            DeadCellsItem("Victory", ItemClassification.progression, None, self.player)
        )
        victory_region.locations.append(victory_loc)

    def create_items(self) -> None:
        pool: List[Item] = []

        def add(name: str) -> None:
            pool.append(self.create_item(name))

        # Runes always included
        for name in RUNE_ITEMS:
            add(name)

        # BSC if shuffled
        if self.options.bsc_shuffle:
            for name in BSC_ITEMS:
                add(name)

        # Scrolls if shuffled (3 copies each)
        if self.options.scroll_shuffle:
            for name in SCROLL_ITEMS:
                for _ in range(3):
                    add(name)

        # Base game blueprints
        for name in BLUEPRINT_ITEMS:
            add(name)

        # DLC blueprints
        for name, data in DLC_BLUEPRINT_ITEMS.items():
            if data.code is None:
                continue
            if 45_000_300 <= data.code <= 45_000_319 and self.options.dlc_rise_of_the_giant:
                add(name)
            elif 45_000_320 <= data.code <= 45_000_339 and self.options.dlc_the_bad_seed:
                add(name)
            elif 45_000_340 <= data.code <= 45_000_359 and self.options.dlc_fatal_falls:
                add(name)
            elif 45_000_360 <= data.code <= 45_000_379 and self.options.dlc_queen_and_the_sea:
                add(name)

        # Count active locations
        location_count = sum(
            1 for loc in ALL_LOCATIONS.values()
            if loc.code is not None
            and (not loc.dlc or getattr(self.options, loc.dlc))
        )

        # If we have more items than locations, trim from the end of the pool
        # (these will be non-progression items like extra blueprints)
        if len(pool) > location_count:
            pool = pool[:location_count]

        # If we have fewer items than locations, pad with traps and filler
        remaining = location_count - len(pool)
        if remaining > 0:
            trap_count = int(remaining * (self.options.trap_percentage / 100))
            filler_count = remaining - trap_count

            trap_names = list(TRAP_ITEMS.keys())
            filler_names = list(FILLER_ITEMS.keys())

            for i in range(trap_count):
                add(trap_names[i % len(trap_names)])
            for i in range(filler_count):
                add(filler_names[i % len(filler_names)])

        self.multiworld.itempool += pool

    def set_rules(self) -> None:
        set_rules(self.multiworld, self.player, self.options)

    def fill_slot_data(self) -> Dict[str, Any]:
        return self.options.as_dict(
            "goal",
            "target_bsc_level",
            "dlc_rise_of_the_giant",
            "dlc_the_bad_seed",
            "dlc_fatal_falls",
            "dlc_queen_and_the_sea",
            "scroll_shuffle",
            "bsc_shuffle",
            "starting_weapon",
        )
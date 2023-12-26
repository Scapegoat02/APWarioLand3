import os
import typing
import math
import threading

import settings
from BaseClasses import Item, MultiWorld, Tutorial, ItemClassification
from .Items import WL3Item, ItemData, item_table, junk_table, crayon_table, useful_table, event_table, power_up_table, music_box_table, level_key_table
from .Names import ItemName, LocationName
from worlds.AutoWorld import WebWorld, World


class WL3Settings(settings.Group):
    class RomFile(settings.UserFilePath):
        """File name of the WL3 US rom"""
        copy_to = "Wario Land 3 (USA).gbc"
        description = "WL3 (US) ROM File"
        md5s = [WL3DeltaPatch.hash]

    rom_file: RomFile = RomFile(RomFile.copy_to)


class WL3Web(WebWorld):
    theme = "ocean"

    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Wario Land 3 randomizer connected to an Archipelago Multiworld",
        "English",
        "setup_en.md",
        "setup/en",
        ["Scapegoat02"]
    )

    tutorials = [setup_en]
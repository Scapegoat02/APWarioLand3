import Utils
from Utils import read_gbc_rom
from worlds.Files import APDeltaPatch
from .Locations import lookup_id_to_name, all_locations


import hashlib
import os
import math


junk_treasures_rom_data = {
    0xEE0000: [0x4e],  # Ruby
    0xEE0001: [0x4f],  # Emerald
    0xEE0002: [0x50],  # Sapphire
    0xEE0003: [0x51],  # Clubs
    0xEE0004: [0x52],  # Spades
    0xEE0005: [0x53],  # Hearts
    0xEE0006: [0x54],  # Diamonds
    0xEE0007: [0x55],  # Clay Figure
    0xEE0008: [0x56],  # Sabre
    0xEE0009: [0x57],  # Goblet
    0xEE000a: [0x58],  # Teapot
    0xEE000b: [0x5a],  # UFO
    0xEE000c: [0x5b],  # Mini Car
    0xEE000d: [0x5c],  # Locomotive
    0xEE000e: [0x37],  # Rocket Ship
    0xEE000f: [0x38],  # Pocket Pet
    0xEE0010: [0x3c],  # Fighter Mannequin
    0xEE0011: [0x4b],  # Telephone
    0xEE0012: [0x4c]   # Crown
}

level_key_rom_data = {
    0xEE0013: [0x0f],  # Lantern
    0xEE0014: [0x10],  # Magic Flame
    0xEE0015: [0x11],  # Torch
    0xEE0016: [0x12],  # Cog Wheel A
    0xEE0017: [0x13],  # Cog Wheel B
    0xEE0018: [0x14],  # Void Compact Mirror
    0xEE0019: [0x15],  # Raincloud Jar
    0xEE001a: [0x16],  # Crater Map
    0xEE001b: [0x17],  # Blue Book
    0xEE001c: [0x18],  # Sky Key
    0xEE001d: [0x19],  # Yellow Book
    0xEE001e: [0x1a],  # Trident
    0xEE001f: [0x1b],  # Axe
    0xEE0020: [0x1c],  # Magic Wand
    0xEE0021: [0x1d],  # Blue Ring
    0xEE0022: [0x1e],  # Red Ring
    0xEE0023: [0x1f],  # Left Keystone
    0xEE0024: [0x20],  # Right Keystone
    0xEE0025: [0x21],  # Ornamental Fan
    0xEE0026: [0x22],  # Scroll Top
    0xEE0027: [0x23],  # Scroll Bottom
    0xEE0028: [0x24],  # Magic Artifact A
    0xEE0029: [0x25],  # Magic Artifact B
    0xEE002a: [0x26],  # Magic Artifact C
    0xEE002b: [0x27],  # Blue Chemical
    0xEE002c: [0x28],  # Red Chemical
    0xEE002d: [0x29],  # Air Pump
    0xEE002e: [0x2a],  # Octopus Growth Seed
    0xEE002f: [0x2b],  # NVG
    0xEE0030: [0x2c],  # Propeller
    0xEE0031: [0x2d],  # Rust Spray
    0xEE0032: [0x2e],  # Wire Wizard
    0xEE0033: [0x2f],  # Detonator
    0xEE0034: [0x30],  # Scissors
    0xEE0035: [0x31],  # Castle Brick
    0xEE0036: [0x32],  # Warp Remote
    0xEE0037: [0x33],  # Key Card Red
    0xEE0038: [0x34],  # Key Card Blue
    0xEE0039: [0x35],  # Jackhammer
    0xEE003a: [0x36],  # Pickaxe
    0xEE003b: [0x39],  # Valve Handle
    0xEE003c: [0x3a],  # Monster Blood
    0xEE003d: [0x3b],  # Magic Powder
    0xEE003e: [0x3d],  # Truck Wheels
    0xEE003f: [0x3e],  # Snake Flute
    0xEE0040: [0x3f],  # Stone Foot
    0xEE0041: [0x40],  # Gold Eye Left
    0xEE0042: [0x41],  # Gold Eye Right
    0xEE0043: [0x42],  # Blue Eye Left
    0xEE0044: [0x43],  # Blue Eye Right
    0xEE0045: [0x44],  # Purity Staff
    0xEE0046: [0x45],  # Sun Fragment Left
    0xEE0047: [0x46],  # Sun Fragment Right
    0xEE0048: [0x47],  # Mini Storm
    0xEE0049: [0x48],  # Beanstalk Seeds
    0xEE004a: [0x49],  # Storm Pouch
    0xEE004b: [0x4a],  # Moon Gong
    0xEE004c: [0x5d],  # Fire Extinguisher

}

music_box_rom_data = {
    0xEE004d: [0x01],  # Music Box 1
    0xEE004e: [0x02],  # Music Box 2
    0xEE004f: [0x03],  # Music Box 3
    0xEE0050: [0x04],  # Music Box 4
    0xEE0051: [0x05],  # Music Box 5

}

power_up_rom_data = {
    0xEE0052: [0x0c],  # Blue Overalls
    0xEE0053: [0x06],  # Swim Fins
    0xEE0054: [0x0e],  # Spiked Helmet
    0xEE0055: [0x0b],  # Red Gloves
    0xEE0056: [0x0a],  # Garlic
    0xEE0057: [0x0d],  # Red Overalls
    0xEE0058: [0x08],  # Jump Boots
    0xEE0059: [0x07],  # Fast Swim Gloves
    0xEE005a: [0x09],  # Gold Gloves

}

crayon_rom_data = {
    0xEE005b: [0x5e],  # Red Crayon
    0xEE005c: [0x5f],  # Brown Crayon
    0xEE005d: [0x60],  # Yellow Crayon
    0xEE005e: [0x61],  # Green Crayon
    0xEE005f: [0x62],  # Cyan Crayon
    0xEE0060: [0x63],  # Blue Crayon
    0xEE0061: [0x64],  # Pink Crayon

}

useful_table = {
    0xEE0062: [0x4d],  # Time of Day Button
    0xEE0063: [0x59],  # Magnifying Glass
}
import typing

from BaseClasses import Item, ItemClassification
from .Names import ItemName


class ItemData(typing.NamedTuple):
    code: typing.Optional[int]
    progression: bool
    quantity: int = 1
    event: bool = False


class WL3Item(Item):
    game: str = "Wario Land 3"


junk_table = {
    ItemName.ruby: ItemData(0xEE0000, False),  # 0x4e
    ItemName.emerald: ItemData(0xEE0001, False),  # 0x4f
    ItemName.sapphire: ItemData(0xEE0002, False),  # 0x50
    ItemName.clubs: ItemData(0xEE0003, False),  # 0x51
    ItemName.spades: ItemData(0xEE0004, False),  # 0x52
    ItemName.hearts: ItemData(0xEE0005, False),  # 0x53
    ItemName.diamonds: ItemData(0xEE0006, False),  # 0x54
    ItemName.clay_figure: ItemData(0xEE0007, False),  # 0x55
    ItemName.sabre: ItemData(0xEE0008, False),  # 0x56
    ItemName.goblet: ItemData(0xEE0009, False),  # 0x57
    ItemName.teapot: ItemData(0xEE000a, False),  # 0x58
    ItemName.ufo: ItemData(0xEE000b, False),  # 0x5a
    ItemName.mini_car: ItemData(0xEE000c, False),  # 0x5b
    ItemName.locomotive: ItemData(0xEE000d, False),  # 0x5c
    ItemName.rocket_ship: ItemData(0xEE000e, False),  # 0x37
    ItemName.pocket_pet: ItemData(0xEE000f, False),  # 0x38
    ItemName.fighter_mannequin: ItemData(0xEE0010, False),  # 0x3c
    ItemName.telephone: ItemData(0xEE0011, False),  # 0x4b
    ItemName.crown: ItemData(0xEE0012, False),  # 0x4c
}

level_key_table = {
    ItemName.lantern: ItemData(0xEE0013, True),  # 0x0f
    ItemName.magic_flame: ItemData(0xEE0014, True),  # 0x10
    ItemName.torch: ItemData(0xEE0015, True),  # 0x11
    ItemName.cog_wheel_a: ItemData(0xEE0016, True),  # 0x12
    ItemName.cog_wheel_b: ItemData(0xEE0017, True),  # 0x13
    ItemName.warp_mirror: ItemData(0xEE0018, True),  # 0x14
    ItemName.raincloud_jar: ItemData(0xEE0019, True),  # 0x15
    ItemName.crater_map: ItemData(0xEE001a, True),  # 0x16
    ItemName.blue_book: ItemData(0xEE001b, True),  # 0x17
    ItemName.sky_key: ItemData(0xEE001c, True),  # 0x18
    ItemName.yellow_book: ItemData(0xEE001d, True),  # 0x19
    ItemName.trident: ItemData(0xEE001e, True),  # 0x1a
    ItemName.axe: ItemData(0xEE001f, True),  # 0x1b
    ItemName.magic_wand: ItemData(0xEE0020, True),  # 0x1c
    ItemName.blue_ring: ItemData(0xEE0021, True),  # 0x1d
    ItemName.red_ring: ItemData(0xEE0022, True),  # 0x1e
    ItemName.left_keystone: ItemData(0xEE0023, True),  # 0x1f
    ItemName.right_keystone: ItemData(0xEE0024, True),  # 0x20
    ItemName.ornamental_fan: ItemData(0xEE0025, True),  # 0x21
    ItemName.scroll_top: ItemData(0xEE0026, True),  # 0x22
    ItemName.scroll_bottom: ItemData(0xEE0027, True),  # 0x23
    ItemName.magic_artifact_a: ItemData(0xEE0028, True),  # 0x24
    ItemName.magic_artifact_b: ItemData(0xEE0029, True),  # 0x25
    ItemName.magic_artifact_c: ItemData(0xEE002a, True),  # 0x26
    ItemName.blue_chemical: ItemData(0xEE002b, True),  # 0x27
    ItemName.red_chemical: ItemData(0xEE002c, True),  # 0x28
    ItemName.air_pump: ItemData(0xEE002d, True),  # 0x29
    ItemName.growth_seed: ItemData(0xEE002e, True),  # 0x2a
    ItemName.night_vision_goggles: ItemData(0xEE002f, True),  # 0x2b
    ItemName.fan_propeller: ItemData(0xEE0030, True),  # 0x2c
    ItemName.rust_spray: ItemData(0xEE0031, True),  # 0x2d
    ItemName.wire_wizard: ItemData(0xEE0032, True),  # 0x2e
    ItemName.detonator: ItemData(0xEE0033, True),  # 0x2f
    ItemName.scissors: ItemData(0xEE0034, True),  # 0x30
    ItemName.castle_brick: ItemData(0xEE0035, True),  # 0x31
    ItemName.warp_remote: ItemData(0xEE0036, True),  # 0x32
    ItemName.key_card_red: ItemData(0xEE0037, True),  # 0x33
    ItemName.key_card_blue: ItemData(0xEE0038, True),  # 0x34
    ItemName.jackhammer: ItemData(0xEE0039, True),  # 0x35
    ItemName.pickaxe: ItemData(0xEE003a, True),  # 0x36
    ItemName.valve_handle: ItemData(0xEE003b, True),  # 0x39
    ItemName.monster_blood: ItemData(0xEE003c, True),  # 0x3a
    ItemName.magic_powder: ItemData(0xEE003d, True),  # 0x3b
    ItemName.truck_wheels: ItemData(0xEE003e, True),  # 0x3d
    ItemName.snake_flute: ItemData(0xEE003f, True),  # 0x3e
    ItemName.stone_foot: ItemData(0xEE0040, True),  # 0x3f
    ItemName.gold_eye_left: ItemData(0xEE0041, True),  # 0x40
    ItemName.gold_eye_right: ItemData(0xEE0042, True),  # 0x41
    ItemName.blue_eye_left: ItemData(0xEE0043, True),  # 0x42
    ItemName.blue_eye_right: ItemData(0xEE0044, True),  # 0x43
    ItemName.purity_staff: ItemData(0xEE0045, True),  # 0x44
    ItemName.sun_fragment_left: ItemData(0xEE0046, True),  # 0x45
    ItemName.sun_fragment_right: ItemData(0xEE0047, True),  # 0x46
    ItemName.mini_storm: ItemData(0xEE0048, True),  # 0x47
    ItemName.beanstalk_seeds: ItemData(0xEE0049, True),  # 0x48
    ItemName.storm_pouch: ItemData(0xEE004a, True),  # 0x49
    ItemName.full_moon_gong: ItemData(0xEE004b, True),  # 0x4a
    ItemName.fire_extinguisher: ItemData(0xEE004c, True),  # 0x5d

}

music_box_table = {
    ItemName.musicbox_1: ItemData(0xEE004d, True),  # 0x01
    ItemName.musicbox_2: ItemData(0xEE004e, True),  # 0x02
    ItemName.musicbox_3: ItemData(0xEE004f, True),  # 0x03
    ItemName.musicbox_4: ItemData(0xEE0050, True),  # 0x04
    ItemName.musicbox_5: ItemData(0xEE0051, True),  # 0x05
}

power_up_table = {
    ItemName.blue_overalls: ItemData(0xEE0052, True),  # 0x0c
    ItemName.swim_fins: ItemData(0xEE0053, True),  # 0x06
    ItemName.spiked_helmet: ItemData(0xEE0054, True),  # 0x0e
    ItemName.red_gloves: ItemData(0xEE0055, True),  # 0x0b
    ItemName.garlic: ItemData(0xEE0056, True),  # 0x0a
    ItemName.red_overalls: ItemData(0xEE0057, True),  # 0x0d
    ItemName.jump_boots: ItemData(0xEE0058, True),  # 0x08
    ItemName.swim_gloves: ItemData(0xEE0059, True),  # 0x07
    ItemName.gold_gloves: ItemData(0xEE005a, True),  # 0x09
}

crayon_table = {
    ItemName.red_crayon: ItemData(0xEE005b, False),  # 0x5e
    ItemName.brown_crayon: ItemData(0xEE005c, False),  # 0x5f
    ItemName.yellow_crayon: ItemData(0xEE005d, False),  # 0x60
    ItemName.green_crayon: ItemData(0xEE005e, False),  # 0x61
    ItemName.cyan_crayon: ItemData(0xEE005f, False),  # 0x62
    ItemName.blue_crayon: ItemData(0xEE0060, False),  # 0x63
    ItemName.pink_crayon: ItemData(0xEE0061, False),  # 0x64
}

useful_table = {
    ItemName.time_button: ItemData(0xEE0062, False),  # 0x4d
    ItemName.magnifying_glass: ItemData(0xEE0063, False)  # 0x59
}

event_table = {
    ItemName.victory(0xEE0064, True),
    ItemName.empty(0xEE0065, False)
}

# Complete item table.
item_table = {
    **junk_table,
    **music_box_table,
    **power_up_table,
    **crayon_table,
    **music_box_table,
    **useful_table,
    **level_key_table,
}

lookup_id_to_name: typing.Dict[int, str] = {data.code: item_name for item_name, data in item_table.items() if data.code}


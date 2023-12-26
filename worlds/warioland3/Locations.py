import typing

from BaseClasses import Location
from .Names import LocationName


class WL3Location(Location):
    game: str = "Wario Land 3"

    progress_byte: int = 0x000000
    progress_bit: int = 0
    inverted_bit: bool = False

    def __init__(self, player:int, name: str = '', address: int = None, parent=None, prog_byte: int = None, prog_bit: int = None, invert: bool = False):
        super().__init__(player, name, address, parent)
        self.progress_byte = prog_byte
        self.progress_bit = prog_bit
        self.inverted_bit = invert


level_location_table = {
    LocationName.n1_out_of_the_woods_gray_chest: 0xEE0000,
    LocationName.n1_out_of_the_woods_red_chest: 0xEE0001,
    LocationName.n1_out_of_the_woods_green_chest: 0xEE0002,

    LocationName.n2_the_peaceful_village_gray_chest: 0xEE0004,
    LocationName.n2_the_peaceful_village_red_chest: 0xEE0005,
    LocationName.n2_the_peaceful_village_green_chest: 0xEE0006,
    LocationName.n2_the_peaceful_village_blue_chest: 0xEE0007,

    LocationName.n3_the_vast_plain_gray_chest: 0xEE0008,
    LocationName.n3_the_vast_plain_red_chest: 0xEE0009,
    LocationName.n3_the_vast_plain_green_chest: 0xEE000a,
    LocationName.n3_the_vast_plain_blue_chest: 0xEE000b,

    LocationName.n4_bank_of_the_wild_river_gray_chest: 0xEE000c,
    LocationName.n4_bank_of_the_wild_river_red_chest: 0xEE000d,
    LocationName.n4_bank_of_the_wild_river_blue_chest: 0xEE000f,

    LocationName.n5_the_tidal_coast_gray_chest: 0xEE0010,
    LocationName.n5_the_tidal_coast_red_chest: 0xEE0011,
    LocationName.n5_the_tidal_coast_green_chest: 0xEE0012,
    LocationName.n5_the_tidal_coast_blue_chest: 0xEE0013,

    LocationName.n6_sea_turtle_rock_red_chest: 0xEE0015,
    LocationName.n6_sea_turtle_rock_green_chest: 0xEE0016,
    LocationName.n6_sea_turtle_rock_blue_chest: 0xEE0017,

    LocationName.w1_desert_ruins_gray_chest: 0xEE0018,
    LocationName.w1_desert_ruins_red_chest: 0xEE0019,
    LocationName.w1_desert_ruins_green_chest: 0xEE001a,

    LocationName.w2_the_volcanos_base_red_chest: 0xEE001d,
    LocationName.w2_the_volcanos_base_green_chest: 0xEE001e,
    LocationName.w2_the_volcanos_base_blue_chest: 0xEE001f,

    LocationName.w3_the_pool_of_rain_gray_chest: 0xEE0020,
    LocationName.w3_the_pool_of_rain_red_chest: 0xEE0021,
    LocationName.w3_the_pool_of_rain_blue_chest: 0xEE0023,

    LocationName.w4_a_town_in_chaos_gray_chest: 0xEE0024,
    LocationName.w4_a_town_in_chaos_green_chest: 0xEE0026,
    LocationName.w4_a_town_in_chaos_blue_chest: 0xEE0027,

    LocationName.w5_beneath_the_waves_gray_chest: 0xEE0028,
    LocationName.w5_beneath_the_waves_red_chest: 0xEE0029,
    LocationName.w5_beneath_the_waves_green_chest: 0xEE002a,
    LocationName.w5_beneath_the_waves_blue_chest: 0xEE002b,

    LocationName.w6_the_west_crater_gray_chest: 0xEE002c,
    LocationName.w6_the_west_crater_red_chest: 0xEE002d,
    LocationName.w6_the_west_crater_green_chest: 0xEE002e,
    LocationName.w6_the_west_crater_blue_chest: 0xEE002f,

    LocationName.s1_the_grasslands_red_chest: 0xEE0031,
    LocationName.s1_the_grasslands_green_chest: 0xEE0032,
    LocationName.s1_the_grasslands_blue_chest: 0xEE0033,

    LocationName.s2_the_big_bridge_gray_chest: 0xEE0034,
    LocationName.s2_the_big_bridge_red_chest: 0xEE0035,
    LocationName.s2_the_big_bridge_green_chest: 0xEE0036,
    LocationName.s2_the_big_bridge_blue_chest: 0xEE0037,

    LocationName.s3_tower_of_revival_gray_chest: 0xEE0038,
    LocationName.s3_tower_of_revival_red_chest: 0xEE0039,
    LocationName.s3_tower_of_revival_green_chest: 0xEE003a,
    LocationName.s3_tower_of_revival_blue_chest: 0xEE003b,

    LocationName.s4_the_steep_canyon_gray_chest: 0xEE003c,
    LocationName.s4_the_steep_canyon_red_chest: 0xEE003d,
    LocationName.s4_the_steep_canyon_green_chest: 0xEE003e,
    LocationName.s4_the_steep_canyon_blue_chest: 0xEE003f,

    LocationName.s5_cave_of_flames_gray_chest: 0xEE0040,
    LocationName.s5_cave_of_flames_red_chest: 0xEE0041,
    LocationName.s5_cave_of_flames_green_chest: 0xEE0042,
    LocationName.s5_cave_of_flames_blue_chest: 0xEE0043,

    LocationName.s6_above_the_clouds_gray_chest: 0xEE0044,
    LocationName.s6_above_the_clouds_red_chest: 0xEE0045,
    LocationName.s6_above_the_clouds_green_chest: 0xEE0046,
    LocationName.s6_above_the_clouds_blue_chest: 0xEE0047,

    LocationName.e1_the_stagnant_swamp_gray_chest: 0xEE0048,
    LocationName.e1_the_stagnant_swamp_blue_chest: 0xEE004b,

    LocationName.e2_the_frigid_sea_gray_chest: 0xEE004c,
    LocationName.e2_the_frigid_sea_red_chest: 0xEE004d,
    LocationName.e2_the_frigid_sea_green_chest: 0xEE004e,
    LocationName.e2_the_frigid_sea_blue_chest: 0xEE004f,

    LocationName.e3_castle_of_illusions_gray_chest: 0xEE0050,
    LocationName.e3_castle_of_illusions_red_chest: 0xEE0051,
    LocationName.e3_castle_of_illusions_green_chest: 0xEE0052,
    LocationName.e3_castle_of_illusions_blue_chest: 0xEE0053,

    LocationName.e4_the_colossal_hole_gray_chest: 0xEE0054,
    LocationName.e4_the_colossal_hole_red_chest: 0xEE0055,
    LocationName.e4_the_colossal_hole_green_chest: 0xEE0056,
    LocationName.e4_the_colossal_hole_blue_chest: 0xEE0057,

    LocationName.e5_the_warped_void_gray_chest: 0xEE0058,
    LocationName.e5_the_warped_void_red_chest: 0xEE0059,
    LocationName.e5_the_warped_void_green_chest: 0xEE005a,
    LocationName.e5_the_warped_void_blue_chest: 0xEE005b,

    LocationName.e6_the_east_crater_gray_chest: 0xEE005c,
    LocationName.e6_the_east_crater_red_chest: 0xEE005d,
    LocationName.e6_the_east_crater_green_chest: 0xEE005e,
    LocationName.e6_the_east_crater_blue_chest: 0xEE005f,

    LocationName.e7_forest_of_fear_gray_chest: 0xEE0060,
    LocationName.e7_forest_of_fear_red_chest: 0xEE0061,
    LocationName.e7_forest_of_fear_green_chest: 0xEE0062,
    LocationName.e7_forest_of_fear_blue_chest: 0xEE0063,

}


boss_chest_location_table = {
    LocationName.n1_out_of_the_woods_blue_chest: 0xEE0003,
    LocationName.n4_bank_of_the_wild_river_green_chest: 0xEE000e,
    LocationName.n6_sea_turtle_rock_gray_chest: 0xEE0014,
    LocationName.w1_desert_ruins_blue_chest: 0xEE001b,
    LocationName.w2_the_volcanos_base_gray_chest: 0xEE001c,
    LocationName.w3_the_pool_of_rain_green_chest: 0xEE0022,
    LocationName.w4_a_town_in_chaos_red_chest: 0xEE0025,
    LocationName.s1_the_grasslands_gray_chest: 0xEE0030,
    LocationName.e1_the_stagnant_swamp_red_chest: 0xEE0049,
    LocationName.e1_the_stagnant_swamp_green_chest: 0xEE004a
}

all_locations = {
    **level_location_table,
    **boss_chest_location_table,
}


def setup_locations(world, player: int):
    location_table = {**all_locations}
    return location_table


lookup_id_to_name: typing.Dict[int, str] = {id: name for name, _ in all_locations.items()}
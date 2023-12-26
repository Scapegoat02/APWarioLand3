import typing

from Options import Choice, Range, Option, Toggle, DefaultOnToggle


class Goal(Choice):
    """
    Determinse the goal of the seed
    5 Music Boxes: Find all 5 music boxes to unlock the final boss fight with Rudy and defeat that clown.
    Last Music Box: Only the fifth music box is needed to unlock the boss fight with Rudy at The Temple.
    """
    display_name = "Goal"
    option_music_boxes = 0
    option_last_box = 1
    default = 0


class RemoveJunkItems(Toggle):
    """
    Will remove all junk treasures that serve absolutely no purpose from the multiworld. When their locations
    are filled, treasure chest locations that would have held these items will appear as already collected.
    """
    display_name = "Remove Junk Items"


class OpenStart(Toggle):
    """
    Will start Wario with a few level key treasures that will start with a more open map. More Metroidvania style!
    """
    display_name = "Open Start"


class PowerfulStart(Range):
    """
    Randomly chooses the selected number powerup items to give to Wario at the start. Will attempt to provide the Blue
    Overalls, Swim Flippers, and Red Gloves first.
    """
    display_name = "Powerful Start"
    range_start = 0
    range_end = 9
    default = 0


class RestrictedMusicBoxes(Toggle):
    """
    Will ensure that if music boxes are local, they will be placed on a chest that is guarded by a boss.
    """
    display_name = "Music Boxes on Bosses"


class StartWithUsefulItems(Toggle):
    """
    Ensures that the Magnifying Glass (Hold B on the map screen to quick look at available chests) and the Time of Day
    Button (press Select and use the button to change the time of day without having to enter and exit a stage) will be
    placed in Wario's starting inventory.
    """
    display_name = "Start With Useful Items"


class MusicBoxCount(Range):
    """
    How many music boxes are needed to summon the final boss Rudy.
    """
    display_name = "Music Box Goal Requirement"
    range_start = 1
    range_end = 5
    default = 5


class StageShuffle(Toggle):
    """
    Shuffles the stages across the level nodes within the whole world. The level keys that unlock stages will
    unlock the respective map node, NOT the intended level at that node. Some navigation using the "Next Area" feature
    in the Select menu on the map screen may be needed to access level nodes that are stuck behind a one-way path.
    """
    display_name = "Stage Shuffle"


wl3_options: typing.Dict[str, type(Option)] = {
    "goal": Goal,
    "remove_junk_items": RemoveJunkItems,
    "powerful_start": PowerfulStart,
    "start_with_useful_items": StartWithUsefulItems,
    "music_box_count": MusicBoxCount,
    "stage_shuffle": StageShuffle,
    "open_start": OpenStart,
}


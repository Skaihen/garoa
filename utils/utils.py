from typing import List, TypedDict

from arcade import Texture


class CharacterParams(TypedDict):
    name_file: str
    sprite_width: int
    sprite_height: int
    columns: int
    count: int
    scale: float
    fpt: float


def get_animation_dict_from_texture_list(texture_list: List[Texture], columns: int, directions: tuple) -> dict:
    animation_dict = {}
    total_texture_count = 0

    for i in directions:
        texture_list_partial = []
        for _ in range(columns):
            texture_list_partial.append(texture_list[total_texture_count])
            total_texture_count += 1
        animation_dict[f"{i}_animation"] = texture_list_partial

    return animation_dict

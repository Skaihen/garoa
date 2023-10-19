from typing import List

from arcade import Texture


def get_animation_dict_from_texture_list(texture_list: List[Texture], columns: int, count: int) -> dict:
    animation_dict = {
        "down_walk_animation": None,
        "left_walk_animation": None,
        "right_walk_animation": None,
        "up_walk_animation": None,
        "idle": texture_list[1],
    }
    directions = "down", "left", "right", "up"
    texture_count = 0

    for i in range(int(count / columns)):
        texture_partial = []
        for _ in range(columns):
            texture_partial.append(texture_list[texture_count])
            texture_count += 1
        animation_dict[f"{directions[i]}_walk_animation"] = texture_partial

    return animation_dict

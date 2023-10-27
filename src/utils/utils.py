from typing import TypedDict

import arcade

from src.config import SCREEN_HEIGHT, SCREEN_WIDTH


class CharacterParams(TypedDict):
    name_file: str
    sprite_width: int
    sprite_height: int
    columns: int
    count: int
    scale: float
    speed: float
    fpt: float
    directions: tuple


class CharacterStats(TypedDict):
    health_bar_list: arcade.SpriteList
    health: int


def is_sprite_off_screen(sprite: arcade.Sprite, screen_height: int = SCREEN_HEIGHT,
                         screen_width: int = SCREEN_WIDTH) -> bool:
    return (
            sprite.top < 0
            or sprite.bottom > screen_height
            or sprite.right < 0
            or sprite.left > screen_width
    )


def get_animation_dict_from_texture_list(texture_list: list[arcade.Texture], columns: int, directions: tuple) -> \
        dict[str, list[arcade.Texture]]:
    animation_dict = {}
    total_texture_count = 0

    for i in directions:
        texture_list_partial = []
        for _ in range(columns):
            texture_list_partial.append(texture_list[total_texture_count])
            total_texture_count += 1
        animation_dict[f"{i}_animation"] = texture_list_partial

    return animation_dict

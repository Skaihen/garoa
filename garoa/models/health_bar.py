from typing import Tuple

import arcade


class HealthBar(arcade.Sprite):
    def __init__(self, max_health: int, position: Tuple[float, float] = (0, 0),
                 full_color: arcade.Color = arcade.color.GREEN, background_color: arcade.Color = arcade.color.BLACK,
                 width: int = 100, height: int = 4, border_size: int = 4) -> None:
        super().__init__()
        self.max_health = max_health
        self.box_width = width
        self.box_height = height
        self.center_x = position[0]
        self.center_y = position[1]

        self.background_box = arcade.SpriteSolidColor(
            self.box_width + border_size,
            self.box_height + border_size,
            background_color,
        )
        self.full_box = arcade.SpriteSolidColor(
            self.box_width,
            self.box_height,
            full_color,
        )
        self.sprite_list = arcade.SpriteList()
        self.sprite_list.append(self.background_box)
        self.sprite_list.append(self.full_box)

    def update_bar_on_dmg(self):
        


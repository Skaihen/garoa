from typing import Tuple

import arcade


class IndicatorBar(arcade.Sprite):
    def __init__(self, sprite_list: arcade.SpriteList, position: Tuple[float, float] = (0, 0),
                 full_color: arcade.Color = arcade.color.GREEN, background_color: arcade.Color = arcade.color.BLACK,
                 width: int = 100, height: int = 4, border_size: int = 4) -> None:
        super().__init__()
        self.sprite_list = sprite_list

        self.box_width = width
        self.box_height = height
        self.center_x = 0.0
        self.center_y = 0.0
        self.fullness = 5

        self._background_box = arcade.SpriteSolidColor(
            self.box_width + border_size,
            self.box_height + border_size,
            background_color,
        )
        self._full_box = arcade.SpriteSolidColor(
            self.box_width,
            self.box_height,
            full_color,
        )
        self.sprite_list.append(self._background_box)
        self.sprite_list.append(self._full_box)
        self.position = position

    @property
    def background_box(self) -> arcade.SpriteSolidColor:
        return self._background_box

    @property
    def full_box(self) -> arcade.SpriteSolidColor:
        return self._full_box

    @property
    def fullness(self) -> float:
        return self._fullness

    @fullness.setter
    def fullness(self, new_fullness: float) -> None:
        if not (0.0 <= new_fullness <= self.fullness):
            raise ValueError(
                f"Got {new_fullness}, but fullness must be between 0.0 and {self.fullness}."
            )

        self._fullness = new_fullness
        if new_fullness == 0:
            self.full_box.visible = False
        else:
            self.full_box.visible = True
            self.full_box.width = self.box_width * new_fullness
            self.full_box.left = self._center_x - (self.box_width // 2)

    @property
    def position(self) -> Tuple[float, float]:
        return self._center_x, self._center_y

    @position.setter
    def position(self, new_position: Tuple[float, float]) -> None:
        if new_position != self.position:
            self._center_x, self._center_y = new_position
            self.background_box.position = new_position
            self.full_box.position = new_position

            self.full_box.left = self._center_x - (self.box_width // 2)

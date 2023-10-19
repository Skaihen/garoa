from pathlib import Path
from typing import Union

import arcade


class Character(arcade.Sprite):
    def __init__(self, name_file: Union[str, Path], sprite_width: int, sprite_height: int, columns: int, count: int,
                 scale: float):
        super().__init__(scale=scale)

        main_path = f"assets/sprites/{name_file}"
        self.walk_textures = arcade.load_spritesheet(main_path, sprite_width, sprite_height, columns, count)
        self.columns = columns
        self.cur_texture = 0
        self.character_face_direction = 0
        self.texture = self.walk_textures[1]
        self.hit_box = self.texture.hit_box_points

    def update_animation(self, delta_time: float = 1 / 60):
        # if self.change_x < 0:
        #     self.character_face_direction = 4
        # elif self.change_x > 0:
        #     self.character_face_direction = 8
        #
        # if self.change_y < 0:
        #     self.character_face_direction = 0
        # elif self.change_y > 0:
        #     self.character_face_direction = 12
        #
        # if self.change_x == 0 and self.change_y == 0:
        #     self.texture = self.walk_textures[self.character_face_direction]
        #     return

        self.cur_texture += 1
        if self.cur_texture > self.columns:
            self.cur_texture = 0
        self.texture = self.walk_textures[self.cur_texture]

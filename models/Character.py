import arcade

from utils.utils import get_animation_dict_from_texture_list


class Character(arcade.Sprite):
    def __init__(self, name_file: str, sprite_width: int, sprite_height: int, columns: int, count: int,
                 scale: float):
        super().__init__(scale=scale)

        main_path = f"assets/sprites/{name_file}"
        self.walk_textures = arcade.load_spritesheet(main_path, sprite_width, sprite_height, columns, count)
        self.walk_textures_dict = get_animation_dict_from_texture_list(self.walk_textures, columns, count)
        self.cur_texture = 0
        self.columns = columns
        self.character_face_direction = "down_walk_animation"
        self.texture = self.walk_textures[1]
        self.hit_box = self.texture.hit_box_points

    def update_animation(self, delta_time: float = 1 / 60):
        if self.change_x < 0:
            self.character_face_direction = "left_walk_animation"
        elif self.change_x > 0:
            self.character_face_direction = "right_walk_animation"

        elif self.change_y < 0:
            self.character_face_direction = "down_walk_animation"
        elif self.change_y > 0:
            self.character_face_direction = "up_walk_animation"

        if self.change_x == 0 and self.change_y == 0:
            self.texture = self.walk_textures_dict[self.character_face_direction][1]
            return

        self.cur_texture += 0.25
        if self.cur_texture > self.columns - 1:
            self.cur_texture = 0
        self.texture = self.walk_textures_dict[self.character_face_direction][int(self.cur_texture)]

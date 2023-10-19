import arcade

from utils.utils import get_animation_dict_from_texture_list


class Character(arcade.Sprite):
    # TODO Convertir entrada en un dict para poder meter los personajes como json y cambiar parametros como el default self.texture a entrada tambien
    def __init__(self, name_file: str, sprite_width: int, sprite_height: int, columns: int, count: int,
                 scale: float, fpt: float):
        super().__init__(scale=scale)

        main_path = f"assets/sprites/{name_file}"
        self.walk_textures = arcade.load_spritesheet(main_path, sprite_width, sprite_height, columns, count)
        self.walk_textures_dict = get_animation_dict_from_texture_list(self.walk_textures, columns,
                                                                       ("down_walk", "left_walk", "right_walk",
                                                                        "up_walk"))
        self.cur_texture = 0
        self.fpt = fpt
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

        self.cur_texture += self.fpt
        if self.cur_texture > self.columns - 1:
            self.cur_texture = 0
        self.texture = self.walk_textures_dict[self.character_face_direction][int(self.cur_texture)]

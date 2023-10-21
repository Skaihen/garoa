import arcade

from utils.utils import get_animation_dict_from_texture_list, CharacterParams


class Character(arcade.Sprite):
    def __init__(self, character_params: CharacterParams):
        super().__init__(scale=character_params["scale"])

        main_path = f"assets/sprites/{character_params['name_file']}"
        self.walk_textures = arcade.load_spritesheet(main_path, character_params["sprite_width"],
                                                     character_params["sprite_height"], character_params["columns"],
                                                     character_params["count"])
        self.walk_textures_dict = get_animation_dict_from_texture_list(self.walk_textures, character_params["columns"],
                                                                       character_params["directions"])
        self.cur_texture = 0
        self.fpt = character_params["fpt"]
        self.columns = character_params["columns"]
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

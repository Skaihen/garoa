import arcade

from src.utils import get_animation_dict_from_texture_list, CharacterParams, CharacterStats


class Character(arcade.Sprite):
    def __init__(self, character_params: CharacterParams, character_stats: CharacterStats) -> None:
        super().__init__(scale=character_params["scale"])

        main_path = f"../assets/sprites/{character_params['name_file']}"
        self.walk_textures = arcade.load_spritesheet(main_path, character_params["sprite_width"],
                                                     character_params["sprite_height"], character_params["columns"],
                                                     character_params["count"])
        self.walk_textures_dict = get_animation_dict_from_texture_list(self.walk_textures, character_params["columns"],
                                                                       character_params["directions"])
        self.cur_texture = 0.0
        self.fpt = character_params["fpt"]
        self.columns = character_params["columns"]
        self.character_face_direction = "down_walk_animation"
        self.texture = self.walk_textures[1]
        self.hit_box = self.texture.hit_box_points
        self.health = character_stats["health"]

    def update_animation(self, delta_time: float = 1 / 60) -> None:
        if self.change_x == 0 and self.change_y == 0:
            self.texture = self.walk_textures_dict[self.character_face_direction][1]
            return

        if abs(self.change_x) >= abs(self.change_y):
            self.character_face_direction = "left_walk_animation" if self.change_x < 0 else "right_walk_animation"
        else:
            self.character_face_direction = "down_walk_animation" if self.change_y < 0 else "up_walk_animation"

        self.cur_texture = (self.cur_texture + self.fpt) % self.columns
        self.texture = self.walk_textures_dict[self.character_face_direction][int(self.cur_texture)]

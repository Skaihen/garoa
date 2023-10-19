import os

import arcade

from models.Character import Character

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 350
SCREEN_TITLE = "Garoa"

TILE_SCALING = 0.5
CHARACTER_SCALING = TILE_SCALING * 4
SPRITE_PIXEL_SIZE = 64
GRID_PIXEL_SIZE = SPRITE_PIXEL_SIZE * TILE_SCALING

MOVEMENT_SPEED = 3

PLAYER_START_X = 4
PLAYER_START_Y = 25

PLAYER_LAYER = "Player"
BACKGROUND_LAYER = "Background"
TREES_LAYER = "Trees"
ITEMS_LAYER = "Items"


class Garoa(arcade.Window):
    def __init__(self, width, height, title, vsync):
        super().__init__(width, height, title, vsync)

        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        self.tile_map = None
        self.map_height = 0
        self.scene = None
        self.player_sprite = None
        self.physics_engine = None
        self.camera = None
        self.gui_camera = None
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

    def setup(self):
        self.camera = arcade.Camera(self.width, self.height)
        self.gui_camera = arcade.Camera(self.width, self.height)

        layer_options = {
            ITEMS_LAYER: {
                "use_spatial_hash": True
            }
        }
        self.tile_map = arcade.TileMap("assets/maps/testMap.json", TILE_SCALING, layer_options)
        self.scene = arcade.Scene.from_tilemap(self.tile_map)

        self.player_sprite = Character("player-sheet.png", 12,
                                       18, 4, 16, CHARACTER_SCALING)
        self.player_sprite.center_x = (
                self.tile_map.tile_width * TILE_SCALING * PLAYER_START_X
        )
        self.player_sprite.center_y = (
                self.tile_map.tile_height * TILE_SCALING * PLAYER_START_Y
        )
        self.scene.add_sprite(PLAYER_LAYER, self.player_sprite)

        self.map_height = self.tile_map.height * GRID_PIXEL_SIZE
        if self.tile_map.background_color:
            arcade.set_background_color(self.tile_map.background_color)

        self.physics_engine = arcade.PhysicsEngineSimple(
            self.player_sprite, self.scene[ITEMS_LAYER]
        )

    def on_draw(self):
        self.clear()
        self.camera.use()
        self.scene.draw(pixelated=True)
        self.gui_camera.use()

        score_text = f"Interfaz {self.player_sprite.change_x}, {self.player_sprite.change_y}"
        arcade.draw_text(
            score_text,
            10,
            self.height - 20,
            arcade.csscolor.WHITE,
            18,
        )

    def update_player_speed(self):
        self.player_sprite.change_x = 0
        self.player_sprite.change_y = 0

        if self.up_pressed and not self.down_pressed:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif self.down_pressed and not self.up_pressed:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        if self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP and key == arcade.key.W:
            self.up_pressed = True
            self.update_player_speed()
        elif key == arcade.key.DOWN and key == arcade.key.S:
            self.down_pressed = True
            self.update_player_speed()
        elif key == arcade.key.LEFT and key == arcade.key.A:
            self.left_pressed = True
            self.update_player_speed()
        elif key == arcade.key.RIGHT and key == arcade.key.D:
            self.right_pressed = True
            self.update_player_speed()

    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP and key == arcade.key.W:
            self.up_pressed = False
            self.update_player_speed()
        elif key == arcade.key.DOWN and key == arcade.key.S:
            self.down_pressed = False
            self.update_player_speed()
        elif key == arcade.key.LEFT and key == arcade.key.A:
            self.left_pressed = False
            self.update_player_speed()
        elif key == arcade.key.RIGHT and key == arcade.key.D:
            self.right_pressed = False
            self.update_player_speed()

    def center_camera_to_player(self):
        screen_center_x = self.player_sprite.center_x - (self.camera.viewport_width / 2)
        screen_center_y = self.player_sprite.center_y - (self.camera.viewport_height / 2)

        if screen_center_x < 0:
            screen_center_x = 0
        if screen_center_y < 0:
            screen_center_y = 0
        if (screen_center_y + self.height / 2) > 900:
            screen_center_y = 900 - self.height / 2
        player_centered = screen_center_x, screen_center_y

        self.camera.move_to(player_centered, 0.2)

    def on_update(self, delta_time):
        self.physics_engine.update()
        self.scene.update_animation(
            delta_time, [BACKGROUND_LAYER, PLAYER_LAYER]
        )
        # self.scene.update([ITEMS_LAYER])
        self.center_camera_to_player()


def main():
    window = Garoa(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, False)
    window.center_window()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()

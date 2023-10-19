import os

import arcade

from models.Character import Character

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 350
SCREEN_TITLE = "Garoa"

TILE_SCALING = 0.5
CHARACTER_SCALING = TILE_SCALING * 2
SPRITE_PIXEL_SIZE = 64
GRID_PIXEL_SIZE = SPRITE_PIXEL_SIZE * TILE_SCALING

PLAYER_MOVEMENT_SPEED = 5

PLAYER_START_X = 90 * CHARACTER_SCALING
PLAYER_START_Y = 800 * CHARACTER_SCALING

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

        self.scene.add_sprite_list_after("Player", TREES_LAYER)
        self.player_sprite = Character("assets/sprites/player-sheet.png")
        self.player_sprite.center_x = PLAYER_START_X
        self.player_sprite.center_y = PLAYER_START_Y
        self.scene.add_sprite("Player", self.player_sprite)

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

        score_text = f"Interfaz {self.player_sprite.center_y + (self.camera.viewport_height / 2)}"
        arcade.draw_text(
            score_text,
            10,
            self.height - 20,
            arcade.csscolor.WHITE,
            18,
        )

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.W:
            self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
        if key == arcade.key.DOWN or key == arcade.key.S:
            self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
        if key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        if key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.W:
            self.player_sprite.change_y = 0
        if key == arcade.key.DOWN or key == arcade.key.S:
            self.player_sprite.change_y = 0
        if key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = 0
        if key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = 0

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
        self.center_camera_to_player()


def main():
    window = Garoa(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, False)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()

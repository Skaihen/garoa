import arcade

from garoa.config.config import ITEMS_LAYER, TILE_SCALING, PLAYER_START_X, PLAYER_START_Y, \
    PLAYER_LAYER, GRID_PIXEL_SIZE, BLOCKS_LAYER, FOREGROUND_LAYER
from garoa.config.player_config import PLAYER_PARAMS, PLAYER_STATS
from garoa.models.player import Player


class GameView(arcade.View):
    def __init__(self) -> None:
        super().__init__()

        self.tile_map = None
        self.map_height = 0
        self.scene = None
        self.player_sprite = None
        self.physics_engine = None
        self.camera = None
        self.gui_camera = None

    def setup(self) -> None:
        self.camera = arcade.Camera(self.window.width, self.window.height)
        self.gui_camera = arcade.Camera(self.window.width, self.window.height)

        layer_options = {
            ITEMS_LAYER: {
                "use_spatial_hash": True
            },
            BLOCKS_LAYER: {
                "use_spatial_hash": True
            },
            FOREGROUND_LAYER: {
                "use_spatial_hash": True
            }
        }
        self.tile_map = arcade.TileMap("../assets/maps/testMap.json", TILE_SCALING, layer_options)
        self.scene = arcade.Scene.from_tilemap(self.tile_map)

        self.player_sprite = Player(PLAYER_PARAMS, PLAYER_STATS)
        self.player_sprite.center_x = (
                self.tile_map.tile_width * TILE_SCALING * PLAYER_START_X
        )
        self.player_sprite.center_y = (
                self.tile_map.tile_height * TILE_SCALING * PLAYER_START_Y
        )
        self.scene.add_sprite(PLAYER_LAYER, self.player_sprite)
        self.scene.add_sprite_list(ITEMS_LAYER, PLAYER_STATS["health_bar_list"])

        self.map_height = self.tile_map.height * GRID_PIXEL_SIZE
        if self.tile_map.background_color:
            arcade.set_background_color(self.tile_map.background_color)

        self.physics_engine = arcade.PhysicsEngineSimple(
            self.player_sprite, self.scene[BLOCKS_LAYER]
        )

    def on_key_press(self, key, modifiers) -> None:
        self.player_sprite.on_key_press(key, modifiers)

    def on_key_release(self, key, modifiers) -> None:
        self.player_sprite.on_key_release(key, modifiers)

    def center_camera_to_player(self) -> None:
        screen_center_x = self.player_sprite.center_x - (self.camera.viewport_width / 2)
        screen_center_y = self.player_sprite.center_y - (self.camera.viewport_height / 2)

        if screen_center_x < 0:
            screen_center_x = 0
        if screen_center_y < 0:
            screen_center_y = 0
        if (screen_center_y + self.window.height / 2) > 900:
            screen_center_y = 900 - self.window.height / 2
        player_centered = screen_center_x, screen_center_y

        self.camera.move_to(player_centered, 0.2)

    def on_draw(self) -> None:
        self.clear()
        self.camera.use()
        self.scene.draw(pixelated=True)
        self.gui_camera.use()

        score_text = f"Velocidad {round(self.player_sprite.change_x, 2)}, {round(self.player_sprite.change_y, 2)}"
        arcade.draw_text(
            score_text,
            10,
            self.window.height - 20,
            arcade.csscolor.RED,
            18,
        )

    def on_update(self, delta_time) -> None:
        self.physics_engine.update()
        self.player_sprite.update_player_position()
        self.scene.update_animation(
            delta_time, [ITEMS_LAYER, PLAYER_LAYER]
        )
        self.center_camera_to_player()

import arcade

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 350
SCREEN_TITLE = "Garoa"

TILE_SCALING = 0.5
CHARACTER_SCALING = TILE_SCALING * 4
SPRITE_SCALING_BULLET = 1
INDICATOR_BAR_OFFSET = 32
SPRITE_PIXEL_SIZE = 64
GRID_PIXEL_SIZE = SPRITE_PIXEL_SIZE * TILE_SCALING

MOVEMENT_SPEED = 3

PLAYER_START_X = 4
PLAYER_START_Y = 25

PLAYER_LAYER = "Player"
BACKGROUND_LAYER = "Background"
TREES_LAYER = "Trees"
ITEMS_LAYER = "Items"

DEAD_ZONE = 0.2

KEY_MAPPING = {
    arcade.key.DOWN: "down",
    arcade.key.S: "down",
    arcade.key.LEFT: "left",
    arcade.key.A: "left",
    arcade.key.RIGHT: "right",
    arcade.key.D: "right",
    arcade.key.UP: "up",
    arcade.key.W: "up"
}
import arcade

SCREEN_WIDTH: int = 400
SCREEN_HEIGHT: int = 350
SCREEN_TITLE: str = "Garoa"

TILE_SCALING: float = 0.5
CHARACTER_SCALING: float = TILE_SCALING * 4
SPRITE_SCALING_BULLET: int = 1
INDICATOR_BAR_OFFSET: int = 32
SPRITE_PIXEL_SIZE: int = 64
GRID_PIXEL_SIZE: float = SPRITE_PIXEL_SIZE * TILE_SCALING

MOVEMENT_SPEED: int = 3

PLAYER_START_X: int = 4
PLAYER_START_Y: int = 25

PLAYER_LAYER: str = "Player"
BACKGROUND_LAYER: str = "Background"
TREES_LAYER: str = "Trees"
ITEMS_LAYER: str = "Items"

DEAD_ZONE: float = 0.2

KEY_MAPPING: dict[int, str] = {
    arcade.key.DOWN: "down",
    arcade.key.S: "down",
    arcade.key.LEFT: "left",
    arcade.key.A: "left",
    arcade.key.RIGHT: "right",
    arcade.key.D: "right",
    arcade.key.UP: "up",
    arcade.key.W: "up"
}

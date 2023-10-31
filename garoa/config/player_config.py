import arcade

from garoa.config import CHARACTER_SCALING, MOVEMENT_SPEED
from garoa.models import HealthBar

PLAYER_PARAMS = {
    "name_file": "player-sheet.png",
    "sprite_width": 12,
    "sprite_height": 18,
    "columns": 4,
    "count": 16,
    "scale": CHARACTER_SCALING,
    "speed": MOVEMENT_SPEED,
    "fpt": 1 / 8,
    "directions": ("down_walk", "left_walk", "right_walk",
                   "up_walk")
}

PLAYER_STATS = {
    "health": 5
}

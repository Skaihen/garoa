import math

import arcade

from models.character import Character
from utils.utils import CharacterParams

DEAD_ZONE = 0.2


class Player(Character):
    def __init__(self, character_params: CharacterParams):
        super().__init__(character_params)
        self.character_params = character_params
        joysticks = arcade.get_joysticks()
        self.character_walking_direct = {
            "down": False,
            "left": False,
            "right": False,
            "up": False
        }

        if joysticks:
            self.joystick = joysticks[0]
            self.joystick.open()
            self.joystick.push_handlers(self)
        else:
            self.joystick = None

    # noinspection PyMethodMayBeStatic
    def on_joybutton_press(self, _joystick, button):
        print("Button {} down".format(button))

    # noinspection PyMethodMayBeStatic
    def on_joybutton_release(self, _joystick, button):
        print("Button {} up".format(button))

    # noinspection PyMethodMayBeStatic
    def on_joyhat_motion(self, _joystick, hat_x, hat_y):
        print("Hat ({}, {})".format(hat_x, hat_y))

    def update_player_position(self):
        if self.joystick and (abs(self.joystick.x) > DEAD_ZONE or abs(self.joystick.y) > DEAD_ZONE):
            self.change_x = self.joystick.x * self.character_params["speed"] if abs(self.joystick.x) > DEAD_ZONE else 0
            self.change_y = -self.joystick.y * self.character_params["speed"] if abs(self.joystick.y) > DEAD_ZONE else 0
        else:
            self.change_x = ((self.character_walking_direct["right"] - self.character_walking_direct["left"]) *
                             self.character_params["speed"])
            self.change_y = ((self.character_walking_direct["up"] - self.character_walking_direct["down"]) *
                             self.character_params["speed"])
            if self.change_x != 0 and self.change_y != 0:
                self.change_x *= math.cos(math.pi / 4)
                self.change_y *= math.sin(math.pi / 4)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.DOWN or key == arcade.key.S:
            self.character_walking_direct["down"] = True
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.character_walking_direct["left"] = True
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.character_walking_direct["right"] = True
        elif key == arcade.key.UP or key == arcade.key.W:
            self.character_walking_direct["up"] = True

    def on_key_release(self, key, modifiers):
        if key == arcade.key.DOWN or key == arcade.key.S:
            self.character_walking_direct["down"] = False
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.character_walking_direct["left"] = False
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.character_walking_direct["right"] = False
        elif key == arcade.key.UP or key == arcade.key.W:
            self.character_walking_direct["up"] = False

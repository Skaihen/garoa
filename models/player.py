import math

import arcade

from models.character import Character
from utils.utils import CharacterParams, CharacterWalkingDirect

DEAD_ZONE = 0.1


class Player(Character):
    def __init__(self, character_params: CharacterParams):
        super().__init__(character_params)
        self.character_params = character_params
        joysticks = arcade.get_joysticks()

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

    def update_player_position(self, character_walking_direct: CharacterWalkingDirect):
        if self.joystick and (abs(self.joystick.x) > DEAD_ZONE or abs(self.joystick.y) > DEAD_ZONE):
            self.change_x = self.joystick.x * self.character_params["speed"] if abs(self.joystick.x) > DEAD_ZONE else 0
            self.change_y = -self.joystick.y * self.character_params["speed"] if abs(self.joystick.y) > DEAD_ZONE else 0
        else:
            self.change_x = ((character_walking_direct["right"] - character_walking_direct["left"]) *
                             self.character_params["speed"])
            self.change_y = ((character_walking_direct["up"] - character_walking_direct["down"]) *
                             self.character_params["speed"])
            if self.change_x != 0 and self.change_y != 0:
                self.change_x *= math.cos(math.pi / 4)
                self.change_y *= math.sin(math.pi / 4)

import math

import arcade

from garoa.config import KEY_MAPPING, DEAD_ZONE, INDICATOR_BAR_OFFSET
from garoa.models import Character
from garoa.utils import CharacterParams, CharacterStats


class Player(Character):
    def __init__(self, character_params: CharacterParams, character_stats: CharacterStats):
        super().__init__(character_params, character_stats)
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

    def is_joystick_active(self):
        return self.joystick and (abs(self.joystick.x) > DEAD_ZONE or abs(self.joystick.y) > DEAD_ZONE)

    def calculate_change(self, value):
        return value * self.character_params["speed"] if abs(value) > DEAD_ZONE else 0

    def update_player_position(self):
        if self.is_joystick_active():
            self.change_x = self.calculate_change(self.joystick.x)
            self.change_y = self.calculate_change(-self.joystick.y)
        else:
            self.change_x = self.calculate_change(
                self.character_walking_direct["right"] - self.character_walking_direct["left"])
            self.change_y = self.calculate_change(
                self.character_walking_direct["up"] - self.character_walking_direct["down"])

            if self.change_x != 0 and self.change_y != 0:
                angle = math.pi / 4
                self.change_x *= math.cos(angle)
                self.change_y *= math.sin(angle)

    def on_key_press(self, key, modifiers):
        direction = KEY_MAPPING.get(key)
        if direction:
            self.character_walking_direct[direction] = True

    def on_key_release(self, key, modifiers):
        direction = KEY_MAPPING.get(key)
        if direction:
            self.character_walking_direct[direction] = False

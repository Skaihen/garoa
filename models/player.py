import arcade

from models.character import Character
from utils.utils import CharacterParams

DEAD_ZONE = 0.05


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
            print("There are no joysticks, plug in a joystick and run again.")
            self.joystick = None

    def update(self):
        if self.joystick:
            self.change_x = self.joystick.x * self.character_params["speed"]
            if abs(self.change_x) < DEAD_ZONE:
                self.change_x = 0

            self.change_y = -self.joystick.y * self.character_params["speed"]
            if abs(self.change_y) < DEAD_ZONE:
                self.change_y = 0

        self.center_x += self.change_x
        self.center_y += self.change_y

    # noinspection PyMethodMayBeStatic
    def on_joybutton_press(self, _joystick, button):
        print("Button {} down".format(button))

    # noinspection PyMethodMayBeStatic
    def on_joybutton_release(self, _joystick, button):
        print("Button {} up".format(button))

    # noinspection PyMethodMayBeStatic
    def on_joyhat_motion(self, _joystick, hat_x, hat_y):
        print("Hat ({}, {})".format(hat_x, hat_y))

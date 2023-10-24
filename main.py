import os

import arcade
import yaml

from views.title_screen_view import TitleScreenView

with open("config/config.yml", "r") as file:
    config_service = yaml.safe_load(file)


def main():
    file_path = os.path.dirname(os.path.abspath(__file__))
    os.chdir(file_path)
    window = arcade.Window(config_service["SCREEN_WIDTH"], config_service["SCREEN_HEIGHT"],
                           config_service["SCREEN_TITLE"], vsync=False)
    window.center_window()
    title_screen_view = TitleScreenView()
    window.show_view(title_screen_view)
    arcade.run()


if __name__ == "__main__":
    main()

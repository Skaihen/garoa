import os

import arcade

from config import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE
from views import TitleScreenView


def main() -> None:
    file_path = os.path.dirname(os.path.abspath(__file__))
    os.chdir(file_path)
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT,

                           SCREEN_TITLE, vsync=False)
    window.center_window()
    title_screen_view = TitleScreenView()
    window.show_view(title_screen_view)
    arcade.run()


if __name__ == "__main__":
    main()

import os

import arcade

from views.title_screen_view import TitleScreenView

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 350
SCREEN_TITLE = "Garoa"


def main():
    file_path = os.path.dirname(os.path.abspath(__file__))
    os.chdir(file_path)
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, vsync=False)
    window.center_window()
    title_screen_view = TitleScreenView()
    window.show_view(title_screen_view)
    arcade.run()


if __name__ == "__main__":
    main()

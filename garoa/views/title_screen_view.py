import arcade

from garoa.config.config import SCREEN_WIDTH, SCREEN_HEIGHT
from garoa.views.game_view import GameView


class TitleScreenView(arcade.View):
    def on_show_view(self) -> None:
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self) -> None:
        self.clear()
        arcade.draw_text("Menu Screen - click to advance", SCREEN_WIDTH / 2,
                         SCREEN_HEIGHT / 2, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers) -> None:
        game_view = GameView()
        game_view.setup()
        self.window.show_view(game_view)
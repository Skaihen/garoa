import arcade
import yaml

from views.game_view import GameView

with open("config/config.yml", "r") as file:
    config_service = yaml.safe_load(file)


class TitleScreenView(arcade.View):
    def on_show_view(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        self.clear()
        arcade.draw_text("Menu Screen - click to advance", config_service["SCREEN_WIDTH"] / 2,
                         config_service["SCREEN_HEIGHT"] / 2, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = GameView()
        game_view.setup()
        self.window.show_view(game_view)

import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Garoa"

CHARACTER_SCALING = 1
TILE_SCALING = 0.5


class Garoa(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.player_list = None
        self.player_sprite = None

        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.player_sprite = arcade.AnimatedTimeBasedSprite()
        self.player_sprite.textures = []

        self.player_sprite.textures.append(
            arcade.load_texture("assets/sprites/player-sheet.png", x=0, y=0, width=12, height=18))

    def on_draw(self):
        self.clear()


def main():
    window = Garoa()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()

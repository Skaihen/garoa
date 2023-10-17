import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Garoa"

CHARACTER_SCALING = 1
TILE_SCALING = 2

PLAYER_MOVEMENT_SPEED = 5


class Garoa(arcade.Window):
    def __init__(self, width, height, title, vsync):
        super().__init__(width, height, title, vsync)

        self.scene = None
        self.player_sprite = None
        self.physics_engine = None

        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

    def setup(self):
        self.scene = arcade.Scene()

        self.player_sprite = arcade.Sprite("assets/sprites/player-sheet.png", CHARACTER_SCALING)
        self.player_sprite.center_x = 12 * CHARACTER_SCALING
        self.player_sprite.center_y = 18 * CHARACTER_SCALING

        self.scene.add_sprite("Player", self.player_sprite)

        wall = arcade.Sprite("assets/sprites/player-sheet.png", TILE_SCALING)
        wall.center_x = 200
        wall.center_y = 200
        self.scene.add_sprite("Walls", wall)

        # self.player_sprite.textures = []
        #
        # self.player_sprite.textures.append(
        #     arcade.load_texture("assets/sprites/player-sheet.png", x=0, y=0, width=12, height=18))

        self.physics_engine = arcade.PhysicsEngineSimple(
            self.player_sprite, self.scene.get_sprite_list("Walls")
        )

    def on_draw(self):
        self.clear()
        self.scene.draw(pixelated=True)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.W:
            self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.W:
            self.player_sprite.change_y = 0
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        self.physics_engine.update()


def main():
    window = Garoa(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, False)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()

import random
import arcade


class Spaceship(arcade.Sprite):
    def __init__(self, game):
        super().__init__(":resources:images/space_shooter/playerShip1_blue.png")
        self.center_x = game.width // 2
        self.center_y = 50
        self.width = 60
        self.height = 60
        self.speed = 20


class Enemy(arcade.Sprite):
    def __init__(self, game):
        super().__init__(":resources:images/space_shooter/playerShip3_orange.png")
        self.center_x = random.randint(0, game.width)
        self.center_y = game.height + 30
        self.width = 60
        self.height = 60
        self.angle = 180
        self.speed = 3


class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=680, height=720, title="star's game")
        arcade.set_background_color(arcade.color.SMOKY_BLACK)
        self.background = arcade.load_texture(
            ":resources:images/backgrounds/stars.png")
        self.space_ship = Spaceship(self)
        self.enemy = Enemy(self)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(
            0, 0, self.width, self.height, self.background)

        self.space_ship.draw()
        self.enemy.draw()

    def on_key_press(self, symbol, modifiers: int):
        print("a key pressed")

        if symbol == 97 or symbol == 65361:  # left
            self.space_ship.center_x -= self.space_ship.speed

        elif symbol == 100 or symbol == 65363:  # right
            self.space_ship.center_x += self.space_ship.speed

        elif symbol == 115 or symbol == 65364:
            self.space_ship.center_x = self.width // 2


    def on_update(self, delta_time):
        self.enemy.center_y -= self.enemy.speed


window = Game()

arcade.run()

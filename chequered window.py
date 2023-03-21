import arcade


class Chequered_window(arcade.Window):
    def __init__(self):
        super().__init__(width=400, height=400, title="chequered window")
        arcade.set_background_color(arcade.color.WHITE)
        self.column_spacing = 20
        self.row_spacing = 20
        self.left_margin = 110
        self.bottom_margin = 110

    def on_draw(self):
        arcade.start_render()

        for row in range(10):
            counter = 1
            for column in range(10):
                x = column * self.column_spacing + self.left_margin
                y = row * self.row_spacing + self.bottom_margin

                if counter % 2 == 1:
                    if row % 2 == 0:
                        arcade.draw_circle_filled(x, y, 7, arcade.color.RED)

                    elif row % 2 == 1:
                        arcade.draw_circle_filled(x, y, 7, arcade.color.BLUE)

                    counter += 1

                elif counter % 2 == 0:
                    if row % 2 == 0:
                        arcade.draw_circle_filled(x, y, 7, arcade.color.BLUE)

                    elif row % 2 == 1:
                        arcade.draw_circle_filled(x, y, 7, arcade.color.RED)

                    counter += 1


window = Chequered_window()
arcade.run()

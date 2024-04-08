import arcade
class craftmine(arcade.Window):
    def __init__(self):
        super ().__init__(500,500,"craftmine")
        arcade.set_background_color(arcade.color.SKY_BLUE)
        self.bolckliste = arcade.SpriteList()#
        self.blockgas = arcade.Sprite("blockgras.png")
        self.blockgas.center_x = 475
        self.blockgas.center_y = 175
        self.bolckliste.append(self.blockgas)
        self.blockgas1 = arcade.Sprite("blockgras.png")
        self.blockgas1.center_x = 425
        self.blockgas1.center_y = 175
        self.bolckliste.append(self.blockgas1)
    def on_draw(self):
        self.clear()
        self.bolckliste.draw()
craftmine()
arcade.run()
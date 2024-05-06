import arcade

class Craftmine(arcade.Window):
    def __init__(self):
        super ().__init__(500,500,"craftmine")
        arcade.set_background_color(arcade.color.ZINNWALDITE_BROWN)
        self.bolckliste = arcade.SpriteList()#blöcke
        self.blockgas = arcade.Sprite("blockgras.png")
        self.blockgas.center_x = 475
        self.blockgas.center_y = 175
        self.bolckliste.append(self.blockgas)
        self.blockgas1 = arcade.Sprite("blockgras.png")
        self.blockgas1.center_x = 425
        self.blockgas1.center_y = 175
        self.bolckliste.append(self.blockgas1)
        self.rafl_der_Iliste = arcade.SpriteList()
        self.rafl_I = arcade.Sprite("rafl_der_I.png",1.89)
        self.rafl_I.center_x = 475
        self.rafl_I.center_y = 294
        self.rafl_der_Iliste.append(self.rafl_I)
    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.A:
            self.rafl_I.change_x=-15
        
        
    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        sprite = arcade.Sprite()
        sprite.center_x = x
        sprite.center_y = y
        sprite.set_hit_box([(1, 1), (-1, 1), (-1, -1), (1, -1)])
        if arcade.check_for_collision(sprite,self.blockgas):
            self.blockgas.kill()
    def on_draw(self):
        self.clear()
        self.bolckliste.draw()
        self.rafl_der_Iliste.draw()
    def on_update(self,delta_time):
        self.bolckliste.update()

Craftmine()
arcade.run()
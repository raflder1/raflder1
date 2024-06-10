import arcade
class Jump(arcade.Window):
    def __init__(self):
        super ().__init__(500,500,"Jump um zu entkommen!")

        arcade.set_background_color(arcade.color.WHITE)
    def setup(self):
        #Listen
        self.spielerliste = arcade.SpriteList()


        #Sprites
        

        









Jump()
arcade.run()
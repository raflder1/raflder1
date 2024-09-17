import arcade
class franz(arcade.Window):
    def __init__(self):
        super ().__init__(500,500,"spreche nach")

        arcade.set_background_color(arcade.color.GRAY)
audio = arcade.load_sound(".wav",False)  


arcade.play_sound(audio,1.0,-1,False) 





franz()
arcade.run()
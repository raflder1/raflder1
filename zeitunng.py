import arcade
class Zeitung(arcade.Window):
    def __init__(self):
        super ().__init__(500,500,"in der zeit der ung")

        arcade.set_background_color(arcade.color.RED)

        self.zeitliste=arcade.SpriteList()

        self.estilleips = arcade.SpriteList()

        self.ungzeit = arcade.Sprite("ungzeit.png")
        self.ungzeit.center_x = 150
        self.ungzeit.center_y = 250
        self.zeitliste.append(self.ungzeit)

        self.versteckliste = arcade.SpriteList()
        
        self.Palme = arcade.Sprite("palme.png")
        self.Palme.center_x = 370
        self.Palme.center_y = 209
        self.versteckliste.append(self.Palme)
        
        

        












        self.releips = arcade.Sprite("bigbruder.png",2)
        self.releips.center_x = 250
        self.releips.center_y = 250
        self.estilleips.append(self.releips)
        self.unge = arcade.Sprite("ungespielt.png")
        self.unge.center_x = 2444444444
        self.unge.center_y = 2345678
        self.zeitliste.append(self.unge)
    def on_key_press(self,symbol,modifiers):
        if symbol == arcade.key.ESCAPE:
            arcade.close_window()
        elif symbol == arcade.key.W:
            self.releips.change_x= -3
        elif symbol == arcade.key.S:
            self.releips.change_y=3
        elif symbol == arcade.key.SPACE:
            self.releips.change_x=1
      #  elif symbol == arcade.key.A:
      #      self.spieler.change_x=-15
     ##   elif symbol == arcade.key.Q:
    # ##       self.bombe.set_position(275,325)
      ##  elif symbol == arcade.key.E:
          #  self.inv.set_position(2501,2501)
        #elif symbol == arcade.key.Z:
         #   self.sog.change_y = 10

    #taste loslassen
    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.W:
            self.releips.change_x = 0
        elif symbol == arcade.key.S:
             self.releips.change_y = 0
        elif symbol == arcade.key.SPACE:
            self.releips.change_x = -1
    #clicks
    def on_mouse_press(self, x, y, button, modifiers):
        sprite = arcade.Sprite()
        sprite.center_x = x
        sprite.center_y = y
        sprite.set_hit_box([(1, 1), (-1, 1), (-1, -1), (1, -1)])
        
            
        


        #truhe öffnen
        
            
    #maus:bewegungen
   # def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        

    def on_update(self, delta_time):
        self.estilleips.update()
        
        if arcade.check_for_collision(self.releips,self.ungzeit):
            self.unge.position=(250,250)
            


    


        
         


        #zeichnen
    def on_draw(self):
        self.clear()
        self.zeitliste.draw()
        self.estilleips.draw()
        self.versteckliste.draw()
        #tuff tuff tuff die eisenbahn🚄
        
        #arcade.play_sound(audio,1.0,-1,False) 






Zeitung()
arcade.run()
#todo ein weiterres featcher ins spiel einbauen bis 15.04.2034

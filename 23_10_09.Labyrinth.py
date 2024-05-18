import arcade
class Labyrinth(arcade.Window):
    def __init__(self):
        super ().__init__(500,500,"labyrinth")

        arcade.set_background_color(arcade.color.RED)

        self.enderliste = arcade.SpriteList()
        self.blockliste = arcade.SpriteList()
        self.inventarliste = arcade.SpriteList()
        self.lebensliste = arcade.SpriteList()
        self.werfliste = arcade.SpriteList()
<<<<<<< HEAD
=======

        self.setup()

>>>>>>> a2c4043e7e934dbe271737b53b3d2970be3d091f
    def setup(self):
        #inv
        self.inv = arcade.Sprite("truheninventar.png")
        self.inv.center_x = 25000
        self.inv.center_y = 25000
        self.inventarliste.append(self.inv)
        #enderperle
        self.perle = arcade.Sprite("enderperle.png",4)
        self.perle.center_x = 25000
        self.perle.center_y = 25000
        self.inventarliste.append(self.perle)
        #truhe
        self.truhe = arcade.Sprite("truhe.png")
        self.truhe.center_x = 375
        self.truhe.center_y = 25
        self.blockliste.append(self.truhe)
        #zug
        self.sogliste = arcade.SpriteList()

        self.sog = arcade.Sprite("achtung.png",20)
        self.sog.center_x = 250
        self.sog.center_y= 250
        self.sogliste.append(self.sog)
        #blöcke
        block =arcade.Sprite("tresor.png",3)
        block.center_x=125
        block.center_y=475
        self.blockliste.append(block)

        block =arcade.Sprite("meer+strand.png") 
        block.center_x=175
        block.center_y=25
        self.blockliste.append(block)

        block =arcade.Sprite("meer+strand.png")
        block.center_x=425
        block.center_y=25
        self.blockliste.append(block)

        block =arcade.Sprite("meer+strand.png")
        block.center_x=223
        block.center_y=25
        self.blockliste.append(block)

        block =arcade.Sprite("meer+strand.png")
        block.center_x=475
        block.center_y=25
        self.blockliste.append(block)

        block =arcade.Sprite("meer+strand.png")
        block.center_x=275
        block.center_y=25
        self.blockliste.append(block)

        block =arcade.Sprite("meer+strand.png")
        block.center_x=25
        block.center_y=25
        self.blockliste.append(block)
        
        block =arcade.Sprite("meer+strand.png")
        block.center_x=25
        block.center_y=75
        self.blockliste.append(block)
        
        block =arcade.Sprite("meer+strand.png")
        block.center_y=25
        block.center_x=125
        self.blockliste.append(block)

        block =arcade.Sprite("meer+strand.png")
        block.center_x=25
        block.center_y=175
        self.blockliste.append(block)

        block =arcade.Sprite("meer+strand.png")
        block.center_x=25
        block.center_y=225
        self.blockliste.append(block)

        block =arcade.Sprite("meer+strand.png")
        block.center_x=25
        block.center_y=275
        self.blockliste.append(block)

        block =arcade.Sprite("meer+strand.png")
        block.center_x=25
        block.center_y=325
        self.blockliste.append(block)

        block =arcade.Sprite("meer+strand.png")
        block.center_x=25
        block.center_y=375
        self.blockliste.append(block)

        block =arcade.Sprite("meer+strand.png")
        block.center_x=25
        block.center_y=425
        self.blockliste.append(block)

        block =arcade.Sprite("meer+strand.png")
        block.center_x=25
        block.center_y=475
        self.blockliste.append(block)
        
        block =arcade.Sprite("meer+strand.png")
        block.center_x=175
        block.center_y=475
        self.blockliste.append(block)

        block =arcade.Sprite("meer+strand.png")
        block.center_x=225
        block.center_y=475
        self.blockliste.append(block)

        self.geist = arcade.SpriteList()

        self.geisti = arcade.Sprite("goustblock.png")
        self.geisti.center_x = -500
        self.geisti.center_y = 250
        self.geist.append(self.geisti)

        block =arcade.Sprite("meer+strand.png")
        block.center_x=275
        block.center_y=475
        self.blockliste.append(block)

        block =arcade.Sprite("meer+strand.png")
        block.center_x=325
        block.center_y=475
        self.blockliste.append(block)

        block =arcade.Sprite("meer+strand.png")
        block.center_x=375
        block.center_y=475
        self.blockliste.append(block)

        block =arcade.Sprite("meer+strand.png")
        block.center_x=425
        block.center_y=475
        self.blockliste.append(block)

        block =arcade.Sprite("meer+strand.png")
        block.center_x=475
        block.center_y=475
        self.blockliste.append(block)

        block =arcade.Sprite("meer+strand.png")
        block.center_x=475
        block.center_y=425
        self.blockliste.append(block)

        block =arcade.Sprite("meer+strand.png")
        block.center_x=475 
        block.center_y=375
        self.blockliste.append(block)

        block =arcade.Sprite("meer+strand.png")
        block.center_x=475
        block.center_y=325
        self.blockliste.append(block)

        block =arcade.Sprite("meer+strand.png")
        block.center_x=475
        block.center_y=275
        self.blockliste.append(block)

        block =arcade.Sprite("meer+strand.png")
        block.center_x=475
        block.center_y=225
        self.blockliste.append(block)

        block =arcade.Sprite("meer+strand.png")
        block.center_x=475
        block.center_y=175
        self.blockliste.append(block)

        block =arcade.Sprite("meer+strand.png")
        block.center_x=475
        block.center_y=125
        self.blockliste.append(block)

        herz =arcade.Sprite("herz.png")
        herz.center_x=475
        herz.center_y=125
        self.lebensliste.append(herz)

        block =arcade.Sprite("meer+strand.png")
        block.center_x=475
        block.center_y=75
        self.blockliste.append(block)
    

        block =arcade.Sprite("meer+strand.png")
        block.center_x=425
        block.center_y=75
        self.blockliste.append(block)

        cola =arcade.Sprite("heiße_party.png")
        cola.center_x=275
        cola.center_y=25
        self.blockliste.append(cola)

        block =arcade.Sprite("meer+strand.png")
        block.center_x=275
        block.center_y=75
        self.blockliste.append(block)

        block =arcade.Sprite("meer+strand.png")
        block.center_x=225
        block.center_y=125
        self.blockliste.append(block)
        block =arcade.Sprite("meer+strand.png")

        block.center_x=275
        block.center_y=125
        self.blockliste.append(block)

        block =arcade.Sprite("meer+strand.png")
        block.center_x=325
        block.center_y=125
        self.blockliste.append(block)

        block =arcade.Sprite("meer+strand.png")
        block.center_x=325
        block.center_y=175
        self.blockliste.append(block)

        block =arcade.Sprite("meer+strand.png")
        block.center_x=375
        block.center_y=175
        self.blockliste.append(block)

        block =arcade.Sprite("meer+strand.png")
        block.center_x=75
        block.center_y=75
        self.blockliste.append(block)

        block =arcade.Sprite("meer+strand.png")
        block.center_x=125
        block.center_y=75
        self.blockliste.append(block)

        block =arcade.Sprite("meer+strand.png")
        block.center_x=125
        block.center_y=125
        self.blockliste.append(block)

        block =arcade.Sprite("meer+strand.png")
        block.center_x=75
        block.center_y=175
        self.blockliste.append(block)

        block =arcade.Sprite("meer+strand.png")
        block.center_x=75
        block.center_y=125
        self.blockliste.append(block)

        block =arcade.Sprite("meer+strand.png")
        block.center_x=375
        block.center_y=425
        self.blockliste.append(block)

        block =arcade.Sprite("meer+strand.png")
        block.center_x=375
        block.center_y=375
        self.blockliste.append(block)

        block =arcade.Sprite("meer+strand.png")
        block.center_x=375
        block.center_y=325
        self.blockliste.append(block)

 #       self.mauernliste = arcade.SpriteList()
  #      self.maur = arcade.Sprite("mauer.png")
#        self.maur.center_x = 

        block =arcade.Sprite("meer+strand.png")
        block.center_x=375
        block.center_y=275
        self.blockliste.append(block)

        block =arcade.Sprite("meer+strand.png")
        block.center_x=325
        block.center_y=275
        self.blockliste.append(block)

        block =arcade.Sprite("meer+strand.png")
        block.center_x=275
        block.center_y=275
        self.blockliste.append(block)
        
        block =arcade.Sprite("meer+strand.png")
        block.center_x=225
        block.center_y=225
        self.blockliste.append(block)

        block =arcade.Sprite("meer+strand.png")
        block.center_x=175
        block.center_y=225
        self.blockliste.append(block)

        block =arcade.Sprite("meer+strand.png")
        block.center_x=125
        block.center_y=275
        self.blockliste.append(block)

        block =arcade.Sprite("meer+strand.png")
        block.center_x=175
        block.center_y=325
        self.blockliste.append(block)

        block =arcade.Sprite("meer+strand.png")
        block.center_x=125
        block.center_y=375
        self.blockliste.append(block)
        #start
        #self.startliste = arcade.SpriteList
#
 ##       self.start = arcade.Sprite("start_lebutton.png")
      #  self.start.center_x = 250
   ##     self.start.center_y = 250
     #   self.startliste.append(self.start)
        #verloren
        self.verloren_schild =arcade.Sprite("win.png",2)
        self.verloren_schild.center_x=7515365535654523
        self.verloren_schild.center_y=700
        self.blockliste.append(self.verloren_schild)      
        #win
        self.win_schild =arcade.Sprite("win.png",2)
        self.win_schild.center_x=7515365535654523
        self.win_schild.center_y=700
        self.blockliste.append(self.win_schild)

        self.gewonnenliste=arcade.SpriteList()

        win=arcade.Sprite("meer+strand.png")
        win.center_x=75
        win.center_y=525
        self.gewonnenliste.append(win)
        #monster
        self.monsterliste = arcade.SpriteList()

        self.spinner = arcade.Sprite("spinner.png",0.18)
        self.spinner.center_x = 225
        self.spinner.center_y = 750
        self.monsterliste.append(self.spinner)
        #spieler
        self.spielerliste = arcade.SpriteList()

        self.spieler =arcade.Sprite("spieler.png")
        self.spieler.center_x=325
        self.spieler.center_y=25
        self.spielerliste.append(self.spieler)
        #phsikengine
        self.physik_engine=arcade.PhysicsEngineSimple(self.spieler,self.blockliste)

        #gegenstände
        self.gegenstandliste=arcade.SpriteList()
        self.tor=arcade.Sprite("tor.png")
        self.tor.center_x=75
        self.tor.center_y=475
        self.blockliste.append(self.tor)

        self.dia=arcade.Sprite("diamant.png")
        self.dia.center_x=175
        self.dia.center_y=275
        self.gegenstandliste.append(self.dia)

        self.münze=arcade.Sprite("münze.png")
        self.münze.center_x=425
        self.münze.center_y=425
        self.gegenstandliste.append(self.münze)
        #bombe
        self.schussliste = arcade.SpriteList()
        self.bombe = arcade.Sprite("bombe.png")
        self.bombe.center_x = 234567
        self.bombe.center_y =123
        self.schussliste.append(self.bombe)
        #maus
        self.mouseliste=arcade.SpriteList()
        self.fadenkreuz=arcade.Sprite("fadenkreuz.png", 5)
        self.fadenkreuz.center_x=-10
        self.fadenkreuz.center_y=-10
        self.mouseliste.append(self.fadenkreuz)
        self.geist = arcade.SpriteList()

        self.geisti = arcade.Sprite("goustblock.png")
        self.geisti.center_x = -500
        self.geisti.center_y = 250
        self.geist.append(self.geisti)
        #countdowns
        self.zeit = 11
        self.kill_zeit = 2
        self.explosions_zeit = 1
    #taste drücken
    def on_key_press(self,symbol,modifiers):
        if symbol == arcade.key.W:
            self.spieler.change_y=15
        elif symbol == arcade.key.S:
            self.spieler.change_y=-15
        elif symbol == arcade.key.D:
            self.spieler.change_x=15
        elif symbol == arcade.key.A:
            self.spieler.change_x=-15
        elif symbol == arcade.key.Q:
            self.bombe.set_position(275,325)
        elif symbol == arcade.key.ESCAPE:
            arcade.close_window()
        elif symbol == arcade.key.E:
            self.inv.set_position(2501,2501)
<<<<<<< HEAD
        elif symbol == arcade.key.R:
            self.setup()
=======
        elif symbol == arcade.key.Z:
            self.sog.change_y = 10
>>>>>>> a2c4043e7e934dbe271737b53b3d2970be3d091f

    #taste loslassen
    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.W:
            self.spieler.change_y = 0
        elif symbol == arcade.key.S:
            self.spieler.change_y = 0
        elif symbol == arcade.key.D:
            self.spieler.change_x = 0
        elif symbol == arcade.key.A:
            self.spieler.change_x= 0
    #clicks
    def on_mouse_press(self, x, y, button, modifiers):
        sprite = arcade.Sprite()
        sprite.center_x = x
        sprite.center_y = y
        sprite.set_hit_box([(1, 1), (-1, 1), (-1, -1), (1, -1)])
        if self.perle not in self.inventarliste and self.perle in self.werfliste:
            self.spieler.position=(250,250)
            
        


        #truhe öffnen
        if arcade.check_for_collision(sprite, self.truhe):
            self.inv.position = (250,250)
            self.perle.position = (250,250)
            self.inventarliste.remove(self.perle)
            self.werfliste.append(self.perle)
            ...
        #perle --> hotpar
        if arcade.check_for_collision(sprite, self.perle):
            self.perle.position = (275,25)
            self.perle.scale = 0.7
            self.spieler.texture = arcade.load_texture("bigbruder.png")


        if arcade.check_for_collision(self.spieler,self.spinner):
            print("spinne,spinne!")

            ...
        if arcade.check_for_collision(self.sog,self.spieler):
            self.spieler.position(325,25)
            ...
    #maus:bewegungen
    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        self.fadenkreuz.center_x = x
        self.fadenkreuz.center_y = y
        





    #updates
    def on_update(self,delta_time):
        #zeit
        self.zeit = self.zeit - delta_time
        if self.zeit <= 0:
            arcade.draw_text("Verloren",250,250,font_size=18,font_name="Kenney Blocks")
            
        #updates
        self.physik_engine.update()
        self.win_schild.update()
        self.spielerliste.update()

        #spieler exportieren
        if self.inv.center_x > 251 and self.spieler not in self.enderliste and self.spieler in self.spielerliste:
            self.spielerliste.remove(self.spieler)
            self.enderliste.append(self.spieler)


        #münze
        if arcade.check_for_collision(self.spieler,self.münze):
            self.münze.kill()
        #tor öffnung
        if self.dia not in self.gegenstandliste and self.münze not in self.gegenstandliste and self.tor not in self.gegenstandliste and self.tor  in  self.blockliste:
            self.blockliste.remove(self.tor)
            self.gegenstandliste.append(self.tor)

        

        #gewonnen & verloren
        if arcade.check_for_collision_with_list(self.spieler,self.gewonnenliste):
            self.win_schild.position = (250, 250)
            self.kill_zeit=self.kill_zeit - delta_time
            if self.kill_zeit <= 0:
                arcade.draw_text("VERLOREN, PROBIERE ES NOCH MAL",0,0,250,250,font_name="Kenny Blocks",font_size=18)
                arcade.draw_text("DRÜCKE R FÜR NOCHMAL!",0,0,250,240,font_name="Kenny Blocks",font_size=18)

        #diamant 
        if arcade.check_for_collision(self.spieler,self.dia):
             self.dia.kill()
        #bombe
        if arcade.check_for_collision(self.spieler,self.bombe):
            self.bombe.texture = arcade.load_textures("explosion.png")


        if arcade.check_for_collision(self):
            self.herz.textures = arcade.load_texture("totherz.png")
            self.spieler.kill()
        
         


        #zeichnen
    def on_draw(self):
        self.clear()
        #tuff tuff tuff die eisenbahn🚄
        self.sogliste.draw()
        #start
        #self.startliste.draw()
        #blöcke
        self.blockliste.draw()
        #inventar
        self.inventarliste.draw()
        #bombe
        self.schussliste.draw()
        #gegenstände
        self.gegenstandliste.draw()
        #werfen
        self.werfliste.draw()
        #monster
        self.monsterliste.draw()
        #leben
        self.lebensliste.draw()
        #spieler
        self.spielerliste.draw(pixelated=True)
        self.enderliste.draw()
        #maus
        self.mouseliste.draw()
        arcade.draw_text(round(self.zeit), 440,475, font_size=18,font_name="Kenney Blocks")
        arcade.draw_text("Zeiqwerzuikoloiuztzuzgfghjuhgfghiuzfdfztfdxfzu8uztfdft787trfdtzugtfdsysdfdyhallofghjuhgfduijhgfdjhgfduzgfzuzgtfdzuzgtfuihgijuhjolkmlpölkmknknechtjiolkjhkjmnkolkijnjit:",150,475, font_size=6,font_name="Kenney Blocks")
        #audio = arcade.load_sound("hintergrundmusik.wav",False) 


        #arcade.play_sound(audio,1.0,-1,False) 






Labyrinth()
arcade.run()
#todo ein weiterres featcher ins spiel einbauen bis 15.04.2034

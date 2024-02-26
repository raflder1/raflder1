import arcade

arcade.open_window(500,500,"zeichnen")
arcade.set_background_color(arcade.color.FERRARI_RED)
#arcade.draw_rectangle_filled(350,300,100,100,arcade.color.BLUE)
arcade.start_render()

arcade.draw_rectangle_filled(250,250,300,300,arcade.color.YELLOW)
arcade.draw_rectangle_filled(250,250,100,100,arcade.color.BLUE)
arcade.draw_rectangle_filled(350,350,100,100,arcade.color.BLUE)
arcade.draw_rectangle_filled(150,150,100,100,arcade.color.BLUE)
arcade.draw_rectangle_filled(350,150,100,100,arcade.color.BLUE)
arcade.draw_rectangle_filled(150,350,100,100,arcade.color.BLUE)
arcade.draw_text("G",250,250,arcade.color.WHITE,50,anchor_x="center",anchor_y="center")
arcade.draw_rectangle_filled(0,100,100,100,100,0,arcade.color.GOLD)
arcade.draw_rectangle_filled(400,100,500,100,400,0,arcade.color.GOLD)  
arcade.finish_render()
arcade.run()
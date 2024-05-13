import arcade

# Öffnet ein Fenster der Breite 600, der Höhe 600 und mit dem Titel "Koordinatensystem"
arcade.open_window(600, 600, "Koordinatensystem", True)

# Wir setzen die Hintergrundfarbe auf Weiß (WHITE)
arcade.set_background_color(arcade.color.ALICE_BLUE)
arcade.set_background_color(arcade.color.AMAZON)

# Wir beginnen das Zeichnen der im Fenster vorkommenden Dinge
arcade.start_render()
arcade.draw_points
# Horizontale Linien
# Eine Linie von (x=0, y=60) nach (x=600, y=60) in der Farbe Schwarz
arcade.draw_line(0, 60, 600, 60, arcade.color.BLACK)
# Eine Linie von (x=0, y=120) nach (x=600, y=120) in der Farbe Schwarz
arcade.draw_line(0, 120, 600, 120, arcade.color.BLACK)
arcade.draw_line(0, 180, 600, 180, arcade.color.BLACK)
arcade.draw_line(0, 240, 600, 240, arcade.color.BLACK)
arcade.draw_line(0, 300, 540, 300, arcade.color.RED, 5)
arcade.draw_line(0, 360, 600, 360, arcade.color.BLACK)
arcade.draw_line(0, 420, 600, 420, arcade.color.BLACK)
arcade.draw_line(0, 480, 600, 480, arcade.color.BLACK)
arcade.draw_line(0, 540, 600, 540, arcade.color.BLACK)

# Vertikale Linien
arcade.draw_line(60, 0, 60, 600, arcade.color.BLACK)
arcade.draw_line(120, 0, 120, 600, arcade.color.BLACK)
arcade.draw_line(180, 0, 180, 600, arcade.color.BLACK)
arcade.draw_line(240, 0, 240, 600, arcade.color.BLACK)
arcade.draw_line(300, 0, 300, 540, arcade.color.RED, 5)
arcade.draw_line(360, 0, 360, 600, arcade.color.PURPLE)
arcade.draw_line(420, 0, 420, 600, arcade.color.YELLOW)
arcade.draw_line(480, 0, 480, 600, arcade.color.RED)
arcade.draw_line(540, 0, 540, 600, arcade.color.RED)
arcade.draw_line(60, 280, 60, 320, arcade.color.RED,5)
arcade.draw_line(120,280  ,120 ,320,arcade.color.RED,5)
arcade.draw_line(180,280,180,320,arcade.color.RED,5)
arcade.draw_line(240,280,240,320,arcade.color.RED,5)
arcade.draw_line(300,280,300,320,arcade.color.RED,5)
arcade.draw_line(360,280,360,320,arcade.color.RED,5)
arcade.draw_line(420,280,420,320,arcade.color.RED,5)
arcade.draw_line(480,280,480,320,arcade.color.RED,5)
arcade.draw_line(540,280,540,320,arcade.color.RED,5)
arcade.draw_line(280,60,320,60,arcade.color.RED,5)
arcade.draw_line(280,120,320,120,arcade.color.RED,5)
arcade.draw_line(280,180,320,180,arcade.color.RED,5)
arcade.draw_line(280,240,320,240,arcade.color.RED,5)
arcade.draw_line(280,300,320,300,arcade.color.RED,5)
arcade.draw_line(280,360,320,360,arcade.color.RED,5)
arcade.draw_line(280,420,320,420,arcade.color.RED,5)
arcade.draw_line(280,480,320,480,arcade.color.RED,5)
arcade.draw_line(280,540,320,540,arcade.color.RED,5)
arcade.draw_triangle_filled(540,280,540,320,600,300,arcade.color.RED)
arcade.draw_triangle_filled(320,540,280,540,300,600,arcade.color.RED)
arcade.draw_text(-4,260,60,arcade.color.FERRARI_RED ,anchor_y="center")
arcade.draw_text(-2,260,180,arcade.color.FERRARI_RED ,anchor_y="center")
arcade.draw_text(-1,260,240,arcade.color.FERRARI_RED ,anchor_y="center")
arcade.draw_text(-3,260,120,arcade.color.FERRARI_RED ,anchor_y="center")
arcade.draw_text(0,280,280,arcade.color.FERRARI_RED ,anchor_y="center")
arcade.draw_text(1,360,260,arcade.color.FERRARI_RED ,anchor_y="center")
arcade.draw_text(2,420,260,arcade.color.FERRARI_RED ,anchor_y="center")
arcade.draw_text(3,480,260,arcade.color.FERRARI_RED ,anchor_y="center")
arcade.draw_text(-4,60,260,arcade.color.FERRARI_RED ,anchor_y="center")
arcade.draw_text(-3,120,260,arcade.color.FERRARI_RED,anchor_y="center")
arcade.draw_text(-2,180,260,arcade.color.FERRARI_RED,anchor_y="center")

arcade.draw_line


# Wir beenden das Zeichnen der im Fenster vorkommenden Dinge
arcade.finish_render()

# Wir starten das Spiel
arcade.run()
import gamepie
import RPGassets

# --- inicializace okna, kamery, objektů, hráče ---
screen = gamepie.Window(title="Test", flags=gamepie.RESIZABLE)
fps = gamepie.Clock(60)

# textury
tree_texture = gamepie.load.Texture("tree")
bush_texture = gamepie.load.Texture("bush")
avatar_texture = gamepie.load.Texture("avatar")

# kamera
camera = gamepie.Camera(position=(0,0), zoom=3, anchor="center")

# objekty
objects = []

grid_size = 32
rows, cols = 10, 10
start_x = -grid_size * cols // 2
start_y = -grid_size * rows // 2
for row in range(rows):
    for col in range(cols):
        choice = gamepie.rand.randchoice(["tree", "bush", "empty", "empty"])
        pos = (start_x + col * grid_size, start_y + row * grid_size)
        if choice == "tree":
            obj = gamepie.draw.Image(screen, texture=tree_texture, position=pos,
                                     anchor=gamepie.CENTER, size=(32,64), camera=camera)
            objects.append(obj)
        elif choice == "bush":
            obj = gamepie.draw.Image(screen, texture=bush_texture, position=pos,
                                     anchor=gamepie.CENTER, size=(32,32), camera=camera)
            objects.append(obj)

# hráč
player = gamepie.draw.Image(screen, avatar_texture, camera=camera, size=(32,36))

controller = RPGassets.RPGController(player, camera, objects, speed=0.05)
controller.c_key_enabled = True  # klávesa C funguje

# --- hlavní loop ---
def update():
    dt = fps.tick()
    
    # update controlleru
    controller.update(dt)

    # vykreslení
    screen.fill((0,80,0))
    for obj in objects:
        obj.draw()
    player.draw()
    screen.flip()

screen.run()
gamepie.quit()

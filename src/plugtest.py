import gamepie


screen = gamepie.Window(title="Test")
fps = gamepie.Clock(60)

# textury
tree_texture = gamepie.load.Texture("rpgplug.tree")
bush_texture = gamepie.load.Texture("rpgplug.bush")
avatar_texture = gamepie.load.Texture("rpgplug.avatar")

# kamera
camera = gamepie.Camera(position=(0,0), zoom=3, anchor="center")

# objekty
objects = []

grid_size = 32
rows, cols = 50, 50
start_x = -grid_size * cols // 2
start_y = -grid_size * rows // 2
for row in range(rows):
    for col in range(cols):
        choice = gamepie.utils.rnd.choice(["tree", "bush", ] + ["empty"] * 6)
        pos = (start_x + col * grid_size, start_y + row * grid_size)
        if choice == "tree":
            obj = gamepie.draw.Image(screen, texture=tree_texture, position=pos,
                                     anchor=gamepie.utils.CENTER, size=(32,64), camera=camera)
            objects.append(obj)
        elif choice == "bush":
            obj = gamepie.draw.Image(screen, texture=bush_texture, position=pos,
                                     anchor=gamepie.utils.CENTER, size=(32,64), camera=camera)
            objects.append(obj)

# hráč
player = gamepie.draw.Image(screen, avatar_texture, camera=camera, size=(32,36))

controller = gamepie.plugins.Controllers.RPGController(player=player, camera=camera, objects=objects, speed=0.05, movement_4_key=("up","down","left","right"))

controller.c_key_enabled = True  # klávesa C funguje

def update():
    dt = fps.tick()
    print(controller.status)
    controller.update(dt)

    screen.fill((0,80,0))
    for obj in objects:
        obj.draw()
    player.draw()
    screen.flip()

screen.run()
gamepie.quit()

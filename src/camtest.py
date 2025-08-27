import random
seed = input("Seed: ")

import gamepie


screen = gamepie.Window(title="Test", flags=gamepie.RESIZABLE)
fps = gamepie.Clock(60)
gamepie.mixer.Music(gamepie.Audio("music"))
font = gamepie.Font("arial", size=20)
tree_texture = gamepie.Texture("tree")
bush_texture = gamepie.load.Texture("bush")
avatar = gamepie.Texture("avatar")

gamecamera = gamepie.Camera(position=(0,0), zoom=3, anchor="center")

objects = [] 

grid_size = 32
rows = 50
cols = 50
start_x = -grid_size * cols // 2
start_y = -grid_size * rows // 2
gamepie.rand.seed(seed)
for row in range(rows):
    for col in range(cols):
        choice = gamepie.rand.randchoice(["tree", "bush"] + ["empty"] * 6)
        pos = (start_x + col * grid_size, start_y + row * grid_size)

        if choice == "tree":
            img = gamepie.draw.Image(screen, texture=tree_texture, position=pos,
                                     anchor=gamepie.CENTER, size=(32, 64), camera=gamecamera)
            objects.append(img)
        elif choice == "bush":
            img = gamepie.draw.Image(screen, texture=bush_texture, position=pos,
                                     anchor=gamepie.CENTER, size=(32, 64), camera=gamecamera)
            objects.append(img)

        
player = gamepie.draw.Image(screen, avatar, camera=gamecamera,size=(32, 36))
gui = gamepie.draw.gui.Label(surface=screen, font=font)


def update():
    dt = fps.tick()
    speed = 0.05 * dt
    move_x = 0
    move_y = 0

    if gamepie.key.is_down("c"):
        collision = False
    else:
        collision = True
    if gamepie.key.is_down("w"):
        move_y -= speed

    if gamepie.key.is_down("s"):
        move_y += speed

    if gamepie.key.is_down("a"):
        move_x -= speed
        player.flip = (False, False)
    if gamepie.key.is_down("d"):
        move_x += speed
        player.flip = (True, False)
    old_x, old_y = gamecamera.x, gamecamera.y

    gamecamera.x += move_x
    gamecamera.y += move_y
    player.pos = gamecamera.pos

    screen.fill((0, 80, 0))

    gui.text = f"seed:{seed}\nposition:{int(gamecamera.x),int(gamecamera.y)}"
    
    for obj in objects:
        if player.collision.mesh(obj) and collision:
            gamecamera.x = old_x
            gamecamera.y = old_y
            player.pos = gamecamera.pos
            break

    for obj in objects:
        obj.draw()
        

    gui.draw()
    player.draw()
    screen.flip()

screen.run()
gamepie.quit()

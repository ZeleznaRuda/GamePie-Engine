import gamepie

screen = gamepie.Window(title="Test")

screen.escape = True
fps = gamepie.Clock(60)
r = gamepie.gobjects.Rectangle(surface=screen,position=(50, 50),anchor=gamepie.TOPLEFT, size=(50, 50)).border_radius(5,5,5,5).outline((0,0,0), 3)
speed = 45
print(gamepie.fonts())
def update():
    dt = fps.tick() / 1000
    screen.fill((0,80,25))
    
    r.draw()
    
    if gamepie.input.key.is_down("s"):
        r.y += speed *dt
    if gamepie.input.key.is_down("w"):
        r.y -= speed *dt
    if gamepie.input.key.is_down("d"):
        r.x += speed *dt
    if gamepie.input.key.is_down("a"):
        r.x -= speed *dt
    screen.flip()
    
#running
screen.run()
gamepie.quit()

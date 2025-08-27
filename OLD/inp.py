import gamepie


screen = gamepie.Window(title="Test")
fps = gamepie.Clock(60)
font = gamepie.loadfn.Font("arial",size=20)
img = gamepie.loadfn.Texture("pacman")
image = gamepie.Image(screen,texture=img,anchor="midleft", size=(90,90))
def update(): 
    dt = fps.tick()
    screen.fill((255,255,255))
    image.pos = gamepie.input.mouse.pos
    image.draw()
    screen.flip()

screen.run()
gamepie.quit()
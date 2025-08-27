import gamepie


screen = gamepie.Window(title="Test")

fps = gamepie.Clock(60)
font = gamepie.loadfn.Font("arial",size=20)
img = gamepie.loadfn.Texture("button_texture")

lab = gamepie.gui.Label(surface=screen,text="Ahoj",font=font,size=(90, 90))
lay = gamepie.Layers(lab)
def update(): 
    dt = fps.tick()
    
    screen.fill((0,80,25))
    lay.draw()

    screen.flip()

screen.run()
gamepie.quit()
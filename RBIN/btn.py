import gamepie


screen = gamepie.Window(title="Test")

fps = gamepie.Clock(60)
font = gamepie.loadfn.Font("arial",size=20)
img = gamepie.loadfn.Texture("button_texture")

con = gamepie.gui.Conversation(surface=screen(),font=font,messages=["Ahoj, jak se mas","Ja jsem:;GamePie"])
btn = gamepie.gui.Button(surface=screen(),font=font,position=(0,0), text="Print time")
lay = gamepie.Layers(
    con, 
    btn
    )
def update(): 
    dt = fps.tick()
    
    screen.fill((0,80,25))
    lay.draw()
    if btn.is_press():
        print(gamepie.time._wait_cache_)
        print("Press")

    screen.flip()

screen.run()
gamepie.quit()
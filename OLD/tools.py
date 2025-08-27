import gamepie

#create window
screen = gamepie.Window(title="Test")
screen.escape = True
#fps
fps = gamepie.Clock(60)

#load
font = gamepie.loadfn.Font("arial",size=50)
img = gamepie.loadfn.Texture("pie")
nom = gamepie.loadfn.Sound("nomnom")


text = gamepie.gui.Text(surface=screen.surface,text=".",color=(0,255,0),font=font,anti_aliasing=True).outline((0,0,0),3)

score = 0
speed = 2
#loop
def update():
    global speed, score
    dt = fps.tick()
    
    text.text = f"Score: {score}"
    text.x += 2 *dt
    screen.fill((0,80,25))
    text.draw()
    screen.flip()
    
#running
screen.run()
gamepie.quit()

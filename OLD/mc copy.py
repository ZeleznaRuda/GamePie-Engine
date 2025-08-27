import gamepie

#fps
#create window
screen = gamepie.Window(title="Test")
screen.escape = True
font = gamepie.loadfn.Font("Arial", 36)

def update():

    screen.fill((0,80,25))
    gamepie.draw.label(screen, "ahoj",font,color=(0,0,0),angle=45,background_color=(255,255,255))
    screen.flip()
    
#running
screen.run()
gamepie.quit()

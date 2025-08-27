
import gamepie # << import library

screen = gamepie.Window(title="Test", flags=gamepie.RESIZABLE) # << create window
fps = gamepie.Clock(60)                                       # << create clock

pie_texture = gamepie.loadfn.Texture("pie")            # << load assets
pie = gamepie.draw.Image(screen, texture=pie_texture) # << create game object

def update():         # << main loop (mandatory!)
    dt = fps.tick()   # << delta time calculation
    speed = 0.1 * dt  # << smooth movement using delta time
    
    pie.x += speed    # << game logic
    
    screen.fill(gamepie.WHITE) # << clear the screen
    pie.draw()                 # << draw object
    screen.flip()              # << update the screen
    
screen.run()   # << start application (mandatory!)
gamepie.quit() # << exit

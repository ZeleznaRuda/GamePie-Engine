
import gamepie

#create window
screen = gamepie.Window(title="Test",flags=gamepie.utils.RESIZABLE)
#fps
fps = gamepie.Clock(60)

rect = gamepie.draw.Rectangle(screen,position=(0,0),size=(50,50),anchor=gamepie.utils.CENTER,camera=gamepie.utils.uicamera)

def update():
    dt = fps.tick()
    speed = 0.1 * dt
    
    rect.x += 1 * speed

    screen.fill((0,80,0))
    

    rect.draw() 
    screen.flip()
    
#running
screen.run()
gamepie.quit()

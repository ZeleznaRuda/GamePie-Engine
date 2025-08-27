
import gamepie

#create window
screen = gamepie.Window(title="Test",flags=gamepie.utils.RESIZABLE)
#fps
fps = gamepie.Clock(60)
tenor = gamepie.load.Frames(r"src\gamepie\assets\bonk_doge-tenor.gif")
giphy = gamepie.load.Frames(r"src\gamepie\assets\elephant_run-giphy.gif")
rect = gamepie.draw.Rectangle(screen,position=(0,0),size=(50,50),anchor=gamepie.utils.CENTER,camera=gamepie.utils.uicamera)
tenor_anim = gamepie.draw.Animation(screen,ms=1, frames=tenor,size=(800,600),camera=gamepie.utils.uicamera)
giphy_anim = gamepie.draw.Animation(screen,ms=1,position=(500,0), frames=giphy,size=(800,600),camera=gamepie.utils.uicamera)
tenor_anim.play()
giphy_anim.play()
def update():
    dt = fps.tick()
    speed = 0.1 * dt
    
    rect.pos = gamepie.mouse.pos

    screen.fill((0,80,0))
    
    tenor_anim.draw()
    giphy_anim.draw()
    rect.draw() 
    screen.flip()
    
#running
screen.run()
gamepie.quit()

import gamepie

screen = gamepie.Window(title="Test", flags=gamepie.NOFRAME)
fps = gamepie.Clock(60)

nyan = gamepie.load.Frames("nyancat")
gamepie.mixer.Music(gamepie.load.Audio("music"))            
anim = gamepie.draw.Animation(screen,ms=70, frames=nyan,size=(800,600),camera=gamepie.uicamera)

anim.play()

def update():
    screen.fill((0,0,0))
    dt = fps.tick()
    anim.draw()
    screen.flip()

screen.run()      
gamepie.quit()

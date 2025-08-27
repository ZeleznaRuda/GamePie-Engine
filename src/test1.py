import gamepie # << import library

screen = gamepie.Window(title="Test", flags=gamepie.utils.NOFRAME) # << create borderless window                                  # << create clock

nyan = gamepie.load.Frames("nyancat", ms=60) # << load animation
gamepie.mixer.Music("nyansound")                # << load and play music
anim = gamepie.draw.Animation(screen, animation=nyan, size=(800, 600), camera=gamepie.utils.uicamera) # << create animation

anim.play() # << start animation

def update():           # << main loop (mandatory!)
    screen.fill((0, 0, 0)) # << clear screen (black)
    dt = screen.fps.tick()  # << delta time calculation
    anim.draw()            # << draw animation
    screen.flip()          # << update the screen

screen.run()   # << start application (mandatory!)
gamepie.quit() # << exit
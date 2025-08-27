import gamepie

screen = gamepie.Window(title="Adventure Platformer", flags=gamepie.utils.RESIZABLE)

r = gamepie.draw.Rectangle(screen)

def update():
    dt = screen.fps.tick()
    r.draw()
    screen.flip()

screen.run()
gamepie.quit()

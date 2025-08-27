import gamepie

fps = gamepie.Clock(60)
screen = gamepie.Window(title="Test", flags=[gamepie.RESIZABLE])
screen.escape = True
img = gamepie.loadfn.Texture("pacman")
def update():
    dt = fps.tick()
    screen.fill((30, 30, 30))
    gamepie.draw.image(screen,image=img, rect=gamepie.Rect(50,50,50,60),flip=(False,True))
    screen.flip()

screen.run()

import gamepie
import gamepie.input
fps = gamepie.Clock(60)
screen = gamepie.Window(title="Test")
line = gamepie.gobjects.Line(screen,width=5,positions=(screen.center,(0,0)))
def update():
    dt = fps.tick()
    screen.fill((0, 0, 0))
    line.end_pos = (gamepie.input.mouse.pos)
    print(screen.center)
    line.draw()
    screen.flip()

screen.run()

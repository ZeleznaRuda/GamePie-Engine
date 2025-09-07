import gamepie 

screen = gamepie.Window()
objs = gamepie.utils.Objects()
def update():
    global objs
    dt = screen.fps.tick()
    screen.fill(gamepie.utils.Color("SKY")())
    for obj in objs.all():
        obj.draw()
    if gamepie.key.is_down("i"):
        objs.save()
    if gamepie.key.is_down("e"):
        objs = gamepie.utils.Objects.load()
    print(objs.objects)
    screen.flip()

screen.run()
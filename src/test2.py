import gamepie
from gamepie import plugins
screen = gamepie.Window(title="Test",flags=gamepie.utils.RESIZABLE)
menu = []
menu_items = ["Save","Load","Settings","Help","Exit"]
for i in range(5):

    btn = gamepie.plugins.GUIassets.Button(screen,text=menu_items[i],image=gamepie.load.Texture("guiplug.button_bg"),size=(125,50),position=(0,i*50),camera=gamepie.utils.uicamera)
    menu.append(btn)

def update():
    dt = screen.fps.tick()
    if menu[4].is_press():
        gamepie.quit()
    screen.fill((255,255,255))

    for btn in menu:
        btn.draw()

    screen.flip()
screen.run()

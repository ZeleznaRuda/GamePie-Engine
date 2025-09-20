import gamepie
from gamepie.plugins import GUIassets

screen = gamepie.Window(title="Test", flags=gamepie.constants.RESIZABLE)
menu = []
menu_items = ["Save", "Load", "Settings", "Help", "Exit"]

for i in range(5):
    btn = gamepie.plugins.GUIassets.Button(
        screen,
        text=menu_items[i],
        image=gamepie.load.Texture("plugins:guiassets.textures.button_bg"),
        size=(125, 50),
        position=(0, i * 50),
        camera=gamepie.utils.uicamera
    )
    menu.append(btn)

inpbx = GUIassets.InputBox(screen,position=(500,0))
inpbx.background.border_radius()
def update():
    global i
    dt = screen.fps.tick()
    screen.fill((255, 255, 0))

    # Ukončení programu
    if menu[4].is_press():
        gamepie.quit()
    
        


    for btn in menu:
        btn.draw()
    inpbx.draw()

    screen.flip()

screen.run()

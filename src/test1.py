import gamepie
from gamepie.utils.dict import *
screen = gamepie.Window(title="První okno", size=(400, 300))

a = gamepie.utils.Messagebox("Něco se pokazilo!").show(type=167)
print(a)

screen.run()

import gamepie
from gamepie.utils.dict import *
gamepie.core._gp_log("\033[1;31m[fatal error]: pywin32 is not installed, maximization will not work (install using 'pip install pywin32')\033[0m")
screen = gamepie.Window(title="První okno", size=(400, 300))

a =gamepie.utils.Messagebox("pywin32 is not installed, maximization will not work (install using 'pip install pywin32')").askquestion()
print(a)
screen.run()

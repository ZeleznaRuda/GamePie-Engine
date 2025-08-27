
import os
import platform
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
os.environ['SDL_VIDEO_CENTERED'] = '1'

GAMEPIE_LOG = os.environ.get('GAMEPIE_LOG', '1') == '1'
def _gp_log(msg: str):
    if GAMEPIE_LOG:
        print(f"[gamepie]: {msg}")
        
if os.environ.get('GAMEPIE_SHOW_WELCOME', '1') == '1':
    print("\nYou use the \033[4m\033[33mGamePie\033[0m library to create 2d games\nPower by \033[4m\033[33mPygame\033[0m\n")

print(f"Using: {platform.platform()}\n")

from .. import utils    
from .error import *
from .load import *
from .event import *
from .quitFunc import quit
from . import mixer
from . import draw

from .time import wait, _wait_cache_, asyncWait
from .point import Point
from .cam import Camera
from .win import Window, Clock
from .surface import Surface
from .rect import Rect

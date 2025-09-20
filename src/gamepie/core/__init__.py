
import os
import platform
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
os.environ['SDL_VIDEO_CENTERED'] = '1'

GAMEPIE_LOG = os.environ.get('GAMEPIE_LOG', '1') == '1'
VERSION = 0.4

def _gp_log(msg: str,start="", end="\n", flush=False):
    if GAMEPIE_LOG:
        print(start,f"[gamepie]: {msg}", end=end, flush=flush)

if os.environ.get('GAMEPIE_SHOW_WELCOME', '1') == '1':
    print(f"\nYou use the \033[4m\033[33mGamePie\033[0m library to create 2d games\nPower by \033[4m\033[33mPygame\033[0m\nVersion: {VERSION}")

print(f"Using: {platform.platform()}\n")

from .. import utils    
from . import error
from .quitFunc import quit
from . import load
from .event import *
from . import mixer
from . import draw
from . import constants
from .time import wait, _wait_cache_, asyncWait
from .point import Point
from .cam import Camera
from .win import Window, Clock
from .surface import Surface
from .rect import Rect

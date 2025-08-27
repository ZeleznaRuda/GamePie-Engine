import pygame 
import sys

from ..pather import *
from .event import mouse, key
from ..utils.func import quit, screenshot

from .surface import Surface
from . import _gp_log
pygame.init()

class Clock:
    def __init__(self, limit):
        self.clock = pygame.time.Clock()
        self.limit = limit

    def tick(self):
        return self.clock.tick(self.limit)

    @property
    def fps(self):
        return self.clock.get_fps()

import platform
import datetime
class Window:
    def __init__(self,icon=ICON16 if platform.system() == "Windows" else ICON70,title="GamePie", size=(800,500),fps_limit=60, flags=None,monitor=0,fullscreensize=False, vsync=False, screenshot=True):
        self._w, self._h = size
        self.title = str(title)
        self.icon = str(icon)
        self.flags = flags
        self.escape = bool(True)
        self.running = bool(True)
        self.monitor = int(monitor)
        self.vsync = int(vsync)
        self.screenshot = bool(screenshot)
        self.fps_limit = int(fps_limit)
        self.fps = Clock(fps_limit)
        self.__create_window()
        
    def __create_window(self):
        _flags = 0
        if self.flags and isinstance(self.flags, tuple):
            for flag_name in self.flags:
                flag_name = flag_name.strip().upper()
                if flag_name in globals():
                    _flags |= globals()[flag_name]
        _gp_log("window was create")



        self.surface  = pygame.display.set_mode((self.w, self.h),display=self.monitor, flags=self.flags)
        pygame.display.set_caption(self.title)
        icon_surface = pygame.image.load(self.icon)
        pygame.display.set_icon(icon_surface)
    
    def blit(self, target_surface, pos=(0,0)):
        target_surface.blit(self.surface, pos)

    
    def fill(self, color):
        self.surface.fill(color)
    
    def flip(self):
        pygame.display.flip()
    def _get_screenshot_folder(self):
        folder = Path(__file__).parent.parent.parent / "screenshots"
        folder.mkdir(exist_ok=True)  
        return folder
    
    def run(self):
        while self.running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False
            
            mouse.update(events)
            key.update(events)
            #microphone.update()
            
            if self.escape and key.is_down("escape"):
                quit()

            if self.screenshot and key.is_down("f2"):
                now = datetime.datetime.now()
                formatted_time = f"{now.day}{now.month}{now.year % 100}0{now.second}{now.minute}{now.hour}"
                folder = self._get_screenshot_folder()
                file_path = folder / f"screenshot0{formatted_time}0{id(self)}0.jpg"
                screenshot(self, str(file_path)) 

            main = sys.modules.get("__main__")
            update_func = getattr(main, "update", None)

            if update_func:
                update_func()

    @property
    def center(self):
        return self._w // 2, self._h // 2

    @property
    def w(self): return self._w
    @property
    def h(self): return self._h

    def __call__(self):
        return self.surface
    def __repr__(self):
        return repr(f"<Window({self._w, self._h})")



import pygame
import sys
import multiprocessing
import platform
import datetime
from pathlib import Path

from ..pather import *
from .event import mouse, key
from ..utils.func import quit, screenshot
from .constants import RESIZABLE
from .surface import Surface
from . import _gp_log
from ..utils.gpbox import Messagebox as msgbox
from ..core.color import _Color
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

#msgbox("Warning low fps").show(11)
class Window:
    _processes = []
    def __init__(self, icon=ICON16 if platform.system() == "Windows" else ICON70,
                 title="GamePie", size=(800, 500), fps_limit=60, flags=0,
                 monitor=0, vsync=False,print_fps=False, screenshot=True,maximize=False):
        self._w, self._h = size
        self.title = str(title)
        self.icon = str(icon)
        self.flags = flags
        self.escape = True
        self.running = True
        self.monitor = int(monitor)
        self.vsync = int(vsync)
        self.screenshot = bool(screenshot)
        self.fps_limit = int(fps_limit)
        self.fps = Clock(fps_limit)
        self.print_fps = bool(print_fps)
        self.maximize = bool(maximize)
        self._tick = 0
        self.__create_window()



    def __create_window(self):
        _flags = 0
        if self.flags and isinstance(self.flags, tuple):
            for flag_name in self.flags:
                flag_name = flag_name.strip().upper()
                if flag_name in globals():
                    _flags |= globals()[flag_name]
            self.flags = _flags
        
        if not self.maximize:
            self.surface = pygame.display.set_mode(
                (self.w, self.h), display=self.monitor, flags=self.flags
            )
        else:
                info = pygame.display.Info()
                self.surface = pygame.display.set_mode(
                    (info.current_w, info.current_h), display=self.monitor, flags=self.flags | RESIZABLE
                )
        pygame.display.set_caption(self.title)
        _gp_log("window was created")
        try:
            icon_surface = pygame.image.load(self.icon)
            pygame.display.set_icon(icon_surface)
        except Exception as e:
            _gp_log(f"icon load failed: {e}")

    def blit(self, target_surface, pos=(0, 0)):
        target_surface.blit(self.surface, pos)

    def fill(self, color):
        self.surface.fill(_Color(color)())
    
    def flip(self):
        pygame.display.flip()

    def _get_screenshot_folder(self):
        base = Path(sys.argv[0]).resolve().parent
        folder = base / "myscreenshots"
        folder.mkdir(parents=True, exist_ok=True)
        return folder

   
    def run(self):
        __onetakeinrunfpswarning = False
        while self.running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False
            
            mouse.update(events)
            key.update(events)

            if self.escape and key.is_down("escape"):
                quit()
            

            if self.screenshot and key.is_down("f2"):
                now = datetime.datetime.now()
                formatted_time = f"{now.day}{now.month}{now.year % 100}{now.hour}{now.minute}{now.second}"
                folder = self._get_screenshot_folder()
                file_path = folder / f"screenshot0{formatted_time}0{id(self)}.jpg"
                screenshot(self, str(file_path)) 

            main = sys.modules.get("__main__")
            if self.print_fps and not _main_uses_print(main=main):
                _gp_log(f"fps: {int(self.fps.fps)}", end="\r", start="", flush=True)
            else:
                if self.print_fps and not __onetakeinrunfpswarning:   # <<< vypsat jen jednou
                    _gp_log("[warning]: You cannot use fps display in the console (because your code uses the print function).")
                    __onetakeinrunfpswarning = True
            update_func = getattr(main, "update", None)
            self._tick = self.fps.tick()
            if update_func:
                update_func()

            

        pygame.quit()

    @property
    def center(self):
        return self._w // 2, self._h // 2
    @property
    def tick(self): 
        return self._tick
    @property
    def w(self): 
        return self._w

    @property
    def h(self): 
        return self._h

    def __call__(self):
        return self.surface

    def __repr__(self):
        return f"<Window({self._w}, {self._h})>"

    @staticmethod
    def spawn(*args, **kwargs):
        import multiprocessing
        try:
            multiprocessing.set_start_method("spawn", force=True)
        except RuntimeError:
            pass

        p = multiprocessing.Process(
            target=_window_process,
            args=(args, kwargs),
            daemon=True
        )
        p.start()
        Window._processes.append(p)
        return p

    @staticmethod
    def join():
        for p in Window._processes:
            p.join()


def _window_process(args, kwargs):
    import pygame
    pygame.init()
    win = Window(*args, **kwargs)
    win.run()
    pygame.quit()
def _main_uses_print(main) -> bool:
    #ai
    import ast
    import inspect
    if not main:
        return False
    try:
        source = inspect.getsource(main)
    except (OSError, TypeError):
        return False

    tree = ast.parse(source)
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name) and node.func.id == "print":
                return True
    return False



"""    def __maxScaledWindowForWindows(self):
        if platform.system() == "Windows":
            try:
                import win32gui
                import win32con
            except ImportError:
                _gp_log("\033[1;31m[fatal error]: pywin32 is not installed, maximization will not work (install using 'pip install pywin32')\033[0m")                
                msgbox("pywin32 is not installed, maximization will not work (install using 'pip install pywin32')").show(11)

            else:
                hwnd = pygame.display.get_wm_info()["window"]
                win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
                style = win32gui.GetWindowLong(hwnd, win32con.GWL_STYLE)
                style &= ~(win32con.WS_THICKFRAME)
                win32gui.SetWindowLong(hwnd, win32con.GWL_STYLE, style)
                win32gui.SetWindowPos(hwnd, None, 0, 0, 0, 0,
                                    win32con.SWP_FRAMECHANGED |
                                    win32con.SWP_NOMOVE |
                                    win32con.SWP_NOSIZE)
"""
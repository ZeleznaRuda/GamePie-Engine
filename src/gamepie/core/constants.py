import pygame
import pygame

RESIZABLE: int = pygame.RESIZABLE
NOFRAME: int = pygame.NOFRAME
FULLSCREEN: int = pygame.FULLSCREEN
DOUBLEBUF: int = pygame.DOUBLEBUF
OPENGL: int = pygame.OPENGL
HWSURFACE: int = pygame.HWSURFACE
SWSURFACE: int = pygame.SWSURFACE
SCALED: int = pygame.SCALED
ANYFORMAT: int = pygame.ANYFORMAT
HWACCEL: int = pygame.HWACCEL
SRCALPHA: int = pygame.SRCALPHA

CURSOR_ARROW: int = pygame.SYSTEM_CURSOR_ARROW
CURSOR_IBEAM: int = pygame.SYSTEM_CURSOR_IBEAM
CURSOR_WAIT: int = pygame.SYSTEM_CURSOR_WAIT
CURSOR_CROSSHAIR: int = pygame.SYSTEM_CURSOR_CROSSHAIR
CURSOR_WAITARROW: int = pygame.SYSTEM_CURSOR_WAITARROW
CURSOR_SIZENWSE: int = pygame.SYSTEM_CURSOR_SIZENWSE
CURSOR_SIZENESW: int = pygame.SYSTEM_CURSOR_SIZENESW
CURSOR_SIZEWE: int = pygame.SYSTEM_CURSOR_SIZEWE
CURSOR_SIZENS: int = pygame.SYSTEM_CURSOR_SIZENS
CURSOR_SIZEALL: int = pygame.SYSTEM_CURSOR_SIZEALL
CURSOR_NO: int = pygame.SYSTEM_CURSOR_NO
CURSOR_HAND: int = pygame.SYSTEM_CURSOR_HAND


TOPLEFT = "topleft"
TOPRIGHT = "topright"
BOTTOMLEFT = "bottomleft"
BOTTOMRIGHT = "bottomright"
CENTER = "center"
MIDTOP = "midtop"
MIDBOTTOM = "midbottom"
MIDLEFT = "midleft"
MIDRIGHT = "midright"

MSGBOX_ERROR = 0
MSGBOX_WARNING = 10
MSGBOX_MSG = 20
MSGBOX_INFO = 40
MSGBOX_QUESTION = 30
MSGBOX_SCREENSHOT = 50

_colors = {
"WHITE"  : (255, 255, 255),
"BLACK"  : (0, 0, 0),
"RED"  : (255, 0, 0),
"GREEN"  : (0, 255, 0),
"BLUE"  : (0, 0, 255),
"YELLOW"  : (255, 255, 0),
"CYAN"   : (0, 255, 255),
"MAGENTA" : (255, 0, 255),
"GRAY": (128, 128, 128),
"GRAY1" : (30, 30, 30),
"LIGHTGRAY"  : (200, 200, 200),
"DARKGRAY": (50, 50, 50),
"ORANGE" : (255, 165, 0),
"PURPLE"  : (128, 0, 128),
"PINK"   : (255, 192, 203),
"BROWN"    : (139, 69, 19),
"SKY"        : (0, 135, 215),
}

class Color:
    def __init__(self, color):
        if isinstance(color, str) and color.upper() in _colors:
            self._color = _colors[color.upper()]
        elif isinstance(color, tuple) and len(color) == 3:
            self._color = color
        else:
            raise ValueError(f"undefined color '{color}'")

    def __call__(self):
        return self._color

    def __repr__(self):
        return f"Color({self._color})"
    def __iter__(self):
        return iter(self._color)
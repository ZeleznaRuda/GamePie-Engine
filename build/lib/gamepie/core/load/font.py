import pygame
import os
from .. import _gp_log

class Font:
    def __init__(self, font=None, size=20, mod=False, msg=True):
        if mod:
            pygame.init()
            pygame.display.set_mode((1, 1))
        pygame.font.init()
        self.size = size

        if font:
            font_lower = font.lower().replace(" ", "")
            if font_lower in pygame.font.get_fonts():
                self.pygame_font = pygame.font.SysFont(font_lower, size)
                if msg:
                    _gp_log(f"SysFont '{font}' was loaded")
            elif os.path.exists(font):
                self.pygame_font = pygame.font.Font(font, size)
                if msg:
                    _gp_log(f"Font file '{font}' was loaded")
            else:
                raise FileNotFoundError(f"Warning: font '{font}' not found in system or path")
        else:
            self.pygame_font = pygame.font.Font(None, 25)

    def __call__(self):
        return self.pygame_font

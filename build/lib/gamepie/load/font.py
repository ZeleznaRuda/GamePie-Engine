import pygame
import os
from .. import _gp_log
class Font:
    def __init__(self, font=None, size=20,mod=False):
        if mod:
            pygame.init()
            pygame.display.set_mode((1, 1))
        pygame.font.init()
        self.size = size

        if font:
            font_lower = font.lower()
            if font_lower in pygame.font.get_fonts():
                self.pygame_font = pygame.font.SysFont(font_lower, size)
                _gp_log(f"SysFont '{font}' was load")
            elif os.path.exists(font):
                self.pygame_font = pygame.font.Font(font, size)
                _gp_log(f"font '{font}' was load")
            else:
                raise FileNotFoundError(f"warning font '{font}' not found in system or path")
        else:
            self.pygame_font = pygame.font.SysFont("arial", size)
    def __call__(self):
        return self.pygame_font
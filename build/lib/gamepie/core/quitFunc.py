import pygame
import sys
from ..core import _gp_log
        
def quit():
    _gp_log(f"program was quit")
    pygame.quit()
    sys.exit()
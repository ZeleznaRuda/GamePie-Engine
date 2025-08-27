import pygame
from ..dict import CURSOR_ARROW
pygame.init()

class _Mouse:
    def __init__(self):
        self.mouse_x = 0
        self.mouse_y = 0
        self._mousewheel = 0
        
        self._left = False
        self._middle = False
        self._right = False
        self._cursor = CURSOR_ARROW
        
    def update(self, events):
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
        self._left, self._middle, self._right = pygame.mouse.get_pressed()
        pygame.mouse.set_cursor(self._cursor)      

        for event in events:
            if event.type == pygame.MOUSEWHEEL:
                self._mousewheel = event.y

 
    def get(self):
        return [(self.mouse_x, self.mouse_y),self._left, self._middle, self._right, self._mousewheel] 

    @property
    def x(self): return self.mouse_x

    @property
    def y(self): return self.mouse_y

    @property
    def pos(self): return self.mouse_x, self.mouse_y

    @property
    def left(self): return self._left

    @property
    def middle(self): return self._middle

    @property
    def right(self): return self._right

    @property
    def mousewheel(self): return self._mousewheel
    @property
    def cursor(self): return self._cursor
    @cursor.setter
    def cursor(self, value): 
        self._cursor = value

class _Key:
    def __init__(self):
        self._keydown = False
        self._keyup = False
        self._any = False
        self._last_key = None
        self.char = None  
        self._pressed = pygame.key.get_pressed()

    def update(self, events):
        self.keydown = False
        self.keyup = False
        self.any = False
        self.char = None 

        for event in events:
            if event.type == pygame.KEYDOWN:
                self.keydown = True
                self.any = True
                self.last_key = event.key
                self.char = event.unicode  

            elif event.type == pygame.KEYUP:
                self.keyup = True
                self.any = True

        self._pressed = pygame.key.get_pressed()

    def get(self):
        return [self.char, self.keydown, self.keyup, self.any]

    def is_down(self, keyname: str):
        try:
            keycode = pygame.key.key_code(keyname.lower())
            return self._pressed[keycode]
        except:
            return False

mouse = _Mouse()
key = _Key()
    

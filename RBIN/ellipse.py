import pygame
from .rect import Rect
from ...func import anchor

class Ellipse:
    def __init__(self, surface, position=(0, 0), size=(60, 50), color=(0, 255, 0),
                 anchor="topleft", alpha=255, angle=0, visible=True):
        self.surface = surface
        self._color = color
        self._anchor = anchor
        self._alpha = alpha
        self._angle = angle
        self.__destroyed = False
        self.__outline = False
        self.__outline_color = (0,0,0)
        self.__outline_size = 0

        self._w, self._h = size
        self._x, self._y = position
        
        self.rect = Rect(surface=self.surface, position=(self._x, self._y),size=(self._w, self._h))
        self._visible = visible 

        self._set_pos((self._x, self._y))

    def _set_pos(self, pos):
        if self.__destroyed:
            return
        x, y = anchor(position=pos, size=(self._w, self._h), anchor=self._anchor)
        self._x, self._y = x, y
        self.rect.topleft = (x, y)

    def destroy(self):
        self.__destroyed = True
        self.surface = None
        self._color = None
        self.rect = None

    def _check_destroyed(self):
        if self.__destroyed:
            raise Exception("The Ellipse object has been destroyed and can no longer be used.")

    def _set_size(self, w, h):
        if self.__destroyed:
            return
        self._w, self._h = w, h
        self.rect.size = (w, h)

    def _set_color(self, color):
        if self.__destroyed:
            return
        self._color = color

    def _set_anchor(self, anchor):
        if self.__destroyed:
            return
        self._anchor = anchor
        self._set_pos((self._x, self._y))

    def _set_visible(self, visible):
        self._visible = visible

    def _set_alpha(self, value):
        if self.__destroyed:
            return
        self._alpha = max(0, min(255, value))

    def _set_angle(self, value):
        if self.__destroyed:
            return
        self._angle = value
        
    def outline(self, color, size):
        self.__outline = True
        self.__outline_color = color
        self.__outline_size = size
        return self
    def __draw_outline(self):
        if self.__outline:
            pygame.draw.ellipse(self.surface, (self.__outline_color), (self._x, self._y, self._w, self._h), self.__outline_size)
    def draw(self):
        if self.__destroyed:
            return 
        if not self._visible:
            return

        rect_surface = pygame.Surface((self._w, self._h), pygame.SRCALPHA)
        pygame.draw.ellipse(rect_surface, (*self._color, self._alpha), rect_surface.get_rect())

        if self._angle != 0:
            rotated = pygame.transform.rotate(rect_surface, self._angle)
            new_rect = rotated.get_rect(center=(self._x + self._w // 2, self._y + self._h // 2))
            self.surface.blit(rotated, new_rect.topleft)
        else:
            self.surface.blit(rect_surface, (self._x, self._y))
        
        self.__draw_outline()

    @property
    def x(self): 
        return self._x

    @x.setter
    def x(self, value): 
        self._set_pos((value, self._y))

    @property
    def y(self): 
        return self._y

    @y.setter
    def y(self, value): 
        self._set_pos((self._x, value))

    @property
    def pos(self): 
        return self._x, self._y

    @pos.setter
    def pos(self, value): 
        self._set_pos(value)

    @property
    def width(self): return self._w

    @width.setter
    def width(self, value): self._set_size(value, self._h)

    @property
    def height(self): return self._h

    @height.setter
    def height(self, value): self._set_size(self._w, value)

    @property
    def size(self): return self._w, self._h

    @size.setter
    def size(self, value):
        if isinstance(value, (tuple, list)) and len(value) == 2:
            self._set_size(value[0], value[1])
        else:
            raise ValueError("Size must be a tuple or list of length 2")

    @property
    def visible(self): return self._visible

    @visible.setter
    def visible(self, value): self._set_visible(value)
    
    @property
    def anchor(self): return self._anchor

    @anchor.setter
    def anchor(self, value): self._set_anchor(value)

    @property
    def color(self): return self._color

    @color.setter
    def color(self, value): self._set_color(value)

    @property
    def alpha(self): return self._alpha

    @alpha.setter
    def alpha(self, value): self._set_alpha(value)

    @property
    def angle(self): return self._angle

    @angle.setter
    def angle(self, value): self._set_angle(value)

    @property
    def type(self): return "mgo"
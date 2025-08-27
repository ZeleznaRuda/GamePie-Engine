import pygame
import os
from ..pather import *
from ..load.font import Font
from ..rect import Rect
import re

class Text:
    def __init__(self, surface, position=(0, 0), size=(60, 50), color=(0, 0, 0),
                 anchor="topleft", alpha=255, angle=0, visible=True,
                 anti_aliasing=False, font=None, text=""):
        self.surface = surface()
        self._color = color
        self._anchor = anchor
        self._alpha = max(0, min(255, alpha))
        self._angle = angle
        self._anti_aliasing = anti_aliasing
        self._text = text
        self._visible = visible 
        self.__destroyed = False
        self.__outline = False
        self.__outline_color = (0,0,0)
        self.__outline_size = 3

        self._w, self._h = size
        self._x, self._y = position

        self._font_obj = font if isinstance(font, Font) else Font(font)
        self.font_obj = self._font_obj.pygame_font
        self.font_name = font

        self.rect = Rect(self._x, self._y, self._w, self._h)
        self.pos = (self._x, self._y)

    def outline(self, color, size):
        self.__outline = True
        self.__outline_color = color
        self.__outline_size = size
        return self

    def __draw_outline(self):
            lines = self.__split_by()
            x, y = getattr(self.rect, self._anchor)
            for i, line in enumerate(lines):
                if not line.strip():
                    continue
                for dx, dy in [(-self.__outline_size, 0), (self.__outline_size, 0), 
                               (0, -self.__outline_size), (0, self.__outline_size)]:
                    outline_surface = self.font_obj.render(line, self._anti_aliasing, self.__outline_color)
                    outline_surface.set_alpha(self._alpha)
                    if self._angle != 0:
                        outline_surface = pygame.transform.rotate(outline_surface, self._angle)
                    pos = (x + dx, y + i * self.font_obj.get_linesize() + dy)
                    self.surface.blit(outline_surface, pos)
                    
    def __draw(self):
        lines = self.__split_by()
        if not lines:
            return

        x, y = getattr(self.rect, self._anchor)
        if self.__outline:
            self.__draw_outline()

        for i, line in enumerate(lines):
            if not line.strip():
                continue

            text_surface = self.font_obj.render(line, self._anti_aliasing, self._color)
            text_surface.set_alpha(self._alpha)
            if self._angle != 0:
                text_surface = pygame.transform.rotate(text_surface, self._angle)

            self.surface.blit(text_surface, (x, y + i * self.font_obj.get_linesize()))

    def draw(self):
        if not self._visible or not self._text:
            return
        if self.__outline:
            self.__draw_outline()
        self.__draw()

    def __split_by(self):
        return re.split(r'<br>|\n|;|\|', self._text)

    @property
    def text(self): return self._text
    @text.setter
    def text(self, value): self._text = value

    @property
    def x(self): return self._x
    @x.setter
    def x(self, value):
        self._x = value
        self.rect.pos = (self._x, self._y)

    @property
    def y(self): return self._y
    @y.setter
    def y(self, value):
        self._y = value
        self.rect.pos = (self._x, self._y)

    @property
    def pos(self): return self._x, self._y
    @pos.setter
    def pos(self, value):
        self._x, self._y = value
        self.rect.pos = (self._x, self._y)

    @property
    def width(self): return self._w
    @width.setter
    def width(self, value):
        self._w = value
        self.rect.size = (self._w, self._h)

    @property
    def height(self): return self._h
    @height.setter
    def height(self, value):
        self._h = value
        self.rect.size = (self._w, self._h)

    @property
    def size(self): return self._w, self._h
    @size.setter
    def size(self, value):
        if isinstance(value, (tuple, list)) and len(value) == 2:
            self._w, self._h = value
            self.rect.size = (self._w, self._h)
        else:
            raise ValueError("Size must be a tuple or list of length 2")

    @property
    def visible(self): return self._visible
    @visible.setter
    def visible(self, value): self._visible = value

    @property
    def color(self): return self._color
    @color.setter
    def color(self, value): self._color = value

    @property
    def anchor(self): return self._anchor
    @anchor.setter
    def anchor(self, value):
        self._anchor = value
        self.rect.pos = (self._x, self._y)

    @property
    def alpha(self): return self._alpha
    @alpha.setter
    def alpha(self, value): self._alpha = max(0, min(255, value))

    @property
    def angle(self): return self._angle
    @angle.setter
    def angle(self, value): self._angle = value

    @property
    def font(self): return self.font_name
    @font.setter
    def font(self, value):
        self._font_obj = value if isinstance(value, Font) else Font(value)
        self.font_obj = self._font_obj.pygame_font
        self.font_name = value

    @property
    def anti_aliasing(self): return self._anti_aliasing
    @anti_aliasing.setter
    def anti_aliasing(self, value): self._anti_aliasing = value

    @property
    def destroyed(self): return self.__destroyed
    @property
    def type(self): return "mgui"

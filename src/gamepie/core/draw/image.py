import pygame
from .draw import image
from ..collision import _Collision
from ..rect import Rect
from ..load.texture import Texture 
from ..load.frames import Frames 
from ..cam import Camera
from ...utils import camera
class Image:
    def __init__(self, surface, texture: Texture, position=(0, 0), size=(50, 50), color=(255, 255, 255),tint_mode="overlay",
                 anchor="topleft", alpha=255, angle=0,flip=(False,False),camera:Camera=camera,enable=True,  visible=True):
        self.surface = surface
        self._color = color
        self._anchor = anchor
        self._alpha = alpha
        self._angle = angle
        self._visible = visible
        self._w, self._h = size
        self._x, self._y = position
        self._flip = flip
        self._camera = camera
        self.__texture = texture
        self._tint_mode = tint_mode
        self.__image_drawn = False
        self.__destroyed = False
        self.__outline = False
        self.__outline_color = (0, 0, 0)
        self.__outline_size = 0
        self.__final_image = None
        self._enable = enable
        self.__final_pos = (self._x, self._y)
        self.__update_rect()
    def _anchor_offset(self, w, h):
        # --for lib
        from ...utils import anchor as ar
        topleft_x, topleft_y = ar(position=(0, 0), size=(w, h), anchor=self.anchor,reverse=True)
        return topleft_x, topleft_y

    def __apply_anchor(self, rect):
        if hasattr(rect, self._anchor):
            setattr(rect, self._anchor, (self._x, self._y))
        else:
            rect.topleft = (self._x, self._y)

    def __update_rect(self):
        self.rect = Rect(self._x, self._y, self._w, self._h)
        self.__apply_anchor(self.rect)
        if self._camera:
            self.rect = self._camera.apply(self.rect,screen_size=(self.surface.w,self.surface.h))
    def outline(self, color, size):
        self.__outline = True
        self.__outline_color = color
        self.__outline_size = size
        return self

    def draw(self):
        if not self._visible:
            return
        if not self._enable:
            return
        self.__update_rect()
        if self.__outline:
            self.__draw_outline_image()
        self.__draw_image()
    def __draw_outline_image(self):
        image(surface=self.surface, image=self.texture, color=self.__outline_color,rect=(self.rect.x-self.__outline_size,self.rect.y-self.__outline_size,self.rect.width+self.__outline_size*2,self.rect.height+self.__outline_size*2),flip=self._flip, angle=self._angle,tint_mode="multiply")
    def __draw_image(self):
        image(surface=self.surface, image=self.texture, color=self._color,rect=self.rect,flip=self._flip, angle=self._angle,tint_mode=self._tint_mode)
    @property
    def x(self): return self._x
    @x.setter
    def x(self, value):
        self._x = value
        self.__update_rect()

    @property
    def flip(self): return self._flip
    @flip.setter
    def flip(self, value):
        self._flip = value
        self.__update_rect()

    @property
    def y(self): return self._y
    @y.setter
    def y(self, value):
        self._y = value
        self.__update_rect()

    @property
    def pos(self): return (self._x, self._y)
    @pos.setter
    def pos(self, pos):
        self._x, self._y = pos
        self.__update_rect()

    @property
    def width(self): return self._w
    @width.setter
    def width(self, value):
        self._w = value
        self.__update_rect()

    @property
    def height(self): return self._h
    @height.setter
    def height(self, value):
        self._h = value
        self.__update_rect()

    @property
    def size(self): return (self._w, self._h)
    @size.setter
    def size(self, size):
        self._w, self._h = size
        self.__update_rect()

    @property
    def color(self): return self._color
    @color.setter
    def color(self, value):
        self._color = value

    @property
    def alpha(self): return self._alpha
    @alpha.setter
    def alpha(self, value):
        self._alpha = value

    @property
    def angle(self): return self._angle
    @angle.setter
    def angle(self, value):
        self._angle = value

    @property
    def visible(self): return self._visible
    @visible.setter
    def visible(self, value):
        self._visible = value
    @property
    def enable(self): return self._enable

    @enable.setter
    def enable(self, value): 
        self._enable = value
        self.__update_rect()
    @property
    def anchor(self): return self._anchor
    @anchor.setter
    def anchor(self, value):
        self._anchor = value
        self.__update_rect()

    @property
    def texture(self): return self.__texture
    @texture.setter
    def texture(self, value):
        self.__texture = value

    @property
    def collision(self): return _Collision(self)

    def __repr__(self):
        return repr(f"<Image position=({self._x}, {self._y}) size=({self._w}, {self._h}) color=({self._color}) texture='{self.__texture}'>")
from .draw import rect
from ..rect import Rect
from ..collision import _Collision
from ..cam import camera, Camera
class Rectangle:
    def __init__(self, surface, position=(0, 0), size=(60, 50), color=(255, 255, 255),
                 anchor="topleft", alpha=255, angle=0,camera:Camera=camera, visible=True):
        self.surface = surface
        self._x, self._y = position
        self._w, self._h = size
        self._color = color
        self._anchor = anchor
        self._alpha = alpha
        self._angle = angle
        self._visible = visible
        self._camera = camera
        self.__confirmed_border_radius=False
        self.__border_bottom_left_radius=0
        self.__border_top_left_radius=0
        self.__border_bottom_right_radius=0
        self.__border_top_right_radius=0
        
        self.__outline=False
        self.__outline_color=(0,0,0)
        self.__outline_size=3
        
        self.__update_rect()
    def border_radius(self, 
                    border_bottom_left_radius=0, 
                    border_top_left_radius=0, 
                    border_bottom_right_radius=0, 
                    border_top_right_radius=0):
        self.__confirmed_border_radius = True
        max_radius = min(self._w, self._h) // 2

        if border_bottom_left_radius > max_radius:
            border_bottom_left_radius = max_radius
        self.__border_bottom_left_radius = border_bottom_left_radius

        if border_top_left_radius > max_radius:
            border_top_left_radius = max_radius
        self.__border_top_left_radius = border_top_left_radius

        if border_bottom_right_radius > max_radius:
            border_bottom_right_radius = max_radius
        self.__border_bottom_right_radius = border_bottom_right_radius

        if border_top_right_radius > max_radius:
            border_top_right_radius = max_radius
        self.__border_top_right_radius = border_top_right_radius
        return self

    def _anchor_offset(self, w, h):
        # --for lib
        from ..func import anchor as ar
        topleft_x, topleft_y = ar(position=(0, 0), size=(w, h), anchor=self.anchor,reverse=True)
        return topleft_x, topleft_y    
    def __apply_anchor(self, rect):
        if hasattr(rect, self._anchor):
            setattr(rect, self._anchor, (self._x, self._y))
        else:
            rect.topleft = (self._x, self._y)
    
    def outline(self, color, size):
        self.__outline = True
        self.__outline_color=color
        self.__outline_size =size
        return self
    
    def __draw_outline(self):
        rect(self.surface, color=(*self.__outline_color, self._alpha), rect=self.__outlinerect, angle=self._angle,
                border_top_left_radius=self.__border_top_left_radius,
                border_top_right_radius=self.__border_top_right_radius,
                border_bottom_left_radius=self.__border_bottom_left_radius,
                border_bottom_right_radius=self.__border_bottom_right_radius,)
    def __draw_rect(self):
        rect(self.surface, color=(*self._color, self._alpha), rect=self.rect, angle=self._angle,
                border_top_left_radius=self.__border_top_left_radius,
                border_top_right_radius=self.__border_top_right_radius,
                border_bottom_left_radius=self.__border_bottom_left_radius,
                border_bottom_right_radius=self.__border_bottom_right_radius,)
    def __update_rect(self):
        self.__outlinerect = Rect(self._x- self.__outline_size, self._y- self.__outline_size, self._w+ self.__outline_size*2, self._h+ self.__outline_size*2)
        self.rect = Rect(self._x, self._y, self._w, self._h)
        self.__apply_anchor(self.rect)
        self.__apply_anchor(self.__outlinerect)
        if self._camera:
            self.rect = self._camera.apply(self.rect,screen_size=(self.surface.w,self.surface.h))
            self.__outlinerect = self._camera.apply(self.__outlinerect,screen_size=(self.surface.w,self.surface.h))
        
    def draw(self):
        if not self._visible:
            return
        self.__update_rect()
        if self.__outline:
            self.__draw_outline()
        self.__draw_rect()

    @property
    def x(self): 
        return self._x

    @x.setter
    def x(self, value): 
        self._x = value
        self.__update_rect()

    @property
    def y(self): 
        return self._y

    @y.setter
    def y(self, value): 
        self._y = value
        self.__update_rect()

    @property
    def pos(self): 
        return self._x, self._y

    @pos.setter
    def pos(self, value): 
        self._x, self._y = value
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
    def size(self): return self._w, self._h

    @size.setter
    def size(self, value):
        self._w, self._h = value
        self.__update_rect()

    @property
    def visible(self): return self._visible

    @visible.setter
    def visible(self, value): 
        self._visible = value
        self.__update_rect()

    @property
    def anchor(self): return self._anchor

    @anchor.setter
    def anchor(self, value): self._set_anchor(value)

    @property
    def color(self): return self._color

    @color.setter
    def color(self, value): 
        self._color = value
        self.__update_rect()

    @property
    def alpha(self): return self._alpha

    @alpha.setter
    def alpha(self, value): 
        self._alpha = value
        self.__update_rect()

    @property
    def angle(self): return self._angle

    @angle.setter
    def angle(self, value): 
        self._angle = value
        self.__update_rect()
    @property
    def collision(self): return _Collision(self)
    def copy(self):
        return self

    def __repr__(self):
        return repr(f"<Rectangle position=({self._x}, {self._y}) size=({self._w}, {self._h}) color=({self._color})>")

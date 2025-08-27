
from ..rect import Rect
from ..draw import label
from ...cam import Camera
from ....utils import uicamera
import re
class Label:
    def __init__(self, surface, position=(0, 0), size=(60, 50), color=(0, 0, 0), background_color=(255, 255, 255),
                 anchor="topleft", alpha=255, angle=0, visible=True,camera:Camera=uicamera,
                 anti_aliasing=False, font=None, text=""):
        self.surface = surface
        self._color = color
        self._anchor = anchor
        self._alpha = max(0, min(255, alpha))
        self._angle = angle
        self._anti_aliasing = anti_aliasing
        self._text = text
        self._font = font
        self._background_color = background_color
        self._camera = camera

        self._visible = visible 
        self.__outline = False
        self.__outline_color = (0,0,0)
        self.__outline_size = 3

        self._w, self._h = size
        self._x, self._y = position

        self.rect = Rect(self._x, self._y, self._w, self._h)
        self.__update_rect()

    def _anchor_offset(self, w, h):
        # --for lib
        from ....utils import anchor as ar
        topleft_x, topleft_y = ar(position=(0, 0), size=(w, h), anchor=self.anchor,reverse=True)
        return topleft_x, topleft_y 

    @property
    def color(self):
        return self._color
    @color.setter
    def color(self, value):
        self._color = value

    @property
    def background_color(self):
        return self._background_color
    @background_color.setter
    def background_color(self, value):
        self._background_color = value

    @property
    def anchor(self):
        return self._anchor
    @anchor.setter
    def anchor(self, value):
        self._anchor = value
        self.__update_rect()

    @property
    def alpha(self):
        return self._alpha
    @alpha.setter
    def alpha(self, value):
        self._alpha = max(0, min(255, value))

    @property
    def angle(self):
        return self._angle
    @angle.setter
    def angle(self, value):
        self._angle = value

    @property
    def anti_aliasing(self):
        return self._anti_aliasing
    @anti_aliasing.setter
    def anti_aliasing(self, value):
        self._anti_aliasing = bool(value)

    @property
    def text(self):
        return self._text
    @text.setter
    def text(self, value):
        self._text = str(value)

    @property
    def font(self):
        return self._font
    @font.setter
    def font(self, value):
        self._font = value

    @property
    def visible(self):
        return self._visible
    @visible.setter
    def visible(self, value):
        self._visible = bool(value)

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


    def __apply_anchor(self, rect):
        if hasattr(rect, self._anchor):
            setattr(rect, self._anchor, (self._x, self._y))
        else:
            rect.topleft = (self._x, self._y)   

    def __update_rect(self):
        self.__outlinerect = Rect(self._x - self.__outline_size, self._y - self.__outline_size, self._w + self.__outline_size*2, self._h + self.__outline_size*2)
        self.rect = Rect(self._x, self._y, self._w, self._h)
        self.__apply_anchor(self.rect)
        self.__apply_anchor(self.__outlinerect)
        
        if self._camera:
            self.rect = self._camera.apply(self.rect,screen_size=(self.surface.w,self.surface.h))
            
    def _split_by(self):
        return [x.strip() for x in re.split(r'[;\n]+', self._text) if x.strip()]

    def __draw_label(self):
        lines = self._split_by()
        line_height = self.height
        
        for i, l in enumerate(lines):
            y_offset = self.rect.y + i * line_height // 2
            label(
                surface=self.surface,
                text=l,
                font=self._font,
                color=self._color,
                background_color=self._background_color,
                anti_aliasing=self._anti_aliasing,
                rect=(self.rect.x, y_offset, self.rect.width, line_height)
            )

    def draw(self):
        if not self._visible:
            return
        self.__update_rect()

        self.__draw_label()

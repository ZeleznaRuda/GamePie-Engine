from ..time import wait
from ..event import mouse

from ..rect import Rect
from ..draw.text import Text

class Button:
    def __get_text_pos(self):
        # ai
        if self._font:
            font_obj = self._font.pygame_font
        else:
            import pygame
            font_obj = pygame.font.Font(None, 24)  #

        text_width, text_height = font_obj.size(self._text)
        x = self._x + (self._w - text_width) // 2
        y = self._y + (self._h - text_height) // 2
        return x, y
    
    def __init__(self, surface,text, position=(200, 200), size=(90, 50), color=(150,150,150),
                 anchor="topleft", alpha=255, image=None, angle=0,font= None,hover_color=(255,0,0), visible=True):
        self.surface = surface
        self._image = image
        self._color = color
        self._anchor = anchor
        self._alpha = alpha
        self._angle = angle
        self._w, self._h = size
        self._x, self._y = position
        self._visible = visible 
        self._text = text
        self._font = font
        self._hover_color = hover_color

        self.background = Rect(surface=self.surface, anchor=self._anchor,
                               position=(self._x, self._y), size=(self._w, self._h),
                               visible=self._visible, color=self._color,
                               angle=self._angle, alpha=self._alpha).border_radius(5,5,5,5)
        if self._image:
            self.background.texture(self._image)
        
        self.label = Text(surface=self.surface,text=self._text, anchor="topleft",
                         position=(0,0),
                         visible=self._visible, color=(0,0,0),
                         angle=self._angle,font=self._font, alpha=self._alpha)
        self.label.pos = self.__get_text_pos()

    def _set_text(self, value):
        self._text = value

    def _set_pos(self, pos):
        self._x, self._y = pos
        self.background.pos = pos
        self.label.pos = pos

    def _set_size(self, size):
        self._w, self._h = size
        self.background.size = size
        self.label.size = size

    def _set_color(self, color):
        self._color = color
        self.background.color = color
        self.label.color = color

    def _set_anchor(self, anchor):
        self._anchor = anchor
        self.background.anchor = anchor
        self.label.anchor = anchor

    def _set_alpha(self, alpha):
        self._alpha = alpha
        self.background.alpha = alpha
        self.label.alpha = alpha

    def _set_image(self, image):
        self._image = image
        self.background.texture(self._image)

    def _set_angle(self, angle):
        self._angle = angle
        self.background.angle = angle
        self.label.angle = angle

    def _set_visible(self, visible):
        self._visible = visible
        self.background.visible = visible
        self.label.visible = visible

    def draw(self):
        if not self._visible:
            return
        self.background.draw()
        self.label.draw()
    
    def _hover(self, bool):
        if bool:
            self.background.color = self._hover_color
        else:
            self.background.color = self.color

    def is_press(self):
        if wait(100, f"__Gamepie.Button.{id(self)}"):
            if self.background.collidepoint(mouse.pos) and mouse.left:
                self._hover(True)
                return True
            else:
                self._hover(False)
                return False
            

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
    @property
    def text(self):
        return self._text

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
    def text(self): return self._text

    @text.setter
    def text(self, value):
        self._set_text(value)
        if hasattr(self, "label"):
            self.label.text = value
            self.label.pos = self.__get_text_pos()
    @property
    def type(self): return "gui"
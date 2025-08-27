from ..input.event import key, mouse
from ..time import wait
from ..draw.rect import Rect
from ..draw.text import Text

class InputBox:
    def __init__(self, surface, position=(200, 200), size=(190, 90),
                 background_color=(150,150,150), text_color=(0,0,0), anchor="topleft",
                 alpha=255, font=None, visible=True):
                self.surface = surface
                self._index = 0
                self._key = key
                self._visible = visible

                self._font = font
                self._alpha = alpha
                self._anchor = anchor
                self._bg_color = background_color
                self._text_color = text_color
                self._x, self._y = position
                self._size = size
                
                self._sent = False

                self._value = []
                self._msg = []

                self.background = Rect(
                    surface,
                    position=position,
                    size=size,
                    color=background_color,
                    alpha=alpha
                ).border_radius(5, 5, 5, 5)

                self.label = Text(
                    surface,
                    text=self._value,
                    font=font,
                    position=position,
                    size=size,
                    color=text_color,
                    alpha=alpha
                )
                
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
                      
    def _update(self):
        if self.background.collidepoint(mouse.pos):
            if key.keydown:
                self._sent = False
                if key.is_down("backspace"):
                    if self._msg:
                        self._msg.pop() 
                elif key.is_down("return"):
                    self._sent = True
                else:
                    self._msg.append(key.char)

                self._value = ''.join(self._msg)
                self.label.text = self._value
    
    def draw(self):
        self._update()
        self.background.draw()
        self.label.draw()

    @property
    def value(self): 
        return self._value

    @property
    def sent(self): 
        return self._sent
       
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
    @property
    def type(self): return "gui"
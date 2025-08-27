from ..rect import Rect
from ..draw.text import Text

class Message:
    def __init__(self, surface, text, position=(200, 200), size=(90, 30), partner=None,
                 color=(255, 255, 255), anchor="topleft", alpha=255, font = None, visible=True):
        
        self.surface = surface
        self._color = color
        self._anchor = anchor
        self._alpha = alpha
        self._w, self._h = size
        self._partner = partner
        self._visible = visible
        self._text = text
        self._font = font

        self._x, self._y = position
        if self._partner:
            self._y = self._partner.y - self._partner.height // 5
            self._x = self._partner.x - self._partner.width

        self.box = Rect(
            surface,
            position=(self._x, self._y),
            size=(self._w, self._h),
            color=self._color,
            alpha=self._alpha
        ).border_radius(50, 50, 1, 50)

        self.text = Text(
            surface,
            position=(self._x + font.size, self._y + self._h // 5),
            font=font,
            text=self._text
        )

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
    def text_value(self):
        return self._text

    @text_value.setter
    def text_value(self, value):
        self._set_text(value)

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._set_color(value)

    @property
    def alpha(self):
        return self._alpha

    @alpha.setter
    def alpha(self, value):
        self._set_alpha(value)

    @property
    def font(self):
        return self._font

    @font.setter
    def font(self, value):
        self._set_font(value)

    @property
    def visible(self):
        return self._visible

    @visible.setter
    def visible(self, value):
        self._set_visible(value)

    @property
    def anchor(self):
        return self._anchor

    @anchor.setter
    def anchor(self, value):
        self._set_anchor(value)

    @property
    def partner(self):
        return self._partner

    @partner.setter
    def partner(self, value):
        self._set_partner(value)

    def _set_pos(self, x, y):
        self._x, self._y = x, y
        self.box._set_pos((self._x, self._y))
        self.text._set_pos((self._x + self._font.size, self._y + self._h // 5))

    def _set_size(self, width, height):
        self._w, self._h = width, height
        self.box._set_size((self._w, self._h))
        self.text._set_pos((self._x + self._font.size, self._y + self._h // 5))

    def _set_text(self, text):
        self._text = text
        self.text._set_text(text)

    def _set_color(self, color):
        self._color = color
        self.box._set_color(color)

    def _set_alpha(self, alpha):
        self._alpha = alpha
        self.box._set_alpha(alpha)

    def _set_font(self, font):
        self._font = font
        self.text._set_font(font)
        self.text._set_pos((self._x + font.size, self._y + self._h // 5))

    def _set_visible(self, visible: bool):
        self._visible = visible

    def _set_anchor(self, anchor):
        self._anchor = anchor

    def _set_partner(self, partner):
        self._partner = partner
        if self._partner:
            self._y = self._partner.y - self._partner.height // 5
            self._x = self._partner.x - self._partner.width
            self._set_pos(self._x, self._y)

    def draw(self):
        if not self._visible:
            return
        if self._partner:
            self._set_partner(self._partner)
        self.box.draw()
        self.text.draw()
    @property
    def type(self): return "gui"
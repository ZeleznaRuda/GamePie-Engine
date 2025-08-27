from ..rect import Rect
from ..draw.image import Image
from ..draw.text import Text
from ..func import anchor as ar
#my///ai
class Label:
    def __init__(self, surface, text=None, image=None, position=(200, 200), size=(90, 90),
                 color=(255, 255, 255), anchor="topleft", alpha=255, font= None, visible=True):
        self.surface = surface
        self._color = color
        self._anchor = anchor
        self._alpha = alpha
        self._w, self._h = size
        self._x, self._y = position
        self._visible = visible
        self._text = text
        self._img = image
        self._font = font
        self.__c_offset_pos = (self._w // 4, self._h // 4)
        self.__c_offset_size = (self._w // 2, self._h // 2)

        # Create background rect
        self.background = Rect(
            surface,
            position=(self._x, self._y),
            size=(self._w, self._h),
            color=self._color,
            alpha=self._alpha
        )

        # Apply anchor
        

        # Create content
        self.text = None
        self.image = None
        if self._text:
            self._create_text()
        elif self._img:
            self._create_image()
    def _calibrate_content(self):
        self.__c_offset_pos = (self._w // 4, self._h // 4)
        self.__c_offset_size = (self._w // 2, self._h // 2)
    def _create_text(self):
        offx, offy = self.__c_offset_pos
        offw, offh = self.__c_offset_size
        self.text = Text(
            self.surface,
            position=(self._x + offx,self._y + offy),
            size=(offw,offh),
            font=self._font,
            text=self._text
        )

    def _create_image(self):
        offx, offy = self.__c_offset_pos
        offw, offh = self.__c_offset_size
        self.image = Image(
            self.surface,
            texture=self._img,
            position=(self._x + offx,self._y + offy),
            size=(offw,offh),
        )


    def content_offset(self, position=(50, 50), size=(50, 50)):
        self.__c_offset_pos = position
        self.__c_offset_size = size
        # Redraw content
        if self._text:
            self._create_text()
        elif self._img:
            self._create_image()
        return self

    def draw(self):
        if not self._visible:
            return
        self.background.draw()
        if self.text:
            self.text.draw()
        elif self.image:
            self.image.draw()


    @property
    def pos(self):
        return (self._x, self._y)

    @pos.setter
    def pos(self, value):
        self._set_pos(*value)

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._set_pos(value, self._y)

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._set_pos(self._x, value)

    @property
    def width(self):
        return self._w

    @width.setter
    def width(self, value):
        self._set_size(value, self._h)

    @property
    def height(self):
        return self._h

    @height.setter
    def height(self, value):
        self._set_size(self._w, value)


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

    def _set_pos(self, x, y):
        self._x, self._y = x, y
        
        self.background.pos = (self._x, self._y)
        if self.text:
            self.text.pos = (self._x, self._y)
        elif self.image:
            self.image.pos = (self._x, self._y)

    def _set_size(self, width, height):
        self._w, self._h = width, height
        self.background._set_size((self._w, self._h))
        if self.text:
            self.text._set_size((self._w + self.__c_offset_size[0], self._h + self.__c_offset_size[1]))
        elif self.image:
            self.image._set_size((self._w - self.__c_offset_size[0], self._h - self.__c_offset_size[1]))

    def _set_text(self, text):
        self._text = text
        if self.text:
            self.text._set_text(text)
        else:
            self._create_text()

    def _set_color(self, color):
        self._color = color
        self.background._set_color(color)

    def _set_alpha(self, alpha):
        self._alpha = alpha
        self.background._set_alpha(alpha)

    def _set_font(self, font):
        self._font = font
        if self.text:
            self.text._set_font(font)
        else:
            self._create_text()

    def _set_visible(self, visible: bool):
        self._visible = visible

    def _set_anchor(self, anchor):
        self._anchor = anchor
        
        self._set_pos(self._x, self._y)  
    @property
    def type(self): return "gui"
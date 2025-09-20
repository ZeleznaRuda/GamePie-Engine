from gamepie.core.draw.rect import Rectangle
from gamepie.core.draw.gui.lable import Label
from gamepie.core.load.font import Font
from gamepie.core.event import key, mouse
from gamepie.utils import uicamera
from gamepie.core.time import wait


class InputBox:
    def __init__(self, surface, text="", font=Font(), image=None,
                 text_color=(255, 255, 255), color=(80, 80, 80),
                 position=(50, 50), size=(150, 30), anchor="topleft",
                 camera=uicamera, visible=True, enable=True):
        self.surface = surface
        self._x, self._y = position
        self._w, self._h = size
        self._anchor = anchor
        self._camera = camera
        self._text = text
        self._image = image
        self._color = color
        self._text_color = text_color
        self._font = font
        self._visible = visible
        self._enable = enable
        self._active = False
        self._cursor_visible = True
        self._cursor_timer = 0
        self._enter = False

        self._label = Label(surface, text=self._text, font=self._font,
                            position=(self._x + 5, self._y + 5),
                            size=(self._w - 10, self._h - 10),
                            color=self._text_color,
                            anchor=self._anchor,
                            camera=self._camera,
                            background_color=None)

        self._background = Rectangle(surface, position=(self._x, self._y),
                                     size=(self._w, self._h),
                                     color=self._color,
                                     anchor=self._anchor,
                                     camera=self._camera).border_radius(5, 5, 5, 5)

    # --- Propertyy ---
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value
        self._update_rect()

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value
        self._update_rect()

    @property
    def pos(self):
        return self._x, self._y

    @pos.setter
    def pos(self, value):
        self._x, self._y = value
        self._update_rect()

    @property
    def width(self):
        return self._w

    @width.setter
    def width(self, value):
        self._w = value
        self._update_rect()

    @property
    def height(self):
        return self._h

    @height.setter
    def height(self, value):
        self._h = value
        self._update_rect()

    @property
    def size(self):
        return self._w, self._h

    @size.setter
    def size(self, value):
        self._w, self._h = value
        self._update_rect()

    @property
    def visible(self):
        return self._visible

    @visible.setter
    def visible(self, value):
        self._visible = value

    @property
    def enable(self):
        return self._enable

    @enable.setter
    def enable(self, value):
        self._enable = value

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = str(value)
        self._label.text = self._text

    @property
    def active(self):
        return self._active

    @active.setter
    def active(self, value):
        self._active = bool(value)

    @property
    def color(self):
        return self._color

    @property
    def background(self):
        return self._background

    @property
    def label(self):
        return self._label

    @color.setter
    def color(self, value):
        self._color = value
        self._background.color = self._color

    @property
    def text_color(self):
        return self._text_color

    @text_color.setter
    def text_color(self, value):
        self._text_color = value
        self._label.color = self._text_color

    @property
    def font(self):
        return self._font

    @font.setter
    def font(self, value):
        self._font = value
        self._label.font = self._font

    # --- Interní metody ---
    def _update_rect(self):
        self._background.pos = (self._x, self._y)
        self._background.size = (self._w, self._h)
        self._label.position = (self._x + 5, self._y + 5)
        self._label.size = (self._w - 10, self._h - 10)

    def handle_event(self):
        if not self._enable:
            return

        if mouse.left and self._background.collision.point(mouse.pos):
            self._active = True
        elif mouse.left:
            self._active = False

        if self._active:
            if key.is_down("backspace"):
                if wait(500, f"__Lib.InputBox.{id(self)}:backspace :: Delay -> 500"):
                    self._text = self._text[:-1]
                self._enter = False
            elif key.is_down("return"):
                self._enter = True
                self._active = False
            else:
                char = key.char
                if char:
                    self._text += char
            self._label.text = str(self._text)

    def draw(self):
        if not self._visible or not self._enable:
            return

        self.handle_event()
        self._background.draw()
        self._label.draw()

        if self._active:
            if wait(500, f"__Lib.InputBox.{id(self)}:bCur :: Delay -> 500"):
                self._cursor_visible = not self._cursor_visible

            if self._cursor_visible:
                cursor_x = self._x + 5 + len(self._text) * 8
                cursor_y = self._y + 5
                Rectangle(self.surface, position=(cursor_x, cursor_y),
                          size=(2, self._h - 10), color=self._text_color,
                          camera=self._camera).draw()

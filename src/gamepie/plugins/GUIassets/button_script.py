from gamepie.core.draw.rect import Rectangle
from gamepie.core.rect import Rect
from gamepie.core.draw.image import Image
from gamepie.core.load.texture import Texture
from gamepie.core.load.font import Font
from gamepie.core.draw.gui.lable import Label
from gamepie.core.event import mouse
from gamepie.core.time import wait
from gamepie.utils import uicamera
from gamepie.utils.func import anchor as ar


class Button:
    def __init__(self, surface, text="Press me.", font=Font(), image=None,
                 text_color=(255, 255, 255), color=(80, 80, 80),
                 position=(50, 50), size=(80, 30), anchor="topleft",
                 camera=uicamera, visible=True, deley=100):
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
        self._hover = False
        self._deley = deley

        self._label = Label(self.surface, text=self._text, font=self._font,
                            position=(self._x, self._y),
                            size=(self._w, self._h),
                            color=self._text_color,
                            background_color=None,
                            anchor=self._anchor,
                            camera=self._camera)
        self._label.pos = self.__get_text_pos()

        if image:
            self._background = Image(self.surface, texture=self._image,
                                     position=(self._x, self._y),
                                     size=(self._w, self._h),
                                     anchor=self._anchor, camera=self._camera)
        else:
            self._background = Rectangle(self.surface, position=(self._x, self._y),
                                         size=(self._w, self._h), color=self._color,
                                         anchor=self._anchor, camera=self._camera).border_radius(5, 5, 5, 5)

    # --- Interní metody ---
    def __get_text_pos(self):
        if self._font:
            font_obj = self._font()
        else:
            import pygame
            font_obj = pygame.font.Font(None, 24)
        text_width, text_height = font_obj.size(self._text)
        x = self._x + (self._w - text_width) // 2
        y = self._y + (self._h - text_height) // 2
        return x, y

    def _update_rect(self):
        self._background.pos = (self._x, self._y)
        self._background.size = (self._w, self._h)
        self._label.pos = self.__get_text_pos()
        self._label.size = (self._w, self._h)

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
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = str(value)
        self._label.text = self._text
        self._update_rect()

    @property
    def font(self):
        return self._font

    @font.setter
    def font(self, value):
        self._font = value
        self._label.font = self._font
        self._update_rect()

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value
        if isinstance(self._background, Rectangle):
            self._background.color = self._color

    @property
    def text_color(self):
        return self._text_color

    @text_color.setter
    def text_color(self, value):
        self._text_color = value
        self._label.color = self._text_color

    @property
    def background(self):
        return self._background

    @property
    def label(self):
        return self._label

    # --- Interakce ---
    def is_press(self):
        if wait(self._deley, f"__Lib.Button.{id(self)}:Deley -> {self._deley}"):
            if self._background.collision.point(mouse.pos) and mouse.left:
                self._hover = True
                return True
            else:
                self._hover = False
                return False

    def draw(self):
        if not self._visible:
            return
        self._background.draw()
        self._label.draw()

import pygame
from ..load.texture import Texture 
from ..func import anchor

class Image:
    def __init__(self, surface, texture: Texture, position=(0, 0), size=(50, 50), color=(255, 255, 255),
                 anchor="topleft", alpha=255, angle=0, visible=True):
        self.surface = surface
        self._color = color
        self._anchor = anchor
        self._alpha = alpha
        self._angle = angle
        self._visible = visible 
        self._w, self._h = size
        self._x, self._y = position

        self.__texture = texture
        self.__image_drawn = False
        self.__destroyed = False
        self.__outline = False
        self.__outline_color = (0, 0, 0)
        self.__outline_size = 0
        self.__final_image = None 
        
        self.__final_pos = (self._x, self._y)
        
    @property
    def x(self): return self._x
    @x.setter
    def x(self, value): self._set_pos(value, self._y)

    @property
    def y(self): return self._y
    @y.setter
    def y(self, value): self._set_pos(self._x, value)

    @property
    def pos(self): return (self._x, self._y)
    @pos.setter
    def pos(self, pos): self._set_pos(*pos)

    @property
    def width(self): return self._w
    @width.setter
    def width(self, value): self._set_size(value, self._h)

    @property
    def height(self): return self._h
    @height.setter
    def height(self, value): self._set_size(self._w, value)

    @property
    def size(self): return (self._w, self._h)
    @size.setter
    def size(self, size): self._set_size(*size)

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
    def visible(self): return self._visible
    @visible.setter
    def visible(self, value): self._set_visible(value)

    @property
    def anchor(self): return self._anchor
    @anchor.setter
    def anchor(self, value): self._set_anchor(value)

    @property
    def texture(self): return self.__texture
    @texture.setter
    def texture(self, value): self._set_texture(value)
          
    def _set_pos(self, x, y):
        self._x, self._y = x, y
        self.__final_pos = (self._x, self._y)
        if self._anchor:
            self.__final_pos = anchor(position=(self._x, self._y), size=(self._w, self._h), anchor=self._anchor)
        

    def _set_size(self, w, h):
        self._w, self._h = w, h
        

    def _set_color(self, color):
        self._color = color
        

    def _set_alpha(self, alpha):
        self._alpha = alpha
        

    def _set_angle(self, angle):
        self._angle = angle
        

    def _set_visible(self, visible: bool):
        self._visible = visible
        

    def _set_anchor(self, anchor):
        self._anchor = anchor
        

    def _set_texture(self, texture: Texture):
        self.__texture = texture


    def outline(self, color, size):
        self.__outline = True
        self.__outline_color = color
        self.__outline_size = size
        return self
    def __draw_outline_image(self):
        if self.__outline and self.__outline_size > 0:
            outline_surface = pygame.Surface(
                (colored_img.get_width() + 2 * self.__outline_size,
                colored_img.get_height() + 2 * self.__outline_size), pygame.SRCALPHA)

            for dx in range(-self.__outline_size, self.__outline_size + 1):
                for dy in range(-self.__outline_size, self.__outline_size + 1):
                    if dx == 0 and dy == 0:
                        continue
                    temp = colored_img.copy()
                    temp.fill(self.__outline_color, special_flags=pygame.BLEND_RGBA_MULT)
                    outline_surface.blit(temp, (dx + self.__outline_size, dy + self.__outline_size))

            outline_surface.blit(colored_img, (self.__outline_size, self.__outline_size))
            self.surface.blit(outline_surface, (self.__final_pos[0] - self.__outline_size, self.__final_pos[1] - self.__outline_size))
    def draw(self):
        if not self._visible:
            return
        self.__draw_image()

    def __draw_image(self):
        img = self.__texture.image if hasattr(self.__texture, "image") else self.__texture
        if not isinstance(img, pygame.Surface):
            return

        scaled_img = pygame.transform.scale(img, (self._w, self._h))

        if self._angle != 0:
            scaled_img = pygame.transform.rotate(scaled_img, self._angle)

        colored_img = scaled_img.copy()
        colored_img.fill((*self._color, self._alpha), special_flags=pygame.BLEND_RGBA_MULT)

        if self.__outline and self.__outline_size > 0:
        else:
            self.surface.blit(colored_img, self.__final_pos)

        self.__image_drawn = True
        self.__final_image = colored_img

    @property
    def type(self): return "mgo"

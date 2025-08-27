import pygame
from ...load.texture import Texture
from ..image import Image
from ...func import anchor
from ...pather import *

class Rect:
    def __init__(self, surface, position=(0, 0), size=(60, 50), color=(255, 255, 255),
                 anchor="topleft", alpha=255, angle=0, visible=True):
        self.surface = surface
        self._color = color
        self._anchor = anchor
        self._alpha = alpha
        self._angle = angle
        self.__image = False
        self.__destroyed = False
        self.__confirmed_border_radius = False
        self.__outline = False
        self.__outline_color = (0,0,0)
        self.__outline_size = 0
        self.__border_radius = 0
        self.__border_bottom_left_radius=0
        self.__border_top_left_radius=0
        self.__border_bottom_right_radius=0
        self.__border_top_right_radius=0

        self._w, self._h = size
        self._x, self._y = position
        
        self.rect = pygame.Rect(self._x, self._y, self._w, self._h)
        self._visible = visible 
        self.__type = "mgo"
        self._set_pos((self._x, self._y))

    def _set_pos(self, pos):
        if self.__destroyed:
            return
        x, y = anchor(position=pos, size=(self._w, self._h), anchor=self._anchor)
        self._x, self._y = x, y
        self.rect.topleft = (x, y)
        if self.__image:
            self.__editimg.pos = (x, y)


    def copy(self):
        self.rect.copy()

    def move_ip(self, x, y):
        self.rect.move_ip(x, y)

    def center_on(self, pos):
        self.rect.center = pos
        self._x, self._y = getattr(self.rect, self._anchor)

    def collidepoint(self, point):
        return self.rect.collidepoint(point)

    def colliderect(self, other_rect):
        if isinstance(other_rect, Rect):
            other_rect = other_rect.rect
        return self.rect.colliderect(other_rect)

    def contains(self, other_rect):
        if isinstance(other_rect, Rect):
            other_rect = other_rect.rect
        return self.rect.contains(other_rect)

    def clamp_ip(self, other_rect):
        if isinstance(other_rect, Rect):
            other_rect = other_rect.rect
        self.rect.clamp_ip(other_rect)
        self._x, self._y = getattr(self.rect, self._anchor)

    def inflate_ip(self, dx, dy):
        self.rect.inflate_ip(dx, dy)
        self._set_size(*self.rect.size)

    def normalize(self):
        self.rect.normalize()
        self._x, self._y = getattr(self.rect, self._anchor)
        self._set_size(*self.rect.size)

    def destroy(self):
        # /ai
        self.__destroyed = True
        self.surface = None
        self._color = None
        self.rect = None

    def _check_destroyed(self):
        if self.__destroyed:
            raise Exception("The Rect object has been destroyed and can no longer be used.")

    def _set_size(self, w, h):
        if self.__destroyed:
            return
        self._w, self._h = w, h
        self.rect.size = (w, h)
        if self.__image:
            self.__editimg.size = (w, h)

    def _set_color(self, color):
        if self.__destroyed:
            return
        self._color = color
        if self.__image:
            self.__editimg.color = color

    def _set_anchor(self, anchor):
        if self.__destroyed:
            return
        self._anchor = anchor
        self._set_pos((self._x, self._y))
        if self.__image:
            self.__editimg.anchor = anchor

    def _set_visible(self, visible):
        self._visible = visible
        if self.__image:
            self.__editimg.visible = visible

    def _set_alpha(self, value):
        if self.__destroyed:
            return
        self._alpha = max(0, min(255, value))
        if self.__image:
            self.__editimg.alpha = max(0, min(255, value))

    def _set_angle(self, value):
        if self.__destroyed:
            return
        self._angle = value
        if self.__image:
            self.__editimg.angle = value

    def texture(self, img: Texture):
        self.__image = True
        if not self._visible:
            return
        if hasattr(img, 'image'):
            img = img.image
        self.__editimg = Image(surface=self.surface, texture=img,position=(self._x, self._y),size=(self._w, self._h),color=self._color,anchor=self._anchor, alpha=self._alpha,angle=self._angle,visible=self._visible)
        return self
    def outline(self, color, size):
        self.__outline = True
        self.__outline_color = color
        self.__outline_size = size
        return self
    
    def __draw_outline(self):
        if self.__outline and not self.__image:
            pygame.draw.rect(self.surface, (self.__outline_color), (self._x, self._y, self._w, self._h), self.__outline_size)
        if self.__outline and self.__image:
            self.__editimg.outline((self.__outline_color), self.__outline_size)

    def __draw_image(self):
        self.__editimg.draw()

    # border_radius: ///ai
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


    def _draw_border_radius(self):
        if self.__confirmed_border_radius:
            rect_surface = pygame.Surface((self._w, self._h), pygame.SRCALPHA)
            pygame.draw.rect(
                rect_surface,
                (*self._color, self._alpha),
                rect_surface.get_rect(),

                border_top_left_radius=self.__border_top_left_radius,
                border_top_right_radius=self.__border_top_right_radius,
                border_bottom_left_radius=self.__border_bottom_left_radius,
                border_bottom_right_radius=self.__border_bottom_right_radius,
            )
            self.surface.blit(rect_surface, (self._x, self._y))



    def draw(self):
        # h/ai
        if self.__destroyed:
            return 
        if not self._visible:
            return
        if not self.__image:
            if self.__confirmed_border_radius:
                self._draw_border_radius()
            else:
                rect_surface = pygame.Surface((self._w, self._h), pygame.SRCALPHA)
                rect_surface.fill((*self._color, self._alpha))
                if self._angle != 0:
                    rotated = pygame.transform.rotate(rect_surface, self._angle)
                    new_rect = rotated.get_rect(center=(self._x + self._w // 2, self._y + self._h // 2))
                    self.surface.blit(rotated, new_rect.topleft)
                else:
                    self.surface.blit(rect_surface, (self._x, self._y))
        else:
            self.__draw_image()
        self.__draw_outline()


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
    def topleft(self):
        return anchor(position=(self._x, self._y), size=(self._w, self._h), anchor="topleft")
    @topleft.setter
    def topleft(self, value):
        self._set_pos(anchor(position=value, size=(self._w, self._h), anchor="topleft"))

    @property
    def topright(self):
        return anchor(position=(self._x, self._y), size=(self._w, self._h), anchor="topright")
    @topright.setter
    def topright(self, value):
        self._set_pos(anchor(position=value, size=(self._w, self._h), anchor="topright"))

    @property
    def midtop(self):
        return anchor(position=(self._x, self._y), size=(self._w, self._h), anchor="midtop")
    @midtop.setter
    def midtop(self, value):
        self._set_pos(anchor(position=value, size=(self._w, self._h), anchor="midtop"))

    @property
    def center(self):
        return anchor(position=(self._x, self._y), size=(self._w, self._h), anchor="center")
    @center.setter
    def center(self, value):
        self._set_pos(anchor(position=value, size=(self._w, self._h), anchor="center"))

    @property
    def midleft(self):
        return anchor(position=(self._x, self._y), size=(self._w, self._h), anchor="midleft")
    @midleft.setter
    def midleft(self, value):
        self._set_pos(anchor(position=value, size=(self._w, self._h), anchor="midleft"))

    @property
    def midright(self):
        return anchor(position=(self._x, self._y), size=(self._w, self._h), anchor="midright")
    @midright.setter
    def midright(self, value):
        self._set_pos(anchor(position=value, size=(self._w, self._h), anchor="midright"))

    @property
    def bottomleft(self):
        return anchor(position=(self._x, self._y), size=(self._w, self._h), anchor="bottomleft")
    @bottomleft.setter
    def bottomleft(self, value):
        self._set_pos(anchor(position=value, size=(self._w, self._h), anchor="bottomleft"))

    @property
    def midbottom(self):
        return anchor(position=(self._x, self._y), size=(self._w, self._h), anchor="midbottom")
    @midbottom.setter
    def midbottom(self, value):
        self._set_pos(anchor(position=value, size=(self._w, self._h), anchor="midbottom"))

    @property
    def bottomright(self):
        return anchor(position=(self._x, self._y), size=(self._w, self._h), anchor="bottomright")
    @bottomright.setter
    def bottomright(self, value):
        self._set_pos(anchor(position=value, size=(self._w, self._h), anchor="bottomright"))

    @property
    def type(self): return self.__type

    def __repr__(self):
        return repr(self.rect)
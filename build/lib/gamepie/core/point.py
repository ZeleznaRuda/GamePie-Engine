from .collision import _Collision
from .cam import Camera
from ..utils import  uicamera
class Point:
    def __init__(self,surface, x, y,width=5,camera:Camera=uicamera):
        self.surface = surface
        self._x = x
        self._y = y
        self._width = width
        self._camera = camera
    def __update_point(self):
        if self._camera:
            self.rect = self._camera.apply(self.rect,screen_size=(self.surface.w,self.surface.h))
            self.__outlinerect = self._camera.apply(self.__outlinerect,screen_size=(self.surface.w,self.surface.h))
    def __iter__(self):
        yield self._x
        yield self._y

    def __repr__(self):
        return f"Point({self._x}, {self._y})"
    @property
    def x(self): 
        return self._x

    @x.setter
    def x(self, value): 
        self._x = value
        self.__update_point()

    @property
    def y(self): 
        return self._y

    @y.setter
    def y(self, value): 
        self._y = value
        self.__update_point()

    @property
    def pos(self): 
        return self._x, self._y

    @pos.setter
    def pos(self, value): 
        self._x, self._y = value
        self.__update_point()

    @property
    def width(self): return self._width

    @width.setter
    def width(self, value): 
        self._width = value
        self.__update_point()
    def collision(self): return _Collision(self)
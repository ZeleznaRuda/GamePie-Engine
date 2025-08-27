from .rect import Rect
from .func import anchor as ar

class Camera:
    def __init__(self, position=(0, 0), zoom=1.0, anchor="center"):
        self._zoom = zoom
        self._anchor = anchor
        self._x, self._y = position

    def move(self, dx, dy):
        self._x += dx
        self._y += dy

    def apply(self, rect, screen_size):
        if not isinstance(rect, Rect):
            raise TypeError(f"Expected Rect, got {type(rect)}")

        ox, oy = ar((0, 0), screen_size, self._anchor)
        cam_x = self._x + ox / self._zoom
        cam_y = self._y + oy / self._zoom

        return Rect(
            (rect.x - cam_x) * self._zoom,
            (rect.y - cam_y) * self._zoom,
            rect.width * self._zoom,
            rect.height * self._zoom,
        )

    def screen_to_world(self, screen_x, screen_y, screen_size):
        ox, oy = ar((0, 0), screen_size, self._anchor)
        world_x = (screen_x - ox) / self._zoom + self._x
        world_y = (screen_y - oy) / self._zoom + self._y
        return world_x, world_y

    @property
    def pos(self):
        return self._x, self._y

    @pos.setter
    def pos(self, value):
        self._x, self._y = value
        
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value
        
    @property
    def zoom(self):
        return self._zoom

    @zoom.setter
    def zoom(self, value):
        if value <= 0:
            raise ValueError("zoom cannot be 0 or negative")
        self._zoom = value


camera = Camera(anchor="center")
uicamera = Camera(anchor="topleft")

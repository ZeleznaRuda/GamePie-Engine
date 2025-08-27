from .func import anchor as ar
from .func import anchor
from .collision import _Collision
class Rect:
    def __init__(self, x, y, width, height, anchor="topleft"):
        self._w = width
        self._h = height
        self._anchor = anchor
        self._x, self._y = ar(position=(x, y), size=(width, height), anchor=anchor)

    def _set_anchor(self, anchor_name, value):
        self._x, self._y = anchor(position=value, size=(self._w, self._h), anchor=anchor_name)

    def _get_anchor(self, anchor_name):
        return anchor(position=(self._x, self._y), size=(self._w, self._h), anchor=anchor_name)


    def move(self, dx, dy):
        return Rect(self._x + dx, self._y + dy, self._w, self._h)

    def inflate(self, dx, dy):
        return Rect(
            self._x - dx // 2,
            self._y - dy // 2,
            self._w + dx,
            self._h + dy
        )

    def union(self, other):
        x1 = min(self._x, other.x)
        y1 = min(self._y, other.y)
        x2 = max(self._x + self._w, other.x + other.width)
        y2 = max(self._y + self._h, other.y + other.height)
        return Rect(x1, y1, x2 - x1, y2 - y1)

    def clip(self, other):
        x1 = max(self._x, other.x)
        y1 = max(self._y, other.y)
        x2 = min(self._x + self._w, other.x + other.width)
        y2 = min(self._y + self._h, other.y + other.height)
        if x2 <= x1 or y2 <= y1:
            return Rect(0, 0, 0, 0)
        return Rect(x1, y1, x2 - x1, y2 - y1)

    def normalize(self):
        if self._w < 0:
            self._x += self._w
            self._w = -self._w
        if self._h < 0:
            self._y += self._h
            self._h = -self._h
    def _anchor_offset(self, w, h):
        # --for lib
        topleft_x, topleft_y = ar(position=(0, 0), size=(w, h), anchor=self._anchor,reverse=True)
        return topleft_x, topleft_y
    @property
    def x(self): return self._x
    @x.setter
    def x(self, value): self._x = value

    @property
    def y(self): return self._y
    @y.setter
    def y(self, value): self._y = value

    @property
    def pos(self): return (self._x, self._y)
    @pos.setter
    def pos(self, value): self._x, self._y = value

    @property
    def width(self): return self._w
    @width.setter
    def width(self, value): self._w = value

    @property
    def height(self): return self._h
    @height.setter
    def height(self, value): self._h = value

    @property
    def size(self): return (self._w, self._h)
    @size.setter
    def size(self, value): self._w, self._h = value

    @property
    def topleft(self): return self._get_anchor("topleft")
    @topleft.setter
    def topleft(self, value): self._set_anchor("topleft", value)

    @property
    def topright(self): return self._get_anchor("topright")
    @topright.setter
    def topright(self, value): self._set_anchor("topright", value)

    @property
    def midtop(self): return self._get_anchor("midtop")
    @midtop.setter
    def midtop(self, value): self._set_anchor("midtop", value)

    @property
    def center(self): return self._get_anchor("center")
    @center.setter
    def center(self, value): self._set_anchor("center", value)

    @property
    def midleft(self): return self._get_anchor("midleft")
    @midleft.setter
    def midleft(self, value): self._set_anchor("midleft", value)

    @property
    def midright(self): return self._get_anchor("midright")
    @midright.setter
    def midright(self, value): self._set_anchor("midright", value)

    @property
    def bottomleft(self): return self._get_anchor("bottomleft")
    @bottomleft.setter
    def bottomleft(self, value): self._set_anchor("bottomleft", value)

    @property
    def midbottom(self): return self._get_anchor("midbottom")
    @midbottom.setter
    def midbottom(self, value): self._set_anchor("midbottom", value)

    @property
    def bottomright(self): return self._get_anchor("bottomright")
    @bottomright.setter
    def bottomright(self, value): self._set_anchor("bottomright", value)
    @property
    def collision(self): return _Collision(self)
    def __iter__(self):
        yield self._x
        yield self._y
        yield self._w
        yield self._h

    def __repr__(self):
        return f"Rect({self._x}, {self._y}, {self._w}, {self._h})"

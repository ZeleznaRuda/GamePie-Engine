import pygame

class _Collision:
    def __init__(self, obj):
        self._object = obj

    def _get_world_rect(self, obj):
        w, h = obj.size
        x, y = obj.pos  # světové souřadnice
        ax, ay = obj._anchor_offset(w, h)
        return pygame.Rect(x - ax, y - ay, w, h)

    def rect(self, other):
        r1 = self._get_world_rect(self._object)
        r2 = self._get_world_rect(other)
        return r1.colliderect(r2)

    def mesh(self, other):
        r1 = self._get_world_rect(self._object)
        r2 = self._get_world_rect(other)

        # maska pro self._object
        if hasattr(self._object, 'texture') and self._object.texture():
            mask1 = pygame.mask.from_surface(self._object.texture())
        else:
            mask1 = pygame.Mask((r1.width, r1.height), fill=True)

        # maska pro other
        if hasattr(other, 'texture') and other.texture():
            mask2 = pygame.mask.from_surface(other.texture())
        else:
            mask2 = pygame.Mask((r2.width, r2.height), fill=True)

        offset = (int(r2.x - r1.x), int(r2.y - r1.y))
        return mask1.overlap(mask2, offset) is not None

    def on_ground(self, other, tolerance=5):
        # my//ai
        r1 = self._get_world_rect(self._object)
        r2 = self._get_world_rect(other)
        # spodní část objektu
        bottom = r1.bottom
        # horní část druhého objektu
        top = r2.top
        return top <= bottom <= top + tolerance

    def point(self,px ,py):
        return self._x <= px < self._x + self._w and self._y <= py < self._y + self._h

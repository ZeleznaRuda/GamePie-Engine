import pygame


class _Collision:
    def __init__(self, obj):
        self._object = obj
        self._x = obj.x
        self._y = obj.y
        self._w = obj.width
        self._h = obj.height
    
    def _get_world_rect(self, obj):

        w, h = obj.size
        x, y = obj.pos 
        ax, ay = obj._anchor_offset(w, h)
        return pygame.Rect(x - ax, y - ay, w, h)

    def rect(self, other, offset=None):
        if not other.enable:
            return
        #my//////offset->ai
        r1 = self._get_world_rect(self._object)
        r2 = self._get_world_rect(other)

        if offset:
            # offset (x, y, width_offset, height_offset)
            x_off, y_off, w_off, h_off = offset
            r1 = r1.move(x_off, y_off)        
            r1.width  += w_off               
            r1.height += h_off

        return r1.colliderect(r2)

    def mesh(self, other):
        if not other.enable:
            return
        r1 = self._get_world_rect(self._object)
        r2 = self._get_world_rect(other)


        if hasattr(self._object, 'texture') and self._object.texture():
            mask1 = pygame.mask.from_surface(self._object.texture())
        else:
            mask1 = pygame.Mask((r1.width, r1.height), fill=True)


        if hasattr(other, 'texture') and other.texture():
            mask2 = pygame.mask.from_surface(other.texture())
        else:
            mask2 = pygame.Mask((r2.width, r2.height), fill=True)

        offset = (int(r2.x - r1.x), int(r2.y - r1.y))
        return mask1.overlap(mask2, offset) is not None

    def on_ground(self, other, tolerance=5):
        if not other.enable:
            return
        # my//ai
        r1 = self._get_world_rect(self._object)
        r2 = self._get_world_rect(other)
 
        bottom = r1.bottom
      
        top = r2.top
        return top <= bottom <= top + tolerance
    def point(self, position):
        px, py = position
        r1 = self._get_world_rect(self._object)
        return r1.collidepoint(px, py)

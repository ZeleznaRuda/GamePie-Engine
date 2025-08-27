import pygame

class Mask:
    def __init__(self, surface=None):
        self._surface = None
        self._mask = None
        if callable(surface):
            self.surface = surface()
            self._mask = pygame.mask.from_surface(self.surface)

    @property
    def mask(self):
        return self._mask

    @mask.setter
    def mask(self, value):
        # Povolit jen pygame.Mask nebo None
        if value is not None and not isinstance(value, pygame.Mask):
            raise TypeError("mask musí být pygame.Mask nebo None")
        self._mask = value

    @classmethod
    def from_bitmask(cls, bitmask):
        mask = pygame.Mask((len(bitmask[0]), len(bitmask)))
        for y, row in enumerate(bitmask):
            for x, val in enumerate(row):
                if val:
                    mask.set_at((x, y), 1)
        obj = cls()
        obj.mask = mask
        return obj

    def to_surface(self, setcolor=(255,255,255,255), unsetcolor=(0,0,0,0)):
        if self.mask:
            return self.mask.to_surface(setcolor=setcolor, unsetcolor=unsetcolor)
        return None
    

    def overlap(self, other_mask, offset):
        if self.mask and other_mask.mask:
            return self.mask.overlap(other_mask.mask, offset)
        return None

    def overlap_area(self, other_mask, offset):
        if self.mask and other_mask.mask:
            return self.mask.overlap_area(other_mask.mask, offset)
        return 0

    def get_bounding_rect(self):
        if self.mask:
            return self.mask.get_bounding_rects()
        return None

    def move(self, offset):
        if self.mask:
            self.mask = self.mask.move(offset)

    def invert(self):
        if self.mask:
            self.mask.invert()

    def fill(self):
        if self.mask:
            self.mask.fill()

    def get_size(self):
        if self.mask:
            return self.mask.get_size()
        return (0, 0)

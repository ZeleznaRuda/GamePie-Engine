import pygame
from ...pather import paths
from ..rect import Rect
from .. import _gp_log
class Texture:
    def __init__(self, path: str, msg=True,mod=False):
        if mod:
            pygame.init()
            pygame.display.set_mode((1, 1))
        self._original_image = None
        self._cropped_backup = None
        self._path = None
        self._img = None
        self._w = 0
        self._h = 0
        self.msg = msg

        self.path = path 

    def _load(self, path):
        # ai/
        try:
            resolved_path = paths.get(path, path)
            image = pygame.image.load(resolved_path).convert_alpha()
            self._path = resolved_path
            self._original_image = image.copy()
            self._cropped_backup = image.copy()
            self._w, self._h = image.get_size()
            if self.msg:
                _gp_log(f"image '{self._path}' was load")
            return image
        except FileNotFoundError:
            raise FileNotFoundError(f"file '{path}' not found. (in {resolved_path})")

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value):
        self._img = self._load(value)
    # ai
    def crop(self, x, y, width, height):
        if self._original_image:
            rect = Rect(x, y, width, height)
            cropped = self._original_image.subsurface(rect).copy()
            self._cropped_backup = self._original_image.copy()
            self._original_image = cropped
            self._img = cropped
            self._w, self._h = width, height
        return self

    def recrop(self):
        if self._cropped_backup:
            self._original_image = self._cropped_backup.copy()
            self._img = self._original_image.copy()
            self._w, self._h = self._img.get_size()
    def __call__(self):
        return self._img
    def __repr__(self):
        return repr(f'<Texture({self._img})>')

    @property
    def width(self): 
        return self._w
    @property
    def height(self): 
        return self._h

import pygame
from ..pather import *
from .. import _gp_log

pygame.mixer.init()

class Audio:
    def __init__(self, path, volume=5,mod=False):
        if mod:
            pygame.init()
            pygame.display.set_mode((1, 1))
        self.audio = None
        self._path = path
        self._volume = volume

        if isinstance(self._path, str) and self._path in paths:
            self._path = Path(paths[self._path])
        else:
            self._path = Path(path)

        if not self._path.exists():
            raise FileNotFoundError(f"file '{self._path}' not found.")
        else:
            _gp_log(f"audio '{self._path}' was _load")

        self._load()

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, new_path):
        new_path = Path(paths[new_path]) if isinstance(new_path, str) and new_path in paths else Path(new_path)
        if not new_path.exists():
            raise FileNotFoundError(f"file '{new_path}' not found.")
        self._path = new_path
        self._load()

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, new_volume):
        if not (0 <= new_volume <= 10):
            raise ValueError("Volume must be between 0 and 10.")
        self._volume = new_volume
        if self.audio:
            self.audio.set_volume(self._volume / 10)

    def _load(self):
        self.audio = pygame.mixer.Sound(str(self._path))
        self.audio.set_volume(self._volume / 10)

    def __call__(self):
        return [self.audio,self._path,self.volume]

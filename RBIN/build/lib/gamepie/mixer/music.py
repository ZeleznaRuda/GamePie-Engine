import pygame
from ..pather import *
from ..load.audio import Audio
from .. import _gp_log
class Music:
    def __init__(self, audio:Audio, auto_play=True, repeats=True):
        # ///ai
        self._audio = audio

        self._volume = audio.volume
        self._path = audio.path
        self.repeats = -1 if repeats else 0
        self._is_loaded = False

        self._load()
        self.volume = self._volume

        if auto_play:
            self.play()

    def _load(self):
        pygame.mixer.music.load(str(self._path)) 
        self._is_loaded = True

    def play(self):
        if self._is_loaded:
            pygame.mixer.music.play(self.repeats)

    def stop(self):
        pygame.mixer.music.stop()

    def pause(self):
        pygame.mixer.music.pause()

    def unpause(self):
        pygame.mixer.music.unpause()

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, value):
        self._volume = value
        pygame.mixer.music.set_volume(self._volume / 10) 
    def is_playing(self):
        # ai
        return pygame.mixer.music.get_busy()

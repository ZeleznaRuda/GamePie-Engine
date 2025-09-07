import pygame

from .. import _gp_log
from ..load import Audio
pygame.mixer.init()

class Sound:
    def __init__(self, audio:Audio):
        self._audio = audio

    def play(self):
        self._audio()[0].play()

    @property
    def volume(self):
        return self._audio.volume

    @volume.setter
    def volume(self, value):
        self._audio.volume = value
import sounddevice as sd
import numpy as np

class _Microphone:
    def __init__(self):
        self._volume = 0
    def _get_microphone_volume(self):
        duration = 0.1 
        sample_rate = 44100

        audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='float32')
        sd.wait()
        volume = np.linalg.norm(audio)
        return volume
    def update(self):
        self._volume = self._get_microphone_volume()
    @property
    def volume(self):
        return self._volume

microphone = _Microphone()
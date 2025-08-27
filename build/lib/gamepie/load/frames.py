import os
from PIL import Image
from ..time import wait
from .texture import Texture
from ..pather import paths
from .. import _gp_log

class Frames:
    def __init__(self, path, msg=True, mod=False):
        if mod:
            import pygame
            pygame.init()
            pygame.display.set_mode((1, 1))
        self.path_input = os.path.abspath(paths.get(path, path))
        self._current_index = 0
        self._loaded = False
        self.msg = msg
        self._load()

    def _load(self):
        if os.path.isdir(self.path_input):
            # Načtení snímků ze složky
            files = os.listdir(self.path_input)
            files.sort()
            self.files = [os.path.abspath(os.path.join(self.path_input, f)) for f in files]

        elif self.path_input.lower().endswith(".gif") and os.path.isfile(self.path_input):
            # Získání cesty ke složce, kde je tento soubor s kódem
            code_folder = os.path.dirname(os.path.abspath(__file__))
            compression_folder = os.path.join(code_folder, "compression")
            os.makedirs(compression_folder, exist_ok=True)

            # Složka pro aktuální GIF
            gif_name = os.path.splitext(os.path.basename(self.path_input))[0]
            frames_folder = os.path.join(compression_folder, f"{gif_name}_frames")
            os.makedirs(frames_folder, exist_ok=True)

            self.files = []
            with Image.open(self.path_input) as img:
                for frame in range(img.n_frames):
                    img.seek(frame)
                    frame_path = os.path.join(frames_folder, f"{gif_name}_{frame:03}.png")
                    img.save(frame_path, format="PNG")
                    self.files.append(frame_path)

        else:
            raise FileNotFoundError(f"Path '{self.path_input}' is not a valid folder or GIF file.")

        self._loaded = True
        if self.msg:
            _gp_log(f"frames '{self.path_input}' was loaded")

    def get(self, index=None):
        if index is not None:
            return Texture(self.files[index], msg=False)
        else:
            return [Texture(f, msg=False) for f in self.files]

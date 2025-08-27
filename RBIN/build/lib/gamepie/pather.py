import sys
from pathlib import Path

def resource_path(relative_path):
    try:
        base_path = Path(sys._MEIPASS)
    except AttributeError:
        base_path = Path(__file__).parent.resolve()
    return base_path / relative_path

BASE_DIR = Path(__file__).resolve().parent

ICON35   = resource_path("assets/icon/icon35x35.ico")
ICON24   = resource_path("assets/icon/icon24x24.ico")
ICON16   = resource_path("assets/icon/icon16x16.ico")
ICON70   = resource_path("assets/icon/icon700x700.ico")
def _gp_path_register_new(name,path):
        paths[name] = resource_path(path)
def _gp_path_register_del(name):
        paths.pop(name, None)
paths = {
    "pie":            resource_path("assets/pie.png"),
    "brick":          resource_path("assets/brick.png"),
    "mushroom":       resource_path("assets/mushroom.png"),
    "button_texture": resource_path("assets/button_texture.png"),
    "music":          resource_path("assets/music.mp3"),
    "pingsound":      resource_path("assets/ping-pong-ball.mp3"),
    "nomnom":         resource_path("assets/nom_nom.mp3"),
    "pacman":         resource_path("assets/pacman.png"),
    "tree":           resource_path("assets/tree.png"),
    "bush":           resource_path("assets/bush.png"),
    "avatar":         resource_path("assets/avatar.png"),
    "nyancat":        resource_path("assets/cat_space"),
    "elephant_run":   resource_path("assets/elephant_run-giphy.gif"),
    "bonk_doge":      resource_path("assets/bonk_doge-tenor.gif"),
}

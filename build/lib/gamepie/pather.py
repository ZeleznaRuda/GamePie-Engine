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

    "stone_brick":    resource_path("assets/stone.brick.block.png"),
    "grass":          resource_path("assets/grass.on.dirt.block.png"),
    "dirt":           resource_path("assets/dirt.block.png"),
    "stone":          resource_path("assets/stone.block.png"),
    "brick":          resource_path("assets/brick.block.png"),
    "oak":            resource_path("assets/oak.log.block.png"),
    "glass":          resource_path("assets/glass.block.png"),
    "leaves":         resource_path("assets/leaves.block.png"),
    "oak_planks":     resource_path("assets/oak.planks.block.png"),
    "door":           resource_path("assets/door.png"),
    "stone_stairs":   resource_path("assets/stone.stairs.png"),

    

    "mushroom":       resource_path("assets/mushroom.png"),
    "button_texture": resource_path("assets/button_texture.png"),
    "music":          resource_path("assets/music.mp3"),
}

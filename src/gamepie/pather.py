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

    "gp:brick_building.textures.stone_brick":    resource_path("assets/bbAssets/stone.brick.block.png"),
    "gp:brick_building.textures.grass":          resource_path("assets/bbAssets/grass.on.dirt.block.png"),
    "gp:brick_building.textures.dirt":           resource_path("assets/bbAssets/dirt.block.png"),
    "gp:brick_building.textures.stone":          resource_path("assets/bbAssets/stone.block.png"),
    "gp:brick_building.textures.brick":          resource_path("assets/bbAssets/brick.block.png"),
    "gp:brick_building.textures.oak":            resource_path("assets/bbAssets/oak.log.block.png"),
    "gp:brick_building.textures.glass":          resource_path("assets/bbAssets/glass.block.png"),
    "gp:brick_building.textures.leaves":         resource_path("assets/bbAssets/leaves.block.png"),
    "gp:brick_building.textures.oak_planks":     resource_path("assets/bbAssets/oak.planks.block.png"),
    "gp:brick_building.textures.door":           resource_path("assets/bbAssets/door.png"),
    "gp:brick_building.textures.stone_stairs":   resource_path("assets/bbAssets/stone.stairs.png"),

    "gp:gp.textures.pie":                        resource_path("assets/pie.png"),
    "gp:gp.textures.mushroom":                   resource_path("assets/mushroom.png"),
    "gp:gp.textures.button_texture":             resource_path("assets/button_texture.png"),
    "gp:gp.sound.music":                         resource_path("assets/music.mp3"),
}

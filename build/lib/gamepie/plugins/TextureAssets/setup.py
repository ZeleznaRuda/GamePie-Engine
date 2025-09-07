from gamepie.pather import _gp_path_register_new as _gp_reg

__gp_registered_paths = {}

def _gp_register(name, path):
    __gp_registered_paths[name] = path
    _gp_reg(name, path)

def help():
    print("Textures:")
    for name, path in __gp_registered_paths.items():
        print(f"{name}: {path}")

_gp_register('texture.platformer.brick', r"plugins\TextureAssets\libTextures\brick.png")
_gp_register('texture.system.mushroom', r"plugins\TextureAssets\libTextures\mushroom.png")
_gp_register('texture.system.pie', r"plugins\TextureAssets\libTextures\pie.png")
